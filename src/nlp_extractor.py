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
    return soup.get_text(separator=" ").lower()

def extract_skills(description_html: str) -> list:
    """
    Parses the job description and uses Keyword Matching (basic NLP) 
    to extract technical skills.
    """
    text = clean_html(description_html)
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
