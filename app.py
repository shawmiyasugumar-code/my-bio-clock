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
    
    # FIXED: Added [0] to extract the single number from the array before rounding
    final_bio_age = round(calculated_bio_age[0], 1)
    
    st.markdown("---")
    st.subheader(f"📊 Longevity Audit Report for {patient_name}")
    st.metric(label="Calculated Biological Age", value=f"{final_bio_age} Years Old")
    
    # Smart Dynamic Logic for Fasting Glucose
    if client_glucose <= 100:
        status_level = "OPTIMAL METABOLIC HEALTH"
        urgency_note = "Your blood sugar regulation is excellent. Your pancreas and cellular insulin receptors are functioning efficiently, protecting your blood vessels from premature aging."
        diet_intensity = "Continue with your current dietary pattern. Focus on whole-grain carbohydrates and complex fibers to maintain this healthy baseline."
        status_color = "success"
    elif 100 < client_glucose <= 125:
        status_level = "EARLY METABOLIC ELEVATION (Pre-Diabetic Range)"
        urgency_note = f"Your fasting glucose is currently at {client_glucose} mg/dL. Your cells are exhibiting early signs of insulin resistance. This means glucose stays in your bloodstream longer, which accelerates cellular decline and blood vessel stiffening. Immediate lifestyle intervention can fully reverse this trajectory."
        diet_intensity = "Adopt a low-glycemic Mediterranean dietary framework. Shift away from processed carbs. Reduce your daily intake of white rice or white bread by 50% and replace them with high-fiber whole grains like oats or quinoa."
        status_color = "warning"
    else:
        status_level = "CRITICAL METABOLIC ELEVATION (Diabetic Range)"
        urgency_note = f"Your fasting glucose is significantly high at {client_glucose} mg/dL. This prolonged high sugar level triggers Advanced Glycation End-products (AGEs). AGEs literally caramelize your proteins and structural tissues, rapidly damaging your kidneys, eyes, and cardiovascular system, forcing your biological age upward."
        diet_intensity = "Initiate aggressive dietary modifications immediately. Eliminate all added sugars, sodas, and processed flour products. Transition your meals entirely to clean, lean proteins (egg whites, chicken breast, fish) and non-starchy green vegetables."
        status_color = "error"

    # Displaying the Smart Personalized Advice on the screen
    st.markdown("### 🩺 Clinical Metabolism & Longevity Analysis")
    if status_color == "success":
        st.success(f"**Status:** {status_level}")
    elif status_color == "warning":
        st.warning(f"**Status:** {status_level}")
    else:
        st.error(f"**Status:** {status_level}")
        
    st.write(f"**Physiological Insight:** {urgency_note}")
    st.write(f"**Actionable Nutrition Protocol:** {diet_intensity}")
    st.write("- **Physical Movement Rule:** Execute a 15-to-20-minute brisk walk immediately after your largest meals. This triggers your skeletal muscles to clear excess glucose directly from your blood without requiring extra insulin.")

    # Generating the downloadable custom report content
    report_content = (
        f"BIOLOGICAL AGE & LONGEVITY AUDIT REPORT\n"
        f"--------------------------------------\n"
        f"Patient Name: {patient_name}\n"
        f"Chronological Age: {client_age} Years Old\n"
        f"Calculated Biological Age: {final_bio_age} Years Old\n\n"
        f"METABOLIC STATE ANALYSIS FOR {patient_name.upper()}\n"
        f"---------------------------------------------\n"
        f"Current Fasting Glucose: {client_glucose} mg/dL\n"
        f"Metabolic Classification: {status_level}\n\n"
        f"Physiological Insight:\n{urgency_note}\n\n"
        f"Actionable Nutrition Protocol:\n{diet_intensity}\n"
        f"- Execute a 15-to-20-minute brisk walk immediately after your largest meals.\n\n"
        f"IMPORTANT CLINICAL DISCLAIMER:\n"
        f"This automated analysis is for educational and wellness tracking purposes only. "
        f"It is not a medical prescription. Always consult a practicing physician before initiating any diet or lifestyle modifications."
    )
    
    st.markdown("---")
    st.subheader("📩 Download Official Client Report")
    st.download_button(
        label="Download Full Clinical Report PDF",
        data=report_content,
        file_name=f"{patient_name}_Longevity_Report.txt",
        mime="text/plain"
    )
        
st.markdown("---")
st.caption("⚠️ DEMO VERSION ONLY - NOT FOR CLINICAL USE. This website is currently under development for an academic validation project. Do not input real medical patient records.")
