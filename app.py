import streamlit as st
import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestRegressor

# 1. Website Frontend Configuration
st.set_page_config(page_title="Longevity Bio-Clock", layout="centered")
st.title("🧬 Longevity & Anti-Aging Bio-Clock Analytics")
st.write("Welcome Dr. [Partner]. Enter biomarker data to analyze clinical risks and biological aging.")

# 2. AI Computational Engine Setup
@st.cache_resource
def train_ai_model():
    np.random.seed(42)
    n_samples = 1000
    chronological_age = np.random.uniform(20, 80, n_samples)
    albumin = 4.8 - (chronological_age * 0.015) + np.random.normal(0, 0.2, n_samples)
    glucose = 85 + (chronological_age * 0.4) + np.random.normal(0, 10, n_samples)
    hs_crp = 0.5 + (chronological_age * 0.04) + np.random.normal(0, 0.8, n_samples)

    dataset = pd.DataFrame({
        'Chronological_Age': chronological_age, 'Albumin': albumin,
        'Glucose': glucose, 'hs_CRP': hs_crp
    })
    X = dataset[['Albumin', 'Glucose', 'hs_CRP']]
    y = dataset['Chronological_Age']
    
    model = RandomForestRegressor(n_estimators=100, random_state=42)
    model.fit(X, y)
    return model

ai_clock = train_ai_model()

# 3. Clinical Data Input Fields
st.markdown("### 📋 Patient Biomarker Data Input")
patient_name = st.text_input("Patient Name", value="")
client_age = st.number_input("Chronological Age (Passport Age)", min_value=1, max_value=120, value=30)
client_albumin = st.number_input("Albumin Level (g/dL)", min_value=1.0, max_value=10.0, value=4.2)
client_glucose = st.number_input("Fasting Glucose Level (mg/dL)", min_value=30.0, max_value=500.0, value=90.0)
client_hs_crp = st.number_input("C-Reactive Protein / hs-CRP (mg/L)", min_value=0.0, max_value=50.0, value=0.8)

