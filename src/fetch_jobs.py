import requests
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def fetch_software_jobs() -> list:
    """
    Fetches the latest remote Software Development and Data jobs from the Remotive API.
    Returns a list of job dictionaries.
    """
    url = "https://remotive.com/api/remote-jobs?category=software-dev"
    logging.info(f"Fetching jobs from {url}")
    
    try:
        response = requests.get(url, timeout=15)
        response.raise_for_status()
        data = response.json()
        jobs = data.get("jobs", [])
        logging.info(f"Successfully fetched {len(jobs)} jobs.")
        # Limit to the top 100 most recent jobs for performance in this project
        return jobs[:100]
    except requests.exceptions.RequestException as e:
        logging.error(f"Failed to fetch jobs: {e}")
        return []
