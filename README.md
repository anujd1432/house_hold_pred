<div align="center">

<br/>

```
██╗███╗   ██╗ ██████╗ ██████╗ ███╗   ███╗███████╗    ██╗ ██████╗
██║████╗  ██║██╔════╝██╔═══██╗████╗ ████║██╔════╝    ██║██╔═══██╗
██║██╔██╗ ██║██║     ██║   ██║██╔████╔██║█████╗      ██║██║   ██║
██║██║╚██╗██║██║     ██║   ██║██║╚██╔╝██║██╔══╝      ██║██║▄▄ ██║
██║██║ ╚████║╚██████╗╚██████╔╝██║ ╚═╝ ██║███████╗    ██║╚██████╔╝
╚═╝╚═╝  ╚═══╝ ╚═════╝ ╚═════╝ ╚═╝     ╚═╝╚══════╝    ╚═╝ ╚══▀▀═╝
```

### ✦ AI-Powered Annual Income Predictor ✦

<br/>

[![Python](https://img.shields.io/badge/Python-3.10%2B-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.35+-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)](https://streamlit.io)
[![scikit-learn](https://img.shields.io/badge/scikit--learn-RandomForest-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white)](https://scikit-learn.org)
[![License](https://img.shields.io/badge/License-MIT-22c55e?style=for-the-badge)](LICENSE)
[![Status](https://img.shields.io/badge/Status-Live-6366f1?style=for-the-badge&logo=vercel&logoColor=white)]()

<br/>

> **IncomeIQ** uses a trained **Random Forest Regressor** to predict your annual income based on 15 demographic, professional, and lifestyle features — wrapped in a stunning dark-themed Streamlit UI.

<br/>
---
Live link-https://householdpred-gwb3xc5klpekw76u8janks.streamlit.app

---

</div>

<br/>

## 🖼️ Preview

<div align="center">

| Hero Section | Prediction Result |
|:---:|:---:|
| ![Hero](https://via.placeholder.com/520x280/050816/6366f1?text=IncomeIQ+Hero) | ![Result](https://via.placeholder.com/520x280/050816/c084fc?text=Prediction+Output) |

</div>

<br/>

---

## ✨ Features

<table>
<tr>
<td width="50%">

### 🤖 Machine Learning
- **Random Forest Regressor** — 15 engineered features
- **StandardScaler** normalization pipeline
- Engineered ratios: `income_per_age`, `experience_age_ratio`
- Predicts **annual**, **monthly**, and **daily** income

</td>
<td width="50%">

### 🎨 Beautiful UI
- Deep space dark theme (`#050816`)
- Animated gradient hero with glowing orbs
- Glassmorphism result cards
- Income tier badge (Entry → Executive)

</td>
</tr>
<tr>
<td>

### 📋 Smart Form
- 3 organized sections: Personal · Career · Lifestyle
- 9 select dropdowns + 6 numeric inputs
- One-click prediction with zero page reload
- Full profile summary after prediction

</td>
<td>

### ⚡ Performance
- Model cached with `@st.cache_resource`
- Instant predictions (< 50ms inference)
- Zero external API calls — fully local
- Lightweight deploy-ready structure

</td>
</tr>
</table>

<br/>

---

## 🧠 Model Details

```
Model Type   ─────  RandomForestRegressor (scikit-learn)
Preprocessor ─────  StandardScaler
Features     ─────  15 input variables
Output       ─────  Annual Income (USD, continuous regression)
```

### Input Features

| # | Feature | Type | Description |
|---|---------|------|-------------|
| 1 | `Age` | Numeric | Age in years (18–90) |
| 2 | `Education_Level` | Ordinal | High School → PhD (0–4) |
| 3 | `Occupation` | Categorical | 6 occupation categories |
| 4 | `Number_of_Dependents` | Numeric | Dependents count |
| 5 | `Location` | Categorical | Rural / Suburban / Urban |
| 6 | `Work_Experience` | Numeric | Years of experience |
| 7 | `Marital_Status` | Categorical | Single / Married / Divorced / Widowed |
| 8 | `Employment_Status` | Categorical | Full-Time / Part-Time / Self-Employed |
| 9 | `Household_Size` | Numeric | Number of household members |
| 10 | `Homeownership_Status` | Categorical | Renting / Mortgaged / Owned |
| 11 | `Type_of_Housing` | Categorical | Apartment → Villa |
| 12 | `Gender` | Categorical | Male / Female / Non-Binary |
| 13 | `Primary_Mode_of_Transportation` | Categorical | Car / Transit / Bike / Walk / Remote |
| 14 | `income_per_age` ⚙️ | Engineered | `age × 800` proxy signal |
| 15 | `Total_Experience_Age_Ratio` ⚙️ | Engineered | `work_experience / age` |

> ⚙️ = Engineered feature derived at inference time

### 🏅 Income Tiers

| Tier | Annual Range | Badge Color |
|------|-------------|------------|
| 🟢 Entry Level | < $40,000 | Emerald |
| 🔵 Mid Level | $40,000 – $79,999 | Blue |
| 🟣 Senior Level | $80,000 – $129,999 | Violet |
| 🩷 Executive | $130,000+ | Pink |

<br/>

---

## 🚀 Getting Started

### Prerequisites

```bash
Python >= 3.10
pip
```

### Installation

```bash
# 1. Clone the repo
git clone https://github.com/yourusername/incomeiq.git
cd incomeiq

# 2. Install dependencies
pip install -r requirements.txt

# 3. Run the app
streamlit run app.py
```

The app will open at `http://localhost:8501` 🎉

<br/>

---

## 📁 Project Structure

```
incomeiq/
│
├── app.py                  ← Streamlit UI (main entry point)
├── best_model.pkl          ← Trained RandomForestRegressor
├── scaler__2_.pkl          ← Fitted StandardScaler
├── features.pkl            ← Feature name list (15 features)
│
├── requirements.txt        ← Python dependencies
├── .gitignore
└── README.md               ← You are here
```

<br/>

---

## 📦 Requirements

```txt
streamlit>=1.35.0
scikit-learn>=1.6.0
numpy>=1.26.0
joblib>=1.4.0
```

Save as `requirements.txt` and run:

```bash
pip install -r requirements.txt
```

<br/>

---

## 🧑‍💻 Usage

1. **Launch** the app with `streamlit run app.py`
2. **Fill in** your personal, career, and lifestyle details
3. **Click** `✦ Predict My Income ✦`
4. **See** your estimated annual income, monthly breakdown, and income tier instantly

<br/>

---

## 🔬 How It Works

```
User Input (15 fields)
        │
        ▼
  Feature Engineering
  (income_per_age, exp_age_ratio)
        │
        ▼
  StandardScaler.transform()
        │
        ▼
  RandomForestRegressor.predict()
        │
        ▼
  Annual Income Estimate 💰
```

The model was trained on demographic and socioeconomic data. The two engineered features (`income_per_age` and `Total_Experience_Age_Ratio`) were critical signals — together they account for **~99.7%** of feature importance in the trained forest.

<br/>

---

## 🤝 Contributing

Contributions, issues and feature requests are welcome!

```bash
# Fork → Clone → Branch → PR
git checkout -b feature/your-feature-name
git commit -m "feat: add your feature"
git push origin feature/your-feature-name
```

Please follow the existing code style and add comments where necessary.

<br/>

---

## 📄 License

This project is licensed under the **MIT License** — see the [LICENSE](LICENSE) file for details.

<br/>

---

## 🙏 Acknowledgements

- [scikit-learn](https://scikit-learn.org) — Machine learning framework
- [Streamlit](https://streamlit.io) — Rapid ML app framework
- [Google Fonts](https://fonts.google.com) — Syne & DM Sans typefaces

<br/>

---

<div align="center">

Made with 💜 and Python

⭐ **Star this repo** if you found it useful!

<br/>

[![GitHub stars](https://img.shields.io/github/stars/yourusername/incomeiq?style=social)](https://github.com/yourusername/incomeiq)
[![GitHub forks](https://img.shields.io/github/forks/yourusername/incomeiq?style=social)](https://github.com/yourusername/incomeiq)

</div>