# 4. Automated Report Generation Logic
if st.button("Generate Bio-Age Report"):
    new_client_data = pd.DataFrame([[client_albumin, client_glucose, client_hs_crp]], columns=['Albumin', 'Glucose', 'hs_CRP'])
    calculated_bio_age = ai_clock.predict(new_client_data)
    final_bio_age = round(calculated_bio_age, 1)
    
    st.markdown("---")
    st.subheader(f"📊 Longevity Audit Report for {patient_name if patient_name else 'Valued Client'}")
    st.metric(label="Calculated Biological Age", value=f"{final_bio_age} Years Old")
    
    # --- SECTION A: FASTING GLUCOSE ---
    if client_glucose <= 100:
        glucose_level = "OPTIMAL METABOLIC HEALTH"
        glucose_insight = "Glycemic regulation is within the ideal longevity zone. Efficient cellular glucose uptake protects vascular endothelial integrity."
        glucose_control = "Maintain current metabolic baseline. Continue monitoring glycemic variance for long-term physiological stability."
        glucose_badge = "#2ecc71"
    elif 100 < client_glucose <= 125:
        glucose_level = "EARLY METABOLIC ELEVATION (Suboptimal Baseline)"
        glucose_insight = f"Fasting glucose is elevated at {client_glucose} mg/dL, indicating early-stage insulin resistance. Prolonged extracellular glucose accelerates micro-vascular aging."
        glucose_control = "Initiate lifestyle modifications and carbohydrate control. Target re-establishing fasting baseline below 100 mg/dL under expert guidance."
        glucose_badge = "#f39c12"
    else:
        glucose_level = "CRITICAL METABOLIC ELEVATION (High Metabolic Risk)"
        glucose_insight = f"Fasting glucose is critically high at {client_glucose} mg/dL, triggering systemic protein glycation (AGEs) which structures vascular decline."
        glucose_control = "Urgent medical review recommended. Aggressively minimize overall glycemic load to re-establish homeostatic biological control."
        glucose_badge = "#e74c3c"

    # --- SECTION B: hs-CRP (INFLAMMATION) ---
    if client_hs_crp <= 1.0:
        crp_level = "OPTIMAL INFLAMMATORY STATUS (Low Cellular Aging)"
        crp_insight = f"Systemic inflammation is minimal at {client_hs_crp} mg/L, creating an ideal low-stress cellular environment that preserves long-term tissue youthfulness."
        crp_control = "Maintain an antioxidant-rich lifestyle pattern to protect mitochondrial health from chronic oxidative damage."
        crp_badge = "#2ecc71"
    elif 1.0 < client_hs_crp <= 3.0:
        crp_level = "MODERATE SYSTEMIC INFLAMMATION (Intermediate Aging Risk)"
        crp_insight = f"Inflammation is elevated at {client_hs_crp} mg/L, signaling low-grade chronic 'inflammaging' that slowly stresses cellular renewal pathways."
        crp_control = "Focus on eliminating industrial seed oils and environmental triggers. Optimize biological stress recovery protocols immediately."
        crp_badge = "#f39c12"
    else:
        crp_level = "CRITICAL SYSTEMIC INFLAMMATION (High Biological Aging Risk)"
        crp_insight = f"Inflammation is high at {client_hs_crp} mg/L. Chronic systemic stress at this tier accelerates the shortening of biological telomeres."
        crp_control = "Prioritize an aggressive clinical protocol to clear systemic physiological inflammation. Immediate healthcare collaboration is advised."
        crp_badge = "#e74c3c"

    # --- SECTION C: ALBUMIN (ORGAN VITALITY) ---
    if client_albumin > 3.5:
        albumin_level = "OPTIMAL ORGAN VITALITY & PROTEIN STATUS"
        albumin_insight = f"Serum albumin is strong at {client_albumin} g/dL, reflecting robust liver biosynthetic capacity and optimal systemic protein status."
        albumin_control = "Maintain adequate clean protein assimilation and gut health to support continued organ and tissue homeostasis."
        albumin_badge = "#2ecc71"
    else:
        albumin_level = "SUBOPTIMAL ORGAN VITALITY (Accelerated Decline Baseline)"
        albumin_insight = f"Serum albumin is low at {client_albumin} g/dL, signaling potential amino acid malabsorption, subclinical liver/kidney strain, or high metabolic stress."
        albumin_control = "Improve functional dietary protein intake and execute a comprehensive gut microbiome assessment to reverse systemic decline."
        albumin_badge = "#e74c3c"

    # --- DISPLAY ALL RESULTS ON WEB SCREEN ---
    st.markdown("### 🩺 Clinical Biomarker & Longevity Analysis")
    if glucose_badge == "#2ecc71": st.success(f"**Glucose Status:** {glucose_level}")
    elif glucose_badge == "#f39c12": st.warning(f"**Glucose Status:** {glucose_level}")
    else: st.error(f"**Glucose Status:** {glucose_level}")
    st.write(f"**Physiological Insight:** {glucose_insight}")
    st.write(f"**Actionable Control Protocol:** {glucose_control}")
    st.markdown("---")
    
    if crp_badge == "#2ecc71": st.success(f"**Inflammation Status:** {crp_level}")
    elif crp_badge == "#f39c12": st.warning(f"**Inflammation Status:** {crp_level}")
    else: st.error(f"**Inflammation Status:** {crp_level}")
    st.write(f"**Physiological Insight:** {crp_insight}")
    st.write(f"**Actionable Control Protocol:** {crp_control}")
    st.markdown("---")

    if albumin_badge == "#2ecc71": st.success(f"**Organ Vitality Status:** {albumin_level}")
    else: st.error(f"**Organ Vitality Status:** {albumin_level}")
    st.write(f"**Physiological Insight:** {albumin_insight}")
    st.write(f"**Actionable Control Protocol:** {albumin_control}")

    # --- GENERATING BEAUTIFUL COLOURFUL PDF REPORT ---
    display_name = patient_name if patient_name else 'Valued Client'
    
    html_report = (
        "<html><head><style>"
        "body { font-family: Arial, sans-serif; background-color: #0a192f; color: #ffffff; padding: 30px; }"
        ".header { text-align: center; border-bottom: 2px solid #c5a059; padding-bottom: 15px; margin-bottom: 25px; }"
        ".title { color: #c5a059; font-size: 26px; font-weight: bold; }"
        ".meta-info { font-size: 15px; margin-top: 10px; color: #8892b0; }"
        ".metric-box { background-color: #112240; border-radius: 6px; padding: 15px; margin-bottom: 20px; border-left: 5px solid #c5a059; }"
        ".section-title { font-size: 18px; color: #c5a059; margin-bottom: 8px; font-weight: bold; }"
        ".badge { display: inline-block; padding: 4px 10px; border-radius: 4px; font-size: 13px; font-weight: bold; color: #ffffff; margin-bottom: 8px; }"
        ".insight { font-size: 14px; color: #e2e8f0; margin-bottom: 8px; }"
        ".protocol { font-size: 14px; color: #64ffda; font-style: italic; }"
        ".disclaimer { font-size: 11px; color: #8892b0; text-align: justify; margin-top: 35px; border-top: 1px solid #233554; padding-top: 12px; }"
        "</style></head><body>"
        "<div class='header'>"
        "<div class='title'>BIOLOGICAL AGE & LONGEVITY AUDIT</div>"
        f"<div class='meta-info'><strong>Patient Name:</strong> {display_name} &nbsp;|&nbsp; <strong>Chronological Age:</strong> {client_age} Years &nbsp;|&nbsp; <strong>Calculated Biological Age:</strong> {final_bio_age} Years</div>"
        "</div>"
        "<div class='metric-box'>"
        "<div class='section-title'>1. METABOLIC ANALYSIS (Fasting Glucose)</div>"
        f"<span class='badge' style='background-color: {glucose_badge};'>{glucose_level}</span>"
        f"<div class='insight'><strong>Physiological Insight:</strong> {glucose_insight}</div>"
        f"<div class='protocol'><strong>Actionable Control Protocol:</strong> {glucose_control}</div>"
        "</div>"
        "<div class='metric-box'>"
        "<div class='section-title'>2. INFLAMMATORY ANALYSIS (hs-CRP)</div>"
        f"<span class='badge' style='background-color: {crp_badge};'>{crp_level}</span>"
        f"<div class='insight'><strong>Physiological Insight:</strong> {crp_insight}</div>"
        f"<div class='protocol'><strong>Actionable Control Protocol:</strong> {crp_control}</div>"
        "</div>"
        "<div class='metric-box'>"
        "<div class='section-title'>3. ORGAN VITALITY ANALYSIS (Serum Albumin)</div>"
        f"<span class='badge' style='background-color: {albumin_badge};'>{albumin_level}</span>"
