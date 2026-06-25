import logging
from src.database import init_db, save_job_to_db
from src.fetch_jobs import fetch_software_jobs
from src.nlp_extractor import extract_skills

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(message)s')

def run_etl():
    """
    The main ETL pipeline:
    Extract: Fetch jobs from API
    Transform: Extract skills using NLP
    Load: Save to SQLite
    """
    logging.info("🚀 Starting AI Remote Job Aggregator ETL Pipeline...")
    
    # 1. Initialize Database
    init_db()
    
    # 2. Extract Jobs
    jobs = fetch_software_jobs()
    
    # 3. Transform & Load
    jobs_processed = 0
    for job in jobs:
        job_id = job.get("id")
        title = job.get("title")
        company = job.get("company_name")
        url = job.get("url")
        pub_date = job.get("publication_date")
        description = job.get("description", "")
        
        # NLP Extraction
        skills = extract_skills(description)
        
        # Save to DB
        save_job_to_db(job_id, title, company, url, pub_date, skills)
        jobs_processed += 1
        
    logging.info(f"✅ ETL Complete! Processed and stored {jobs_processed} remote jobs.")

if __name__ == "__main__":
    run_etl()
