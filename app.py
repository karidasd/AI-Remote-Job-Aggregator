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
    st.subheader("Deep Job Filtering")
    # Filters
    col_search1, col_search2 = st.columns(2)
    with col_search1:
        search_term = st.text_input("🔍 Search by Job Title or Company...")
    with col_search2:
        source_options = jobs_df['source'].unique().tolist() if 'source' in jobs_df.columns else []
        selected_sources = st.multiselect("Filter by Source:", options=source_options, default=source_options)
        
    skill_counts = skills_df['skill'].value_counts().reset_index()
    skill_counts.columns = ['Skill', 'Count']
    selected_skills = st.multiselect("Filter by Skills Required:", options=skill_counts['Skill'].tolist())
    
    # Filter logic
    filtered_df = display_df.copy()
    
    if search_term:
        filtered_df = filtered_df[filtered_df['title'].str.contains(search_term, case=False, na=False) | 
                                filtered_df['company'].str.contains(search_term, case=False, na=False)]
        
    if selected_skills:
        for sk in selected_skills:
            filtered_df = filtered_df[filtered_df['skill'].str.contains(sk, case=False, na=False)]
            
    if selected_sources and 'source' in filtered_df.columns:
        filtered_df = filtered_df[filtered_df['source'].isin(selected_sources)]
            
    # Premium DataFrame Display
    st.dataframe(
        filtered_df[['title', 'company', 'source', 'salary', 'skill', 'published_at', 'url']].sort_values('published_at', ascending=False),
        column_config={
            "title": "Job Title",
            "company": "Company",
            "source": "Platform",
            "salary": "Salary",
            "skill": "Extracted Skills",
            "published_at": "Posted On",
            "url": st.column_config.LinkColumn("Apply Here")
        },
        hide_index=True,
        use_container_width=True,
        height=500
    )

with tab2:
    st.subheader("🤖 ML Resume Matcher (TF-IDF & Cosine Similarity)")
    st.markdown("Paste your skills here, and our **Machine Learning model** will calculate semantic similarity against all open jobs!")
    user_skills = st.text_area("Your Tech Stack (e.g. Python, SQL, AWS, Docker):", "Python, SQL, Pandas, Machine Learning")
    
    if st.button("Run ML Similarity Search"):
        with st.spinner("Running TF-IDF Vectorizer..."):
            # Prepare corpus: Job Skills
            corpus = display_df['skill'].tolist()
            corpus = [s if s else "unknown" for s in corpus]
            
            # Append user skills to the end of corpus
            corpus.append(user_skills)
            
            # TF-IDF
            vectorizer = TfidfVectorizer()
            tfidf_matrix = vectorizer.fit_transform(corpus)
            
            # Calculate Cosine Similarity between user_skills (last row) and all jobs
            cosine_sim = cosine_similarity(tfidf_matrix[-1], tfidf_matrix[:-1]).flatten()
            
            # Add to dataframe
            ml_df = display_df.copy()
            ml_df['Match_Score'] = (cosine_sim * 100).astype(int)
            best_matches = ml_df.sort_values('Match_Score', ascending=False).head(10)
            
            st.success("ML Analysis Complete! Here are your top 10 job matches based on mathematical similarity:")
            st.dataframe(
                best_matches[['Match_Score', 'title', 'company', 'source', 'salary', 'url']],
                column_config={"Match_Score": st.column_config.ProgressColumn("Match %", min_value=0, max_value=100, format="%d%%"), "url": st.column_config.LinkColumn("Apply")},
                hide_index=True, use_container_width=True
            )

with tab3:
    st.subheader("📝 AI Cover Letter Prompt Engineer")
    st.markdown("Select a job below. The AI will generate a highly optimized prompt tailored to this job's skills. Copy the prompt and paste it into ChatGPT!")
    
    job_titles = display_df['title'].tolist()
    selected_job_title = st.selectbox("Select a Job:", job_titles)
    
    if selected_job_title:
        job_data = display_df[display_df['title'] == selected_job_title].iloc[0]
        company = job_data['company']
        req_skills = job_data['skill']
        
        st.write("---")
        st.markdown(f"**Target Company:** {company}")
        st.markdown(f"**Extracted Skills:** {req_skills if req_skills else 'None detected'}")
        
        st.write("---")
        st.markdown("### ✨ Your Custom ChatGPT Prompt")
        prompt = f"""Act as an expert Career Coach and Copywriter. I am applying for the '{selected_job_title}' position at '{company}'. 

Here are the core technical skills they are looking for: {req_skills}.

Please write a highly professional, engaging, and concise Cover Letter for me. Focus on my ability to work autonomously in a remote environment, my strong asynchronous communication skills, and highlight how my experience aligns with the specific technologies mentioned above. 

Do not use overly robotic language; make it sound human, passionate, and direct. Keep it under 300 words."""

        st.code(prompt, language="markdown")
        st.info("💡 Click the copy button on the top right of the code block, and paste it into ChatGPT!")

with tab4:
    st.subheader("📈 Tech Market Insights")
    st.markdown("Real-time analytics based on the scraped job data.")
    
    col_chart1, col_chart2 = st.columns(2)
    
    with col_chart1:
        # Top 10 Skills Bar Chart
        top_skills = skill_counts.head(10)
        fig_bar = px.bar(top_skills, x='Count', y='Skill', orientation='h', 
                         title="🔥 Top 10 Most In-Demand Skills",
                         color='Count', color_continuous_scale='Blues')
        fig_bar.update_layout(plot_bgcolor="rgba(0,0,0,0)", paper_bgcolor="rgba(0,0,0,0)", font_color="white")
        st.plotly_chart(fig_bar, use_container_width=True)
        
    with col_chart2:
        # Source Platform Pie Chart
        if 'source' in jobs_df.columns:
            source_counts = jobs_df['source'].value_counts().reset_index()
            source_counts.columns = ['Source', 'Count']
            fig_pie = px.pie(source_counts, values='Count', names='Source', 
                             title="📡 Job Distribution by Platform", hole=0.4)
            fig_pie.update_layout(plot_bgcolor="rgba(0,0,0,0)", paper_bgcolor="rgba(0,0,0,0)", font_color="white")
            st.plotly_chart(fig_pie, use_container_width=True)
        else:
            st.info("Source data not available yet.")
