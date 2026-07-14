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
        glucose_color = "success"
    elif 100 < client_glucose <= 125:
        glucose_level = "EARLY METABOLIC ELEVATION (Suboptimal Glycemic Baseline)"
        glucose_insight = f"Fasting glucose is elevated at {client_glucose} mg/dL, indicating early-stage insulin resistance. Prolonged extracellular glucose accelerates micro-vascular aging."
        glucose_control = "Initiate lifestyle modifications and carbohydrate control. Target re-establishing fasting baseline below 100 mg/dL under expert guidance."
        glucose_color = "warning"
    else:
        glucose_level = "CRITICAL METABOLIC ELEVATION (High Metabolic Risk)"
        glucose_insight = f"Fasting glucose is critically high at {client_glucose} mg/dL, triggering systemic protein glycation (AGEs) which structures vascular decline."
        glucose_control = "Urgent medical review recommended. Aggressively minimize overall glycemic load to re-establish homeostatic biological control."
        glucose_color = "error"

    # --- SECTION B: hs-CRP (INFLAMMATION) ---
    if client_hs_crp <= 1.0:
        crp_level = "OPTIMAL INFLAMMATORY STATUS (Low Cellular Aging)"
        crp_insight = f"Systemic inflammation is minimal at {client_hs_crp} mg/L, creating an ideal low-stress cellular environment that preserves long-term tissue youthfulness."
        crp_control = "Maintain an antioxidant-rich lifestyle pattern to protect mitochondrial health from chronic oxidative damage."
        crp_color = "success"
    elif 1.0 < client_hs_crp <= 3.0:
        crp_level = "MODERATE SYSTEMIC INFLAMMATION (Intermediate Aging Risk)"
        crp_insight = f"Inflammation is elevated at {client_hs_crp} mg/L, signaling low-grade chronic 'inflammaging' that slowly stresses cellular renewal pathways."
        crp_control = "Focus on eliminating industrial seed oils and environmental triggers. Optimize biological stress recovery protocols immediately."
        crp_color = "warning"
    else:
        crp_level = "CRITICAL SYSTEMIC INFLAMMATION (High Biological Aging Risk)"
        crp_insight = f"Inflammation is high at {client_hs_crp} mg/L. Chronic systemic stress at this tier accelerates the shortening of biological telomeres."
        crp_control = "Prioritize an aggressive clinical protocol to clear systemic physiological inflammation. Immediate healthcare collaboration is advised."
        crp_color = "error"

    # --- SECTION C: ALBUMIN (ORGAN VITALITY) ---
    if client_albumin > 3.5:
        albumin_level = "OPTIMAL ORGAN VITALITY & PROTEIN STATUS"
        albumin_insight = f"Serum albumin is strong at {client_albumin} g/dL, reflecting robust liver biosynthetic capacity and optimal systemic protein status."
        albumin_control = "Maintain adequate clean protein assimilation and gut health to support continued organ and tissue homeostasis."
        albumin_color = "success"
    else:
        albumin_level = "SUBOPTIMAL ORGAN VITALITY (Accelerated Decline Baseline)"
        albumin_insight = f"Serum albumin is low at {client_albumin} g/dL, signaling potential amino acid malabsorption, subclinical liver/kidney strain, or high metabolic stress."
        albumin_control = "Improve functional dietary protein intake and execute a comprehensive gut microbiome assessment to reverse systemic decline."
        albumin_color = "error"

    # --- DISPLAY ALL RESULTS ON SCREEN ---
    st.markdown("### 🩺 Clinical Biomarker & Longevity Analysis")
    
    # Glucose Display
    if glucose_color == "success": st.success(f"**Glucose Status:** {glucose_level}")
    elif glucose_color == "warning": st.warning(f"**Glucose Status:** {glucose_level}")
    else: st.error(f"**Glucose Status:** {glucose_level}")
    st.write(f"**Physiological Insight:** {glucose_insight}")
    st.write(f"**Actionable Control Protocol:** {glucose_control}")
    
    st.markdown("---")
    
    # hs-CRP Display
    if crp_color == "success": st.success(f"**Inflammation Status:** {crp_level}")
    elif crp_color == "warning": st.warning(f"**Inflammation Status:** {crp_level}")
    else: st.error(f"**Inflammation Status:** {crp_level}")
    st.write(f"**Physiological Insight:** {crp_insight}")
    st.write(f"**Actionable Control Protocol:** {crp_control}")
    
    st.markdown("---")

    # Albumin Display
    if albumin_color == "success": st.success(f"**Organ Vitality Status:** {albumin_level}")
    else: st.error(f"**Organ Vitality Status:** {albumin_level}")
    st.write(f"**Physiological Insight:** {albumin_insight}")
    st.write(f"**Actionable Control Protocol:** {albumin_control}")

    # Generating the downloadable custom report content
    report_content = (
        f"BIOLOGICAL AGE & LONGEVITY AUDIT REPORT\n"
        f"--------------------------------------\n"
        f"Patient Name: {patient_name if patient_name else 'Valued Client'}\n"
        f"Chronological Age: {client_age} Years Old\n"
        f"Calculated Biological Age: {final_bio_age} Years Old\n\n"
        f"1. METABOLIC STATE ANALYSIS\n"
        f"---------------------------\n"
        f"Fasting Glucose: {client_glucose} mg/dL\n"
        f"Classification: {glucose_level}\n"
        f"Insight: {glucose_insight}\n"
        f"Control Rule: {glucose_control}\n\n"
        f"2. INFLAMMATORY STATE ANALYSIS\n"
        f"------------------------------\n"
        f"Current hs-CRP: {client_hs_crp} mg/L\n"
        f"Classification: {crp_level}\n"
        f"Insight: {crp_insight}\n"
        f"Control Rule: {crp_control}\n\n"
        f"3. ORGAN VITALITY ANALYSIS\n"
        f"--------------------------\n"
        f"Serum Albumin: {client_albumin} g/dL\n"
        f"Classification: {albumin_level}\n"
        f"Insight: {albumin_insight}\n"
        f"Control Rule: {albumin_control}\n\n"
        f"IMPORTANT CLINICAL DISCLAIMER:\n"
        f"This automated digital analysis is for educational and wellness tracking purposes only. "
        f"It does not constitute a specific medical prescription or dietary plan. Always consult a physician."
    )
    
    st.markdown("---")
    st.subheader("📩 Download Official Client Report")
    st.download_button(
        label="Download Full Clinical Report PDF",
        data=report_content,
        file_name=f"{patient_name if patient_name else 'Client'}_Longevity_Report.txt",
        mime="text/plain"
    )
        
st.markdown("---")
st.caption("⚠️ DEMO VERSION ONLY - NOT FOR CLINICAL USE. This website is currently under development for an academic validation project. Do not input real medical patient records.")
