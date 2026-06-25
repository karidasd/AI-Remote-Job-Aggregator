import sqlite3
import logging
import os

DB_PATH = "data/jobs.db"

def init_db():
    """Initializes the SQLite database with jobs and skills tables."""
    os.makedirs(os.path.dirname(DB_PATH), exist_ok=True)
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    
    # Table for Jobs
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS jobs (
            job_id TEXT PRIMARY KEY,
            title TEXT,
            company TEXT,
            url TEXT,
            published_at TEXT
        )
    ''')
    
    # Table for Skills associated with jobs
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS job_skills (
            job_id TEXT,
            skill TEXT,
            FOREIGN KEY(job_id) REFERENCES jobs(job_id)
        )
    ''')
    
    conn.commit()
    conn.close()
    logging.info("Database initialized successfully.")

def save_job_to_db(job_id, title, company, url, published_at, skills):
    """Saves a job and its extracted skills to the database."""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    
    try:
        # Insert job (IGNORE if it already exists to prevent duplicates)
        cursor.execute('''
            INSERT OR IGNORE INTO jobs (job_id, title, company, url, published_at)
            VALUES (?, ?, ?, ?, ?)
        ''', (str(job_id), title, company, url, published_at))
        
        # If the job was actually inserted, insert its skills
        if cursor.rowcount > 0:
            for skill in skills:
                cursor.execute('''
                    INSERT INTO job_skills (job_id, skill)
                    VALUES (?, ?)
                ''', (str(job_id), skill))
        
        conn.commit()
    except Exception as e:
        logging.error(f"Error saving job {job_id}: {e}")
    finally:
        conn.close()
