import re
from bs4 import BeautifulSoup

# A predefined dictionary of core Tech Skills we want our NLP to look for
TECH_SKILLS = [
    "python", "java", "javascript", "typescript", "c++", "c#", "ruby", "go", "rust",
    "sql", "nosql", "postgresql", "mysql", "mongodb", "redis",
    "aws", "azure", "gcp", "docker", "kubernetes", "terraform",
    "react", "angular", "vue", "node.js", "django", "flask", "fastapi",
    "machine learning", "data science", "pandas", "spark", "hadoop", "airflow",
    "nlp", "pytorch", "tensorflow", "ci/cd", "agile", "scrum"
]

def clean_html(raw_html: str) -> str:
    """Removes HTML tags from the job description."""
    if not raw_html:
        return ""
    soup = BeautifulSoup(raw_html, "html.parser")
    return soup.get_text(separator=" ")

def extract_salary(description_html: str) -> str:
    """Uses Regex to find salary patterns (e.g., $100k - $150k, 100,000 USD)."""
    text = clean_html(description_html)
    
    # Common salary patterns
    patterns = [
        r'\$\d{2,3}k\s*-\s*\$\d{2,3}k',           # $100k - $150k
        r'\$\d{2,3},\d{3}\s*-\s*\$\d{2,3},\d{3}', # $100,000 - $150,000
        r'\d{2,3}k\s*(?:USD|EUR)',                # 100k USD
        r'\$\d{2,3}k(?!\s*-)'                     # $120k (standalone)
    ]
    
    for pattern in patterns:
        match = re.search(pattern, text, re.IGNORECASE)
        if match:
            return match.group(0).upper()
            
    return "Not Specified"

def extract_skills(description_html: str) -> list:
    """
    Parses the job description and uses Keyword Matching (basic NLP) 
    to extract technical skills.
    """
    text = clean_html(description_html).lower()
    found_skills = set()
    
    # Tokenize by splitting non-word characters
    words = re.split(r'\W+', text)
    
    # Check for exact matches
    for skill in TECH_SKILLS:
        if skill in text:
            # Extra check for standalone words to avoid sub-string matching
            # e.g., 'go' matching inside 'algorithm'
            pattern = rf'\b{re.escape(skill)}\b'
            if re.search(pattern, text):
                found_skills.add(skill.title())
                
    return list(found_skills)
