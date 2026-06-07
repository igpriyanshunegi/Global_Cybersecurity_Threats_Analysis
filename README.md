# 🛡️ Global Cybersecurity Threats Analysis (2015–2024)

> An Exploratory Data Analysis (EDA) project uncovering patterns, trends, and insights from a decade of global cyberattack data across industries and nations.

---

## 📌 Table of Contents

- [Project Overview](#-project-overview)
- [Problem Statement](#-problem-statement)
- [Dataset Description](#-dataset-description)
- [Tech Stack](#-tech-stack)
- [Project Structure](#-project-structure)
- [Key Analyses Performed](#-key-analyses-performed)
- [Visual Insights](#-visual-insights)
- [Key Findings](#-key-findings)
- [How to Run](#-how-to-run)
- [Author](#-author)

---

## 🔍 Project Overview

**Project Name:** Cyberattack Trends by Sector
**Project Type:** Exploratory Data Analysis (EDA)
**Domain:** Cybersecurity / Data Analytics
**Contribution:** Individual

Cybersecurity incidents have become a critical threat across industries — from finance and healthcare to government and retail. This project systematically analyzes **3,000 publicly reported cyber incidents** spanning **10 years (2015–2024)** across **10 countries**, to extract actionable intelligence on:

- Which sectors are most frequently targeted
- What attack types dominate the threat landscape
- How attack trends have evolved year over year
- What the financial and operational impact looks like

This intelligence supports **policy-making, security investments, and proactive defense strategies**.

---

## ❗ Problem Statement

Cyberattacks have grown increasingly frequent and sophisticated. Despite the availability of incident data, organizations often struggle to extract actionable insights due to the unstructured and fragmented nature of cyber reports.

Without a systematic analytical approach, businesses and policymakers face challenges in:

- Identifying the most targeted industry sectors
- Recognizing the most exploited attack vectors
- Detecting year-over-year attack trends
- Allocating security budgets effectively

This project addresses that gap by providing a structured, visual, and data-driven analysis of the global threat landscape.

---

## 📊 Dataset Description

| Attribute | Details |
|-----------|---------|
| **File** | `Global_Cybersecurity_Threats_2015-2024.csv` |
| **Time Period** | 2015 – 2024 (10 Years) |
| **Total Records** | 3,000 rows |
| **Total Features** | 10 columns |
| **Source** | PhishTank, CERT-In, Unit42, Kaggle, Verizon DBIR Reports |

### 🗂️ Column Reference

| Column | Description |
|--------|-------------|
| `Country` | Country where the incident occurred |
| `Year` | Year of the incident |
| `Attack Type` | Type of cyberattack (e.g., Phishing, Ransomware, DDoS) |
| `Target Industry` | Industry sector targeted (e.g., Healthcare, Banking, IT) |
| `Financial Loss (in Million $)` | Financial impact of the attack in USD millions |
| `Number of Affected Users` | Number of individuals impacted |
| `Attack Source` | Origin of the attack (Hacker Group, Nation-state, Insider, Unknown) |
| `Security Vulnerability Type` | Vulnerability exploited (e.g., Unpatched Software, Weak Passwords, Zero-day) |
| `Defense Mechanism Used` | Defense deployed (e.g., Firewall, VPN, AI-based Detection, Encryption) |
| `Incident Resolution Time (in Hours)` | Time taken to resolve the incident |

---

## 🛠️ Tech Stack

![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-Data%20Analysis-150458?logo=pandas)
![Matplotlib](https://img.shields.io/badge/Matplotlib-Visualization-orange)
![Seaborn](https://img.shields.io/badge/Seaborn-Statistical%20Plots-4C72B0)
![Jupyter](https://img.shields.io/badge/Jupyter-Notebook-F37626?logo=jupyter)

| Library | Purpose |
|---------|---------|
| `pandas` | Data loading, cleaning, manipulation |
| `matplotlib` | Bar charts, line charts, visualizations |
| `seaborn` | Heatmaps and statistical plots |
| `Jupyter Notebook` | Interactive analysis and presentation |

---

## 📁 Project Structure

```
📦 Global-Cybersecurity-Threats-Analysis
├── 📄 README.md                                  # Project documentation
├── 📓 Global_Cybersecurity_Threats_Analysis.ipynb  # Main Jupyter Notebook (EDA)
├── 🐍 data_analysis.py                           # Python analysis script
└── 📊 Global_Cybersecurity_Threats_2015-2024.csv # Dataset
```

---

## 🔬 Key Analyses Performed

### 1. 📋 Dataset Profiling
- Shape, data types, and column overview
- Missing value detection
- Duplicate record check
- Unique value counts per column

### 2. 📅 Temporal Analysis
- Year-wise incident distribution (2015–2024)
- Trend analysis of attack types over time

### 3. 🎯 Attack Type Analysis
- Top 6 most frequent attack types
- Average financial loss by attack type
- Year-over-year trend for top attack vectors

### 4. 🏭 Industry Sector Analysis
- Top 7 most targeted industries
- Heatmap: Frequency of attacks by sector and year
- Total attack count per industry (bar chart)

### 5. 🌐 Attack Source & Vulnerability Analysis
- Most common attack sources (Nation-state, Hacker Group, Insider, Unknown)
- Most exploited security vulnerabilities

### 6. 💰 Financial Impact Analysis
- Average financial loss ranked by attack type
- Comparative financial impact across sectors

---

## 📈 Visual Insights

The notebook generates the following visualizations:

| # | Chart | Description |
|---|-------|-------------|
| 1 | 📊 Bar Chart | Top 6 Attack Types by frequency |
| 2 | 📉 Line Chart | Top 6 Attack Types trend over time (2015–2024) |
| 3 | 🔥 Heatmap | Cyber attacks frequency by Sector × Year |
| 4 | 📊 Bar Chart | Total cyber attacks by Industry Sector |

---

## 💡 Key Findings

- **Phishing, Ransomware, and DDoS** consistently rank as the most frequent attack types across the decade.
- **Healthcare, Banking, and IT** are the most targeted industries, making them high-priority sectors for security investment.
- Financial losses vary significantly by attack type — **Ransomware** tends to inflict the highest average financial damage.
- **Hacker Groups and Nation-state actors** are the dominant attack sources, signaling an organized, often geopolitically motivated threat landscape.
- **Unpatched Software and Social Engineering** are the most exploited vulnerability types, highlighting the importance of patch management and employee training.
- Attack frequency shows a **rising trend from 2020 onward**, aligning with the global shift to remote work.

---

## ▶️ How to Run

### Prerequisites

Make sure you have Python 3.x installed along with the required libraries:

```bash
pip install pandas matplotlib seaborn notebook
```

### Option 1 — Run the Jupyter Notebook

```bash
# Clone the repository
git clone https://github.com/igpriyanshunegi/Global_Cybersecurity_Threats_Analysis.git
cd Global_Cybersecurity_Threats_Analysis

# Launch Jupyter
jupyter notebook Global_Cybersecurity_Threats_Analysis.ipynb
```

### Option 2 — Run the Python Script

```bash
python data_analysis.py
```

> ⚠️ Make sure `Global_Cybersecurity_Threats_2015-2024.csv` is in the **same directory** as the script/notebook before running.

---

## 👤 Author

**Priyanshu**
🔗 [GitHub Profile](https://github.com/igpriyanshunegi)
📁 [Project Repository](https://github.com/igpriyanshunegi/Global_Cybersecurity_Threats_Analysis)

---

> ⭐ *If you found this project helpful or insightful, consider giving it a star on GitHub!*
