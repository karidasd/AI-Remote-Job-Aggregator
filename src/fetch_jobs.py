import requests
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def fetch_remotive() -> list:
    url = "https://remotive.com/api/remote-jobs?category=software-dev"
    logging.info("Fetching jobs from Remotive...")
    try:
        resp = requests.get(url, timeout=15)
        resp.raise_for_status()
        jobs = resp.json().get("jobs", [])
        formatted = []
        for j in jobs[:50]:
            formatted.append({
                "id": f"remotive_{j.get('id')}",
                "title": j.get("title"),
                "company": j.get("company_name"),
                "url": j.get("url"),
                "published_at": j.get("publication_date"),
                "description": j.get("description", ""),
                "source": "Remotive"
            })
        return formatted
    except Exception as e:
        logging.error(f"Remotive Error: {e}")
        return []

def fetch_arbeitnow() -> list:
    url = "https://arbeitnow.com/api/job-board-api"
    logging.info("Fetching jobs from Arbeitnow...")
    try:
        resp = requests.get(url, timeout=15)
        resp.raise_for_status()
        jobs = resp.json().get("data", [])
        formatted = []
        for j in jobs[:50]:
            # Arbeitnow returns remote jobs, we filter software specifically later or assume API returns general tech
            formatted.append({
                "id": f"arbeitnow_{j.get('slug')}",
                "title": j.get("title"),
                "company": j.get("company_name"),
                "url": j.get("url"),
                "published_at": str(j.get("created_at")),
                "description": j.get("description", ""),
                "source": "Arbeitnow"
            })
        return formatted
    except Exception as e:
        logging.error(f"Arbeitnow Error: {e}")
        return []

def fetch_remoteok() -> list:
    url = "https://remoteok.com/api"
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"}
    logging.info("Fetching jobs from RemoteOK...")
    try:
        resp = requests.get(url, headers=headers, timeout=15)
        resp.raise_for_status()
        jobs = resp.json()
        formatted = []
        # Skip the first element which is usually legal text in RemoteOK API
        for j in jobs[1:51]:
            formatted.append({
                "id": f"remoteok_{j.get('id')}",
                "title": j.get("position"),
                "company": j.get("company"),
                "url": j.get("apply_url") or j.get("url"),
                "published_at": j.get("date"),
                "description": j.get("description", ""),
                "source": "RemoteOK"
            })
        return formatted
    except Exception as e:
        logging.error(f"RemoteOK Error: {e}")
        return []

def fetch_all_jobs() -> list:
    """Aggregates jobs from multiple remote platforms."""
    all_jobs = []
    all_jobs.extend(fetch_remotive())
    all_jobs.extend(fetch_arbeitnow())
    all_jobs.extend(fetch_remoteok())
    logging.info(f"🎉 Successfully aggregated {len(all_jobs)} jobs from 3 different sources!")
    return all_jobs
