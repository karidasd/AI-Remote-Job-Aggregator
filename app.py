import streamlit as st
import sqlite3
import pandas as pd
import plotly.express as px
from datetime import datetime

# --- Page Configuration ---
st.set_page_config(page_title="AI Remote Job Hub", page_icon="🚀", layout="wide", initial_sidebar_state="expanded")

# --- Custom CSS for Premium UI ---
st.markdown("""
<style>
    .reportview-container .main .block-container{
        padding-top: 2rem;
    }
    .metric-card {
        background-color: #1E1E2E;
        border-radius: 10px;
        padding: 20px;
        box-shadow: 0 4px 6px rgba(0,0,0,0.3);
        text-align: center;
    }
    .metric-val { font-size: 36px; font-weight: bold; color: #00E5FF; }
    .metric-label { font-size: 14px; color: #A0A0B0; text-transform: uppercase; letter-spacing: 1px; }
</style>
""", unsafe_allow_html=True)

DB_PATH = "data/jobs.db"

@st.cache_data(ttl=3600)
def load_data():
    """Loads jobs and skills from SQLite with caching for speed."""
    try:
        conn = sqlite3.connect(DB_PATH)
        jobs_df = pd.read_sql_query("SELECT * FROM jobs", conn)
        skills_df = pd.read_sql_query("SELECT * FROM job_skills", conn)
        conn.close()
        
        if not jobs_df.empty:
            jobs_df['published_at'] = pd.to_datetime(jobs_df['published_at'])
            
        return jobs_df, skills_df
    except Exception as e:
        return pd.DataFrame(), pd.DataFrame()

jobs_df, skills_df = load_data()

# --- Sidebar ---
with st.sidebar:
    st.image("assets/logo.png", use_container_width=True)
    st.markdown("## 🧠 AI Job Engine")
    st.markdown("This dashboard runs autonomously via **GitHub Actions**, scraping daily remote tech jobs and using **NLP** to extract core skills.")
    st.divider()
    if not jobs_df.empty:
        st.info(f"Last updated: {jobs_df['published_at'].max().strftime('%Y-%m-%d')}")
    st.markdown("Built by [Karydas](https://karidasd.github.io/)")

# --- Main UI ---
st.title("🚀 Advanced AI Remote Job Hub")

if jobs_df.empty or skills_df.empty:
    st.error("No data found. Please run the ETL pipeline first (`python main.py`).")
    st.stop()

# --- Metrics Row ---
col1, col2, col3, col4 = st.columns(4)
with col1:
    st.markdown(f"<div class='metric-card'><div class='metric-val'>{len(jobs_df)}</div><div class='metric-label'>Live Jobs</div></div>", unsafe_allow_html=True)
with col2:
    st.markdown(f"<div class='metric-card'><div class='metric-val'>{jobs_df['company'].nunique()}</div><div class='metric-label'>Companies Hiring</div></div>", unsafe_allow_html=True)
with col3:
    st.markdown(f"<div class='metric-card'><div class='metric-val'>{len(skills_df)}</div><div class='metric-label'>Skills Extracted</div></div>", unsafe_allow_html=True)
with col4:
    unique_skills = skills_df['skill'].nunique()
    st.markdown(f"<div class='metric-card'><div class='metric-val'>{unique_skills}</div><div class='metric-label'>Unique Technologies</div></div>", unsafe_allow_html=True)

st.write("")
st.write("")

# --- Tabs for Deep Analytics ---
tab1, tab2, tab3 = st.tabs(["📊 Skill Analytics", "💼 Job Explorer", "🤖 AI Matcher (Beta)"])

with tab1:
    st.subheader("Market Demand Analysis")
    c1, c2 = st.columns([2, 1])
    
    with c1:
        # Top Skills Bar Chart
        skill_counts = skills_df['skill'].value_counts().reset_index()
        skill_counts.columns = ['Skill', 'Demand']
        top_skills = skill_counts.head(20)
        
        fig = px.bar(top_skills, x='Demand', y='Skill', orientation='h', 
                     color='Demand', color_continuous_scale="Agalnith",
                     title="Top 20 Most Requested Tech Skills")
        fig.update_layout(yaxis={'categoryorder':'total ascending'}, plot_bgcolor='rgba(0,0,0,0)', paper_bgcolor='rgba(0,0,0,0)')
        st.plotly_chart(fig, use_container_width=True)
        
    with c2:
        # Treemap for visual flair
        fig2 = px.treemap(top_skills.head(10), path=['Skill'], values='Demand', 
                          color='Demand', color_continuous_scale="Blues",
                          title="Skill Weight Matrix")
        st.plotly_chart(fig2, use_container_width=True)

with tab2:
    st.subheader("Deep Job Filtering")
    # Filters
    search_term = st.text_input("🔍 Search by Job Title or Company...")
    selected_skills = st.multiselect("Filter by Skills Required:", options=skill_counts['Skill'].tolist())
    
    # Merge and filter logic
    skills_grouped = skills_df.groupby('job_id')['skill'].apply(lambda x: ', '.join(x)).reset_index()
    display_df = pd.merge(jobs_df, skills_grouped, on='job_id', how='left')
    display_df['skill'] = display_df['skill'].fillna('')
    
    if search_term:
        display_df = display_df[display_df['title'].str.contains(search_term, case=False, na=False) | 
                                display_df['company'].str.contains(search_term, case=False, na=False)]
        
    if selected_skills:
        for sk in selected_skills:
            display_df = display_df[display_df['skill'].str.contains(sk, case=False, na=False)]
            
    # Premium DataFrame Display
    st.dataframe(
        display_df[['title', 'company', 'skill', 'published_at', 'url']].sort_values('published_at', ascending=False),
        column_config={
            "title": "Job Title",
            "company": "Company",
            "skill": "Extracted Skills",
            "published_at": "Posted On",
            "url": st.column_config.LinkColumn("Apply Here")
        },
        hide_index=True,
        use_container_width=True,
        height=500
    )

with tab3:
    st.subheader("🤖 AI Resume Matcher (Simulated)")
    st.markdown("Paste your skills here, and the AI will score how well you match the current open jobs!")
    user_skills = st.text_area("Your Tech Stack (e.g. Python, SQL, AWS, Docker):", "Python, SQL, Pandas")
    
    if st.button("Calculate Match Scores"):
        with st.spinner("Running similarity matrix..."):
            user_skill_list = [s.strip().lower() for s in user_skills.split(',')]
            
            def calculate_score(job_skills_str):
                if not job_skills_str: return 0
                job_skills = [s.strip().lower() for s in job_skills_str.split(',')]
                if not job_skills: return 0
                matches = sum(1 for s in user_skill_list if s in job_skills)
                return min(100, int((matches / len(job_skills)) * 100))
                
            display_df['Match_Score'] = display_df['skill'].apply(calculate_score)
            best_matches = display_df.sort_values('Match_Score', ascending=False).head(5)
            
            st.success("Analysis Complete! Here are your top 5 job matches:")
            st.dataframe(
                best_matches[['Match_Score', 'title', 'company', 'skill', 'url']],
                column_config={"Match_Score": st.column_config.ProgressColumn("Match %", min_value=0, max_value=100, format="%d%%"), "url": st.column_config.LinkColumn("Apply")},
                hide_index=True, use_container_width=True
            )
