import streamlit as st
import joblib
import numpy as np
import warnings
warnings.filterwarnings('ignore')

# ─── Page Config ─────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="IncomeIQ · Salary Predictor",
    page_icon="💎",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ─── Load Model ──────────────────────────────────────────────────────────────
@st.cache_resource
def load_model():
    model  = joblib.load("best_model.pkl")
    scaler = joblib.load("scaler (2).pkl")
    return model, scaler

model, scaler = load_model()

# ─── Global CSS ──────────────────────────────────────────────────────────────
st.markdown("""
<style>
  @import url('https://fonts.googleapis.com/css2?family=Syne:wght@400;600;700;800&family=DM+Sans:ital,wght@0,300;0,400;0,500;1,300&display=swap');

  /* ── Reset ── */
  *, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }

  html, body, [data-testid="stAppViewContainer"], [data-testid="stMain"] {
    background: #050816 !important;
    font-family: 'DM Sans', sans-serif;
    color: #e2e8f0;
  }

  [data-testid="stHeader"] { background: transparent !important; }
  [data-testid="stSidebar"] { display: none; }
  .block-container { padding: 0 !important; max-width: 100% !important; }

  /* ── Scrollbar ── */
  ::-webkit-scrollbar { width: 6px; }
  ::-webkit-scrollbar-track { background: #0a0f1e; }
  ::-webkit-scrollbar-thumb { background: #334155; border-radius: 99px; }

  /* ── Hide Streamlit chrome ── */
  #MainMenu, footer, [data-testid="stToolbar"] { display: none !important; }

  /* ── Select boxes & number inputs ── */
  [data-testid="stSelectbox"] > div > div,
  [data-testid="stNumberInput"] input {
    background: rgba(15,23,42,0.8) !important;
    border: 1px solid rgba(99,102,241,.35) !important;
    border-radius: 12px !important;
    color: #e2e8f0 !important;
    font-family: 'DM Sans', sans-serif !important;
    transition: border .25s, box-shadow .25s;
  }
  [data-testid="stSelectbox"] > div > div:hover,
  [data-testid="stNumberInput"] input:focus {
    border-color: #818cf8 !important;
    box-shadow: 0 0 0 3px rgba(99,102,241,.18) !important;
  }
  [data-testid="stSelectbox"] svg { color: #818cf8 !important; }

  /* dropdown options */
  [data-testid="stSelectboxVirtualDropdown"] {
    background: #0f172a !important;
    border: 1px solid #334155 !important;
    border-radius: 12px !important;
  }

  /* ── Labels ── */
  label[data-testid="stWidgetLabel"] p {
    color: #94a3b8 !important;
    font-size: .78rem !important;
    font-weight: 500 !important;
    letter-spacing: .06em !important;
    text-transform: uppercase !important;
    margin-bottom: 4px !important;
  }

  /* ── Predict button ── */
  [data-testid="stFormSubmitButton"] button,
  .stButton button {
    width: 100%;
    padding: 1rem 2rem !important;
    font-family: 'Syne', sans-serif !important;
    font-size: 1.05rem !important;
    font-weight: 700 !important;
    letter-spacing: .05em !important;
    color: #fff !important;
    background: linear-gradient(135deg, #6366f1 0%, #8b5cf6 50%, #ec4899 100%) !important;
    border: none !important;
    border-radius: 14px !important;
    cursor: pointer;
    transition: opacity .2s, transform .15s, box-shadow .2s !important;
    box-shadow: 0 4px 24px rgba(99,102,241,.45) !important;
  }
  [data-testid="stFormSubmitButton"] button:hover,
  .stButton button:hover {
    opacity: .92 !important;
    transform: translateY(-2px) !important;
    box-shadow: 0 8px 32px rgba(99,102,241,.6) !important;
  }
  [data-testid="stFormSubmitButton"] button:active,
  .stButton button:active {
    transform: translateY(0) !important;
  }

  /* ── Metric overrides ── */
  [data-testid="stMetricValue"] {
    font-family: 'Syne', sans-serif !important;
    font-size: 2.8rem !important;
    font-weight: 800 !important;
    background: linear-gradient(135deg, #a5b4fc, #f0abfc);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
  }
  [data-testid="stMetricLabel"] { color: #64748b !important; font-size: .8rem !important; }

  /* ── Spinner ── */
  [data-testid="stSpinner"] { color: #818cf8 !important; }
</style>
""", unsafe_allow_html=True)

