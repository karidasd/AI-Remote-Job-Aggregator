<div align="center">
  <img src="assets/logo.png" alt="AI Remote Job Aggregator Logo" width="200"/>
  <h1>AI Remote Job Aggregator</h1>
  <p><em>An automated Data Pipeline & Dashboard that scrapes remote tech jobs and uses NLP to extract in-demand skills.</em></p>
  
  ![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
  ![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=Streamlit&logoColor=white)
  ![SQLite](https://img.shields.io/badge/SQLite-07405E?style=for-the-badge&logo=sqlite&logoColor=white)
  ![NLP](https://img.shields.io/badge/NLP-Keyword_Extraction-8A2BE2?style=for-the-badge)
</div>

---

<!-- LIVE_JOBS_START -->

### 🔴 LIVE: Top 5 Remote Jobs of the Day

| Job Title | Company | Salary | Apply |
|-----------|---------|--------|-------|
| Director of Procurement | Kardion | **Not Specified** | [Apply Here](https://remoteOK.com/remote-jobs/remote-director-of-procurement-kardion-1134002) |
| Junior Business Analyst | Work Force Nexus | **Not Specified** | [Apply Here](https://remoteOK.com/remote-jobs/remote-junior-business-analyst-work-force-nexus-1133994) |
| Bookkeeper | Pickle | **Not Specified** | [Apply Here](https://remoteOK.com/remote-jobs/remote-bookkeeper-pickle-1133991) |
| Youth Mental Wellness Coach | ð Clayful | **Not Specified** | [Apply Here](https://remoteOK.com/remote-jobs/remote-youth-mental-wellness-coach-3-clayful-1134067) |
| Monitor de Concursos RaciocÃ­nio LÃ³gico + InformÃ¡tica | VÃ­cio | **Not Specified** | [Apply Here](https://remoteOK.com/remote-jobs/remote-monitor-de-concursos-raciocinio-logico-informatica-vicio-1134051) |

*(Auto-updated by GitHub Actions CRON bot 🤖)*

<!-- LIVE_JOBS_END -->

---

## 📖 About The Project

This project acts as an automated **Data Engineering pipeline**. It fetches the latest remote job postings for Data & Software roles from public APIs, cleans the HTML job descriptions, and applies **Natural Language Processing (NLP)** techniques to extract technical skills (e.g., Python, AWS, React, Kubernetes). 

The results are stored locally in an SQLite database and visualized on a beautiful **Streamlit Dashboard** using Plotly.

## 🔥 Enterprise-Grade Features Added:
- **Autonomous CRON Data Pipeline:** Integrated with **GitHub Actions** (`daily_scrape.yml`). This repository literally runs by itself! It wakes up every day at midnight, runs the Python ETL pipeline, scrapes new jobs, and commits the updated `jobs.db` back to the repository.
- **AI Resume Matcher:** Added an interactive "Beta" AI tool in the dashboard that simulates matching your specific tech stack to the current open jobs, providing a dynamic Match Score.
- **Deep Analytics Dashboard:** Re-engineered the Streamlit UI using custom CSS, Plotly Treemaps, and interactive DataFrames with URL columns.

## 🚀 How to Run

1. **Install Dependencies:** `pip install -r requirements.txt`
2. **Fetch Data (ETL):** `python main.py` (or `make fetch`)
3. **Start Dashboard:** `streamlit run app.py` (or `make run`)

---

# 🌍 The Ultimate Guide to Remote Work (Οδηγός για Remote Εργασία)

Welcome to the comprehensive guide on finding and securing remote work in the tech industry!
*Καλώς ήρθατε στον πλήρη οδηγό για εύρεση απομακρυσμένης εργασίας στον κλάδο της τεχνολογίας!*

## 🟢 Pros of Remote Work (Πλεονεκτήματα)
- **Global Opportunities (Παγκόσμιες Ευκαιρίες):** You are not limited to your local job market. You can work for a company in San Francisco while living in Athens.
- **Higher Salaries (Υψηλότεροι Μισθοί):** Companies in tech hubs often pay significantly more than local averages, even when adjusted for location.
- **Flexibility & Work-Life Balance (Ευελιξία):** No commuting time, flexible working hours (often async), leading to a better quality of life.

## 🔴 Cons of Remote Work (Μειονεκτήματα)
- **Isolation (Απομόνωση):** Lack of physical social interaction with colleagues can sometimes feel lonely.
- **Time Zone Differences (Διαφορές Ώρας):** Working with a team in PST while you are in CET can lead to late-night meetings.
- **Self-Discipline (Αυτοπειθαρχία):** You must be highly organized and proactive in communicating your progress.

## 🎯 Top 30+ Platforms for Remote Tech Jobs (Η Απόλυτη Λίστα)

If you are looking for remote jobs in Data Science, Engineering, or Software Development, here is the ultimate list of platforms you should check:

### 🏆 The Giants (Τα Κορυφαία)
1. **[Remote OK](https://remoteok.com/)**: One of the most popular boards globally. High-paying roles.
2. **[We Work Remotely](https://weworkremotely.com/)**: The largest remote work community. Excellent for engineering.
3. **[Remotive](https://remotive.com/)**: Great filtering, specifically tailored for tech professionals.
4. **[FlexJobs](https://www.flexjobs.com/)**: Hand-screened remote jobs (requires subscription, but very high quality).
5. **[LinkedIn](https://www.linkedin.com/jobs/)**: Set location to "Worldwide" and select the "Remote" filter.

### 🧠 Vetted Freelance & Top Tier (Για Senior / Έμπειρους)
6. **[Toptal](https://www.toptal.com/)**: "Top 3%" vetted network. Pass the test, get matched with Silicon Valley.
7. **[Turing](https://www.turing.com/)**: AI-backed matching for vetted developers.
8. **[Arc.dev](https://arc.dev/)**: Specifically for remote developers looking for full-time or freelance.
9. **[Gun.io](https://www.gun.io/)**: Premium platform connecting elite devs with great companies.
10. **[Braintrust](https://www.usebraintrust.com/)**: User-owned talent network (Web3 vibe).

### 🚀 Startups & Tech Specific
11. **[Wellfound (AngelList)](https://wellfound.com/)**: The absolute best place for remote Startup jobs.
12. **[Otta](https://otta.com/)**: Highly curated jobs at fast-growing tech companies.
13. **[Y Combinator (Work at a Startup)](https://www.workatastartup.com/)**: Find remote roles directly in YC-backed startups.
14. **[Built In](https://builtin.com/jobs/remote)**: Great for US-based tech hubs hiring globally.
15. **[Dice](https://www.dice.com/)**: The classic tech job board, with strong remote filters.

### 🌐 Hidden Gems & Aggregators
16. **[Working Nomads](https://www.workingnomads.com/jobs)**: Newsletter and job board for digital nomads.
17. **[JustRemote](https://justremote.co/)**: Covers many niches including Data and Design.
18. **[Remote.co](https://remote.co/)**: Cultivated list of remote opportunities by the FlexJobs team.
19. **[Himalayas](https://himalayas.app/)**: Beautiful UI, fast-growing remote job board.
20. **[Jobspresso](https://jobspresso.co/)**: Expertly curated remote jobs in tech, marketing, etc.
21. **[DailyRemote](https://dailyremote.com/)**: Daily updates on remote jobs.
22. **[NoDesk](https://nodesk.co/)**: Remote jobs and resources for the digital nomad.
23. **[Pangian](https://pangian.com/)**: A global community with a solid job board.
24. **[SkipTheDrive](https://www.skipthedrive.com/)**: Free remote job search engine.
25. **[Remote Leaf](https://remoteleaf.com/)**: Aggregates jobs from everywhere.

### ⛓️ Niche (Web3, Freelance, Specific Tech)
26. **[Upwork](https://www.upwork.com/)**: The biggest general freelance platform.
27. **[Fiverr](https://www.fiverr.com/)**: Productize your tech services (e.g., "I will build an ETL pipeline").
28. **[Freelancer](https://www.freelancer.com/)**: Global freelance marketplace.
29. **[Web3 Jobs](https://web3.career/)**: For Blockchain, Solidity, and Web3 Data roles.
30. **[Crypto Jobs List](https://cryptojobslist.com/)**: The #1 site for Crypto remote jobs.
31. **[Python.org Jobs](https://www.python.org/jobs/)**: Official Python job board (many remote listings).
32. **[RubyNow](https://rubynow.com/)**: For Ruby/Rails developers.

> **Pro Tip:** When applying for remote roles, emphasize your **asynchronous communication skills** and your ability to work autonomously in your Cover Letter!

---

<div align="center">
  <b>Built by <a href="https://karidasd.github.io/">Karydas</a></b><br>
  <i>AI & Data Science Instructor / PhD Candidate</i>
</div>
