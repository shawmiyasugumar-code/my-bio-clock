import streamlit as st
import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestRegressor

# 1. Website Frontend Configuration
st.set_page_config(page_title="Longevity Bio-Clock", layout="centered")
st.title("🧬 Longevity & Anti-Aging Bio-Clock Analytics")
st.write("Welcome Dr. [Partner]. Enter your patient's biomarker data below to calculate biological age.")

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
patient_name = st.text_input("Patient Name", "Sithara")
client_age = st.number_input("Chronological Age (Passport Age)", min_value=1, max_value=120, value=69)
client_albumin = st.number_input("Albumin Level (g/dL)", min_value=1.0, max_value=10.0, value=4.2)
client_glucose = st.number_input("Fasting Glucose Level (mg/dL)", min_value=30.0, max_value=500.0, value=132.0)
client_hs_crp = st.number_input("C-Reactive Protein / hs-CRP (mg/L)", min_value=0.0, max_value=50.0, value=3.5)

# 4. Automated Report Generation Logic
if st.button("Generate Bio-Age Report"):
    new_client_data = pd.DataFrame([[client_albumin, client_glucose, client_hs_crp]], columns=['Albumin', 'Glucose', 'hs_CRP'])
    calculated_bio_age = ai_clock.predict(new_client_data)
    
    st.markdown("---")
    st.subheader(f"📊 Longevity Audit Report for {patient_name}")
    st.metric(label="Calculated Biological Age", value=f"{round(calculated_bio_age[0], 1)} Years Old")
    
    if client_glucose > 125:
        st.error("⚠️ Metabolic Status: Elevated / Diabetic Range")
        st.write("**Dietary Management Protocol (Based on ADA Guidelines):**")
        st.write("- **Breakfast:** Oatmeal, egg whites, or ragi idiyappam. Avoid white bread and sugary tea.")
        st.write("- **Lunch:** Small portion of red rice with heavy green vegetables and fish/chicken. Avoid potatoes.")
        st.write("- **Exercise:** 15-20 minutes of brisk walking immediately after meals.")
    else:
        st.success("✅ Metabolic Status: Normal Range")
        st.write("Maintain current healthy lifestyle and balanced diet.")
        
    st.markdown("---")
    st.caption("⚠️ DEMO VERSION ONLY - NOT FOR CLINICAL USE. This website is currently under development for an academic validation project. Do not input real medical patient records.")
