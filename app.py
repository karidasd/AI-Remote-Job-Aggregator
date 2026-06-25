import streamlit as st
import sqlite3
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Remote Job AI Aggregator", page_icon="🌍", layout="wide")

DB_PATH = "data/jobs.db"

def load_data():
    """Loads jobs and skills from SQLite."""
    try:
        conn = sqlite3.connect(DB_PATH)
        jobs_df = pd.read_sql_query("SELECT * FROM jobs", conn)
        skills_df = pd.read_sql_query("SELECT * FROM job_skills", conn)
        conn.close()
        return jobs_df, skills_df
    except Exception as e:
        st.error("Database not found. Please run main.py first to fetch jobs.")
        return pd.DataFrame(), pd.DataFrame()

jobs_df, skills_df = load_data()

st.title("🌍 AI-Powered Remote Job Aggregator")
st.markdown("This dashboard automatically scrapes remote Data & Software jobs and uses **NLP** to extract the most in-demand skills.")

if not jobs_df.empty and not skills_df.empty:
    col1, col2, col3 = st.columns(3)
    col1.metric("Total Remote Jobs Found", len(jobs_df))
    col2.metric("Total Skills Extracted", len(skills_df))
    col3.metric("Unique Companies Hiring", jobs_df['company'].nunique())
    
    st.divider()
    
    st.header("📈 Top Requested Skills in Remote Jobs")
    # Count skill occurrences
    skill_counts = skills_df['skill'].value_counts().reset_index()
    skill_counts.columns = ['Skill', 'Count']
    top_skills = skill_counts.head(15)
    
    fig = px.bar(top_skills, x='Count', y='Skill', orientation='h', 
                 title="Most In-Demand Technologies", color='Count', color_continuous_scale="Viridis")
    fig.update_layout(yaxis={'categoryorder':'total ascending'})
    st.plotly_chart(fig, use_container_width=True)
    
    st.divider()
    
    st.header("💼 Latest Remote Opportunities")
    
    # Merge jobs with their skills for display
    skills_grouped = skills_df.groupby('job_id')['skill'].apply(lambda x: ', '.join(x)).reset_index()
    display_df = pd.merge(jobs_df, skills_grouped, on='job_id', how='left')
    
    # Show as an interactive table
    st.dataframe(
        display_df[['title', 'company', 'skill', 'published_at', 'url']],
        column_config={
            "title": "Job Title",
            "company": "Company",
            "skill": "Extracted Skills",
            "url": st.column_config.LinkColumn("Apply Link")
        },
        hide_index=True,
        use_container_width=True
    )
else:
    st.warning("No data available. Run `python main.py` in your terminal.")