# ─── Hero Header ─────────────────────────────────────────────────────────────
st.markdown("""
<div style="
  position: relative;
  overflow: hidden;
  background: linear-gradient(135deg, #0f0c29 0%, #130f40 40%, #0d0d2b 100%);
  padding: 3.5rem 3rem 3rem;
  border-bottom: 1px solid rgba(99,102,241,.18);
">
  <!-- Decorative blobs -->
  <div style="
    position:absolute; top:-80px; right:-60px;
    width:380px; height:380px; border-radius:50%;
    background: radial-gradient(circle, rgba(139,92,246,.25) 0%, transparent 70%);
    filter: blur(40px); pointer-events:none;
  "></div>
  <div style="
    position:absolute; bottom:-100px; left:5%;
    width:300px; height:300px; border-radius:50%;
    background: radial-gradient(circle, rgba(236,72,153,.15) 0%, transparent 70%);
    filter: blur(50px); pointer-events:none;
  "></div>

  <!-- Badge -->
  <div style="display:flex; align-items:center; gap:.6rem; margin-bottom:1.2rem;">
    <div style="
      display:inline-flex; align-items:center; gap:.5rem;
      background: rgba(99,102,241,.12); border:1px solid rgba(99,102,241,.3);
      border-radius:99px; padding:.28rem .9rem;
      font-size:.72rem; font-weight:600; color:#a5b4fc; letter-spacing:.08em;
      text-transform:uppercase;
    ">
      <span style="width:6px;height:6px;border-radius:50%;background:#6366f1;
        box-shadow:0 0 8px #6366f1; display:inline-block; animation:pulse 2s infinite;"></span>
      AI Powered · Random Forest Model
    </div>
  </div>

  <!-- Title -->
  <h1 style="
    font-family:'Syne',sans-serif; font-size:clamp(2.2rem,5vw,3.6rem);
    font-weight:800; line-height:1.1; color:#fff; margin-bottom:.7rem;
  ">
    Income<span style="
      background: linear-gradient(90deg,#818cf8,#c084fc,#f472b6);
      -webkit-background-clip:text; -webkit-text-fill-color:transparent;
      background-clip:text;
    ">IQ</span>
  </h1>
  <p style="
    font-size:1.05rem; color:#94a3b8; max-width:520px; line-height:1.65;
    font-weight:300;
  ">
    Enter your personal &amp; professional details below.<br>
    Our trained <strong style="color:#c4b5fd; font-weight:500;">Random Forest</strong>
    model will estimate your annual income instantly.
  </p>

  <style>
    @keyframes pulse {
      0%,100%{opacity:1; transform:scale(1);}
      50%{opacity:.6; transform:scale(1.4);}
    }
  </style>
</div>
""", unsafe_allow_html=True)

# ─── Mapping helpers ─────────────────────────────────────────────────────────
EDU_MAP = {
    "High School":         0,
    "Associate's Degree":  1,
    "Bachelor's Degree":   2,
    "Master's Degree":     3,
    "PhD":                 4,
}
OCC_MAP = {
    "Unemployed":          0,
    "Student":             1,
    "Blue-Collar":         2,
    "White-Collar":        3,
    "Self-Employed":       4,
    "Professional":        5,
}
LOC_MAP = {"Rural": 0, "Suburban": 1, "Urban": 2}
MAR_MAP = {"Single": 0, "Married": 1, "Divorced": 2, "Widowed": 3}
EMP_MAP = {"Unemployed": 0, "Part-Time": 1, "Full-Time": 2, "Self-Employed": 3}
HOM_MAP = {"Renting": 0, "Mortgaged": 1, "Owned": 2}
HOU_MAP = {"Apartment": 0, "Condo": 1, "Townhouse": 2, "Single-Family Home": 3, "Villa": 4}
GEN_MAP = {"Male": 0, "Female": 1, "Non-Binary": 2}
TRA_MAP = {"Public Transit": 0, "Bike": 1, "Car": 2, "Walk": 3, "Remote": 4}

# ─── Form ────────────────────────────────────────────────────────────────────
st.markdown("<div style='padding:2.5rem 3rem 3rem; max-width:1400px; margin:0 auto;'>", unsafe_allow_html=True)

# Section title helper
def section_title(icon, text, sub):
    st.markdown(f"""
    <div style="display:flex;align-items:center;gap:.75rem;margin:2.2rem 0 1.2rem;">
      <div style="
        width:36px;height:36px;border-radius:10px;
        background:rgba(99,102,241,.15);border:1px solid rgba(99,102,241,.3);
        display:flex;align-items:center;justify-content:center;font-size:1rem;
      ">{icon}</div>
      <div>
        <div style="font-family:'Syne',sans-serif;font-weight:700;color:#e2e8f0;font-size:1.05rem;">{text}</div>
        <div style="font-size:.75rem;color:#64748b;">{sub}</div>
      </div>
    </div>
    """, unsafe_allow_html=True)

