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

## 🎯 Top 40+ Platforms for Remote Tech Jobs (Η Απόλυτη Λίστα)

If you are looking for remote jobs in Data Science, Engineering, or Software Development, here is the ultimate, enriched list of platforms you should check. We categorized them based on what you are looking for:

### 🏆 The Giants (Τα Κορυφαία & Πιο Γνωστά)
1. **[Remote OK](https://remoteok.com/)**: *Best for High-Paying Roles.* One of the most popular boards globally, known for listings from US companies hiring worldwide with excellent compensation.
2. **[We Work Remotely](https://weworkremotely.com/)**: *Best for Established Companies.* The oldest and largest remote work community. If a big tech company goes remote, they post here.
3. **[Remotive](https://remotive.com/)**: *Best for Tech Focus.* Great filtering, specifically tailored for software developers and data professionals.
4. **[FlexJobs](https://www.flexjobs.com/)**: *Best for Scam-Free Search.* Hand-screened remote jobs. It requires a subscription, but guarantees zero spam or fake listings.
5. **[LinkedIn](https://www.linkedin.com/jobs/)**: *Best for Networking.* Set location to "Worldwide" and select the "Remote" filter. Applying via LinkedIn Easy Apply while messaging the recruiter is a powerful tactic.
6. **[Dynamite Jobs](https://dynamitejobs.com/)**: *Best for Quality.* Every job is 100% remote and manually vetted by their team.

### 🧠 Vetted Freelance & Top Tier (Για Senior / Έμπειρους)
7. **[Toptal](https://www.toptal.com/)**: *Best for $100+/hr Rates.* "Top 3%" vetted network. You must pass rigorous algorithms and interviews, but once in, you get matched with top Silicon Valley clients.
8. **[Turing](https://www.turing.com/)**: *Best for AI Matching.* Similar to Toptal, heavily focused on matching vetted developers with US companies for long-term remote contracts.
9. **[Arc.dev](https://arc.dev/)**: *Best for Full-Time Remote.* Specifically designed to help remote developers find full-time salaried roles, not just freelance gigs.
10. **[Gun.io](https://www.gun.io/)**: *Best for Elite Freelancers.* Premium platform connecting highly skilled devs with great companies. Very high standards.
11. **[Braintrust](https://www.usebraintrust.com/)**: *Best for Web3 Ethos.* A decentralized, user-owned talent network where you keep 100% of your earnings.
12. **[Crossover](https://www.crossover.com/)**: *Best for High-Pay / High-Intensity.* Offers $100k+ roles, but requires passing extreme cognitive and technical tests.
13. **[X-Team](https://x-team.com/)**: *Best for Developer Community.* Join an exclusive community of developers working for massive brands like Riot Games.
14. **[Clevertech](https://www.clevertech.biz/)**: *Best for Premium Tech Culture.* Highly sought-after remote tech roles with excellent benefits.

### 🚀 Startups & Tech Specific (Για Καινοτόμες Εταιρείες)
15. **[Wellfound (AngelList)](https://wellfound.com/)**: *Best for Startups & Equity.* The absolute best place to find remote jobs at early-stage startups where you can negotiate stock options.
16. **[Otta](https://otta.com/)**: *Best for Modern Tech.* Highly curated jobs at fast-growing, trendy tech companies. Has the best user interface for job seekers.
17. **[Y Combinator (Work at a Startup)](https://www.workatastartup.com/)**: *Best for YC Companies.* Find remote roles directly in startups backed by the most famous accelerator in the world.
18. **[Built In](https://builtin.com/jobs/remote)**: *Best for US Hubs.* Originally focused on local hubs (Built In NYC, Built In Austin), now features a massive "Remote" section for tech roles.
19. **[Dice](https://www.dice.com/)**: *Best for Traditional IT.* The classic tech job board. Excellent if you are looking for enterprise Data Engineering or Cloud roles.
20. **[The Muse](https://www.themuse.com/search/remote)**: *Best for Culture Insights.* Shows detailed company profiles and culture videos alongside job postings.

### 🌐 Hidden Gems & Aggregators (Εργαλεία Συλλογής)
21. **[Working Nomads](https://www.workingnomads.com/jobs)**: *Best for Digital Nomads.* Curated list sent via newsletter.
22. **[JustRemote](https://justremote.co/)**: *Best for Hidden Jobs.* Uncovers jobs that aren't advertised on the major job boards.
23. **[Remote.co](https://remote.co/)**: *Best for Diversity.* Cultivated list by the FlexJobs team, covering many non-tech roles too.
24. **[Himalayas](https://himalayas.app/)**: *Best for Company Insights.* Beautiful UI, provides deep data on the tech stack and culture of the hiring companies.
25. **[Jobspresso](https://jobspresso.co/)**: *Best for Curation.* Expertly curated remote jobs in tech, marketing, etc.
26. **[DailyRemote](https://dailyremote.com/)**: *Best for Daily Updates.* Consistently updated with fresh listings.
27. **[NoDesk](https://nodesk.co/)**: *Best for Nomad Resources.* Besides jobs, it offers great articles on remote life and taxes.
28. **[Pangian](https://pangian.com/)**: *Best for Global Community.* A global community network with a solid job board.
29. **[SkipTheDrive](https://www.skipthedrive.com/)**: *Best for Free Searching.* A completely free remote job search engine.
30. **[Remote Leaf](https://remoteleaf.com/)**: *Best for Personalized Alerts.* Aggregates jobs from everywhere and sends them to your inbox.

### ⛓️ Niche (Web3, Freelance, Specific Tech)
31. **[Upwork](https://www.upwork.com/)**: *Best for Quick Gigs.* The biggest general freelance platform. Great for building a portfolio.
32. **[Fiverr](https://www.fiverr.com/)**: *Best for Productized Services.* Sell your skills as a product (e.g., "I will build an ETL pipeline for $500").
33. **[Freelancer](https://www.freelancer.com/)**: *Best for Global Competition.* Massive global freelance marketplace.
34. **[PeoplePerHour](https://www.peopleperhour.com/)**: *Best for European Market.* A solid alternative to Upwork, highly popular in the UK/EU.
35. **[Guru](https://www.guru.com/)**: *Best for Enterprise Freelance.* Great for longer-term B2B freelance contracts.
36. **[Codeable](https://codeable.io/)**: *Best for WordPress Experts.* Vetted freelance platform exclusively for WP developers.
37. **[Authentic Jobs](https://authenticjobs.com/)**: *Best for Designers & Frontend.* A premium board for web professionals.
38. **[Dribbble Jobs](https://dribbble.com/jobs)**: *Best for UI/UX & Graphic Designers.* The top spot for remote design roles.
39. **[Topcoder](https://www.topcoder.com/)**: *Best for Competitive Coding.* Win challenges to get paid and get hired.
40. **[Web3 Jobs](https://web3.career/)**: *Best for Blockchain.* The go-to place for Blockchain, Solidity, and Web3 Data roles.
41. **[Crypto Jobs List](https://cryptojobslist.com/)**: *Best for Crypto.* The #1 site for remote jobs in the cryptocurrency space.
42. **[Python.org Jobs](https://www.python.org/jobs/)**: *Best for Pythonistas.* Official Python job board (many remote listings).
43. **[RubyNow](https://rubynow.com/)**: *Best for Ruby Devs.* Dedicated entirely to Ruby/Rails developers.

> **Pro Tip:** When applying for remote roles, emphasize your **asynchronous communication skills**, your ability to work autonomously, and your experience with tools like Slack, Jira, and GitHub in your Cover Letter!

---

<div align="center">
  <b>Built by <a href="https://karidasd.github.io/">Karydas</a></b><br>
  <i>AI & Data Science Instructor / PhD Candidate</i>
</div>
