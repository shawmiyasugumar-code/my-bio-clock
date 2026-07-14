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
client_albumin = st.number_input("Albumin Level (g/dL)", min_value=1.0, max_value=10.0, value=4.0)
client_glucose = st.number_input("Fasting Glucose Level (mg/dL)", min_value=30.0, max_value=500.0, value=90.0)
client_hs_crp = st.number_input("C-Reactive Protein / hs-CRP (mg/L)", min_value=0.0, max_value=50.0, value=1.0)

# 4. Automated Report Generation Logic
if st.button("Generate Bio-Age Report"):
    new_client_data = pd.DataFrame([[client_albumin, client_glucose, client_hs_crp]], columns=['Albumin', 'Glucose', 'hs_CRP'])
    calculated_bio_age = ai_clock.predict(new_client_data)
    final_bio_age = round(calculated_bio_age, 1)
    
    st.markdown("---")
    st.subheader(f"📊 Longevity Audit Report for {patient_name if patient_name else 'Valued Client'}")
    st.metric(label="Calculated Biological Age", value=f"{final_bio_age} Years Old")
    
    # Smart Dynamic Logic for Fasting Glucose (No Food Names, Only Clinical Control)
    if client_glucose <= 100:
        status_level = "OPTIMAL METABOLIC HEALTH baseline"
        clinical_insight = "Your glycemic regulation is within the ideal longevity zone. Cellular glucose uptake is efficient, preventing advanced glycation end-products (AGEs) and protecting vascular endothelial integrity."
        control_protocol = "Maintain your current metabolic baseline. Keep monitoring glycemic variance to ensure long-term stability and minimal cellular aging stress."
        status_color = "success"
    elif 100 < client_glucose <= 125:
        status_level = "EARLY METABOLIC ELEVATION (Suboptimal Glycemic Baseline)"
        clinical_insight = f"Fasting glucose is elevated at {client_glucose} mg/dL. This implies early-stage peripheral insulin resistance. Glucose remains in extracellular spaces longer, causing minor vascular stiffening and accelerated micro-vascular decline."
        control_protocol = "Initiate immediate carbohydrate restriction and caloric control. Work with your registered nutritionist or doctor to implement a low-glycemic dietary framework aimed at pulling fasting glucose below 100 mg/dL."
        status_color = "warning"
    else:
        status_level = "CRITICAL METABOLIC ELEVATION (High Metabolic Risk)"
        clinical_insight = f"Fasting glucose is critically high at {client_glucose} mg/dL. This chronic level triggers systemic protein glycation. This process literal modifies tissue structures, damaging renal filtration pathways, retinal health, and cardiovascular systems."
        control_protocol = "Urgent clinical intervention is recommended. Consult your physician immediately for medical management. Aggressively eliminate refined carbohydrates and reduce glycemic load to re-establish homeostatic control."
        status_color = "error"

    # Displaying the Smart Personalized Advice on the screen
    st.markdown("### 🩺 Clinical Metabolism & Longevity Analysis")
    if status_color == "success": st.success(f"**Status:** {status_level}")
    elif status_color == "warning": st.warning(f"**Status:** {status_level}")
    else: st.error(f"**Status:** {status_level}")
        
    st.write(f"**Physiological Insight:** {clinical_insight}")
    st.write(f"**Actionable Control Protocol:** {control_protocol}")
    st.write("- **Post-Meal Movement Rule:** Execute 15-20 minutes of light movement or walking immediately after major caloric intakes to utilize skeletal muscles as a direct glucose sink.")

    # Generating the downloadable custom report content
    report_content = (
        f"BIOLOGICAL AGE & LONGEVITY AUDIT REPORT\n"
        f"--------------------------------------\n"
        f"Patient Name: {patient_name if patient_name else 'Valued Client'}\n"
        f"Chronological Age: {client_age} Years Old\n"
        f"Calculated Biological Age: {final_bio_age} Years Old\n\n"
        f"METABOLIC STATE ANALYSIS FOR {patient_name.upper() if patient_name else 'CLIENT'}\n"
        f"---------------------------------------------\n"
        f"Current Fasting Glucose: {client_glucose} mg/dL\n"
        f"Classification: {status_level}\n\n"
        f"Physiological Insight:\n{clinical_insight}\n\n"
        f"Actionable Control Protocol:\n{control_protocol}\n"
        f"- Execute 15-20 minutes of light physical movement immediately after major meals to clear glucose spikes.\n\n"
        f"IMPORTANT CLINICAL DISCLAIMER:\n"
        f"This automated digital analysis is for educational and wellness tracking purposes only. "
        f"It does not contain or constitute a medical prescription or specific dietary menu. Always consult your practicing healthcare provider before making lifestyle modifications."
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