with st.form("prediction_form"):

    # ── Section 1: Personal ──────────────────────────────────────────────────
    section_title("👤", "Personal Information", "Demographics & background")
    c1, c2, c3, c4 = st.columns(4)
    with c1:
        age = st.number_input("Age", min_value=18, max_value=90, value=30, step=1)
    with c2:
        gender = st.selectbox("Gender", list(GEN_MAP.keys()))
    with c3:
        marital = st.selectbox("Marital Status", list(MAR_MAP.keys()))
    with c4:
        dependents = st.number_input("Number of Dependents", min_value=0, max_value=15, value=1, step=1)

    # ── Section 2: Education & Career ───────────────────────────────────────
    section_title("🎓", "Education & Career", "Your professional profile")
    c5, c6, c7, c8 = st.columns(4)
    with c5:
        education = st.selectbox("Education Level", list(EDU_MAP.keys()))
    with c6:
        occupation = st.selectbox("Occupation", list(OCC_MAP.keys()))
    with c7:
        employment = st.selectbox("Employment Status", list(EMP_MAP.keys()))
    with c8:
        work_exp = st.number_input("Work Experience (years)", min_value=0, max_value=50, value=5, step=1)

    # ── Section 3: Lifestyle ─────────────────────────────────────────────────
    section_title("🏡", "Lifestyle & Housing", "Where and how you live")
    c9, c10, c11, c12, c13 = st.columns(5)
    with c9:
        location = st.selectbox("Location Type", list(LOC_MAP.keys()))
    with c10:
        homeownership = st.selectbox("Homeownership", list(HOM_MAP.keys()))
    with c11:
        housing_type = st.selectbox("Type of Housing", list(HOU_MAP.keys()))
    with c12:
        household = st.number_input("Household Size", min_value=1, max_value=15, value=3, step=1)
    with c13:
        transport = st.selectbox("Primary Transport", list(TRA_MAP.keys()))

    # ── Submit ───────────────────────────────────────────────────────────────
    st.markdown("<div style='height:1.5rem'></div>", unsafe_allow_html=True)
    submitted = st.form_submit_button("✦  Predict My Income  ✦")

