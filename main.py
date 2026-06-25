import logging
from src.database import init_db, save_job_to_db
from src.fetch_jobs import fetch_all_jobs
from src.nlp_extractor import extract_skills

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(message)s')

import os
import sqlite3
import pandas as pd

def update_readme():
    """Generates the Live Top 5 Jobs table and injects it into README.md"""
    logging.info("📝 Updating Live README...")
    conn = sqlite3.connect("data/jobs.db")
    df = pd.read_sql_query("SELECT title, company, url, salary FROM jobs ORDER BY published_at DESC LIMIT 5", conn)
    conn.close()
    
    if df.empty: return
    
    # Generate Markdown Table
    md_table = "### 🔴 LIVE: Top 5 Remote Jobs of the Day\n\n"
    md_table += "| Job Title | Company | Salary | Apply |\n"
    md_table += "|-----------|---------|--------|-------|\n"
    for _, row in df.iterrows():
        md_table += f"| {row['title']} | {row['company']} | **{row['salary']}** | [Apply Here]({row['url']}) |\n"
        
    md_table += "\n*(Auto-updated by GitHub Actions CRON bot 🤖)*\n"
    
    # Read README, replace placeholder
    readme_path = "README.md"
    try:
        with open(readme_path, "r", encoding="utf-8") as f:
            content = f.read()
            
        # We will inject between two marker comments
        start_marker = "<!-- LIVE_JOBS_START -->"
        end_marker = "<!-- LIVE_JOBS_END -->"
        
        if start_marker in content and end_marker in content:
            before = content.split(start_marker)[0]
            after = content.split(end_marker)[1]
            new_content = before + start_marker + "\n\n" + md_table + "\n" + end_marker + after
            
            with open(readme_path, "w", encoding="utf-8") as f:
                f.write(new_content)
            logging.info("✅ README updated successfully.")
    except Exception as e:
        logging.error(f"Failed to update README: {e}")

def run_etl():
    """
    The main ETL pipeline:
    Extract: Fetch jobs from APIs
    Transform: Extract skills using NLP
    Load: Save to SQLite
    """
    logging.info("🚀 Starting Multi-Source Remote Job ETL Pipeline...")
    
    # 1. Initialize Database
    init_db()
    
    # 2. Extract Jobs
    jobs = fetch_all_jobs()
    
    # 3. Transform & Load
    jobs_processed = 0
    for job in jobs:
        job_id = job.get("id")
        title = job.get("title")
        company = job.get("company")
        url = job.get("url")
        pub_date = job.get("published_at")
        description = job.get("description", "")
        source = job.get("source", "Unknown")
        
        # NLP Extraction
        skills = extract_skills(description)
        # Salary Extraction
        from src.nlp_extractor import extract_salary
        salary = extract_salary(description)
        
        # Save to DB
        save_job_to_db(job_id, title, company, url, pub_date, source, salary, skills)
        jobs_processed += 1
        
    logging.info(f"✅ ETL Complete! Processed and stored {jobs_processed} remote jobs.")
    
    # 4. Dynamic README Update
    update_readme()

if __name__ == "__main__":
    run_etl()