# ─── Prediction ──────────────────────────────────────────────────────────────
if submitted:
    income_per_age     = age * 800  # reasonable proxy
    exp_age_ratio      = work_exp / max(age, 1)

    X_raw = np.array([[
        age,
        EDU_MAP[education],
        OCC_MAP[occupation],
        dependents,
        LOC_MAP[location],
        work_exp,
        MAR_MAP[marital],
        EMP_MAP[employment],
        household,
        HOM_MAP[homeownership],
        HOU_MAP[housing_type],
        GEN_MAP[gender],
        TRA_MAP[transport],
        income_per_age,
        exp_age_ratio,
    ]])

    X_scaled = scaler.transform(X_raw)
    prediction = model.predict(X_scaled)[0]

    monthly = prediction / 12
    daily   = prediction / 365

    # ── Result banner ────────────────────────────────────────────────────────
    tier_label, tier_color, tier_bg = (
        ("Entry Level",  "#34d399", "rgba(52,211,153,.1)")  if prediction < 40000 else
        ("Mid Level",    "#60a5fa", "rgba(96,165,250,.1)")  if prediction < 80000 else
        ("Senior Level", "#c084fc", "rgba(192,132,252,.1)") if prediction < 130000 else
        ("Executive",    "#f472b6", "rgba(244,114,182,.1)")
    )

    st.markdown(f"""
    <div style="
      margin-top:2.5rem;
      background: linear-gradient(135deg,rgba(15,23,42,.9) 0%,rgba(20,10,50,.9) 100%);
      border:1px solid rgba(99,102,241,.3);
      border-radius:24px;
      padding:2.5rem 2.8rem;
      position:relative; overflow:hidden;
    ">
      <!-- Glow -->
      <div style="
        position:absolute;top:-60px;right:-40px;width:300px;height:300px;border-radius:50%;
        background:radial-gradient(circle,rgba(139,92,246,.2) 0%,transparent 70%);
        filter:blur(40px);pointer-events:none;
      "></div>

      <div style="display:flex;align-items:center;gap:.7rem;margin-bottom:1.8rem;">
        <div style="
          background:{tier_bg}; border:1px solid {tier_color}40;
          color:{tier_color}; border-radius:99px; padding:.3rem 1rem;
          font-size:.75rem;font-weight:600;letter-spacing:.07em;text-transform:uppercase;
        ">⬡ {tier_label}</div>
        <div style="color:#475569;font-size:.8rem;">Based on your profile</div>
      </div>

      <div style="font-family:'Syne',sans-serif;font-size:.8rem;color:#64748b;
        letter-spacing:.1em;text-transform:uppercase;margin-bottom:.4rem;">
        Predicted Annual Income
      </div>
      <div style="
        font-family:'Syne',sans-serif;
        font-size:clamp(2.8rem,7vw,5rem);font-weight:800;line-height:1;
        background:linear-gradient(135deg,#a5b4fc 0%,#c084fc 50%,#f0abfc 100%);
        -webkit-background-clip:text;-webkit-text-fill-color:transparent;background-clip:text;
        margin-bottom:1.8rem;
      ">
        ${prediction:,.0f}
        <span style="font-size:1.5rem;opacity:.6;"> / yr</span>
      </div>

      <div style="display:grid;grid-template-columns:repeat(3,1fr);gap:1rem;max-width:560px;">
        <div style="background:rgba(255,255,255,.04);border:1px solid rgba(255,255,255,.07);
          border-radius:14px;padding:1rem 1.2rem;">
          <div style="font-size:.7rem;color:#64748b;text-transform:uppercase;letter-spacing:.07em;margin-bottom:.3rem;">Monthly</div>
          <div style="font-family:'Syne',sans-serif;font-weight:700;color:#e2e8f0;font-size:1.25rem;">
            ${monthly:,.0f}
          </div>
        </div>
        <div style="background:rgba(255,255,255,.04);border:1px solid rgba(255,255,255,.07);
          border-radius:14px;padding:1rem 1.2rem;">
          <div style="font-size:.7rem;color:#64748b;text-transform:uppercase;letter-spacing:.07em;margin-bottom:.3rem;">Daily</div>
          <div style="font-family:'Syne',sans-serif;font-weight:700;color:#e2e8f0;font-size:1.25rem;">
            ${daily:,.0f}
          </div>
        </div>
        <div style="background:rgba(255,255,255,.04);border:1px solid rgba(255,255,255,.07);
          border-radius:14px;padding:1rem 1.2rem;">
          <div style="font-size:.7rem;color:#64748b;text-transform:uppercase;letter-spacing:.07em;margin-bottom:.3rem;">Experience</div>
          <div style="font-family:'Syne',sans-serif;font-weight:700;color:#e2e8f0;font-size:1.25rem;">
            {work_exp} yrs
          </div>
        </div>
      </div>
    </div>
    """, unsafe_allow_html=True)

    # ── Profile summary ───────────────────────────────────────────────────────
    st.markdown("""<div style="height:1.5rem"></div>""", unsafe_allow_html=True)

    st.markdown("""
    <div style="font-family:'Syne',sans-serif;font-size:.78rem;color:#475569;
      text-transform:uppercase;letter-spacing:.09em;margin-bottom:.8rem;">
      Profile Summary
    </div>""", unsafe_allow_html=True)

    items = [
        ("🎂", "Age", f"{age} years"),
        ("🎓", "Education", education),
        ("💼", "Occupation", occupation),
        ("📍", "Location", location),
        ("🏠", "Housing", f"{homeownership} · {housing_type}"),
        ("👥", "Household", f"{household} members"),
    ]
    cols = st.columns(6)
    for col, (icon, label, val) in zip(cols, items):
        col.markdown(f"""
        <div style="background:rgba(255,255,255,.03);border:1px solid rgba(255,255,255,.07);
          border-radius:14px;padding:1rem;text-align:center;">
          <div style="font-size:1.4rem;margin-bottom:.4rem;">{icon}</div>
          <div style="font-size:.65rem;color:#64748b;text-transform:uppercase;
            letter-spacing:.07em;margin-bottom:.2rem;">{label}</div>
          <div style="font-size:.85rem;font-weight:500;color:#cbd5e1;">{val}</div>
        </div>""", unsafe_allow_html=True)

# ─── Footer ──────────────────────────────────────────────────────────────────
st.markdown("""
<div style="
  margin-top:4rem;padding:2rem 3rem;
  border-top:1px solid rgba(255,255,255,.05);
  display:flex;align-items:center;justify-content:space-between;flex-wrap:wrap;gap:1rem;
">
  <div style="font-family:'Syne',sans-serif;font-weight:700;color:#334155;font-size:.95rem;">
    Income<span style="color:#6366f1;">IQ</span>
  </div>
  <div style="font-size:.75rem;color:#334155;">
    Predictions are estimates based on historical data. Not financial advice.
  </div>
</div>
""", unsafe_allow_html=True)

st.markdown("</div>", unsafe_allow_html=True)

