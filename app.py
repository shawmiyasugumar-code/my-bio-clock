import streamlit as st
import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestRegressor

# 1. Website Frontend Configuration
st.set_page_config(page_title="Longevity Bio-Clock", layout="centered")
st.title("🧬 Longevity & Anti-Aging Bio-Clock Analytics")
st.write("Enter biomarker data below to analyze clinical risks and biological aging.")

# Custom Organization Name Placeholder (The Illusion Box)
organization_name = st.text_input("Authorized Clinician / Clinic / Hospital Name", placeholder="Global Longevity Clinic")

# 2. AI Computational Engine Setup (9-Marker Programmatic Matrix)
@st.cache_resource
def train_ai_model():
    np.random.seed(42)
    n_samples = 1000
    chronological_age = np.random.uniform(20, 80, n_samples)
    
    # Simulating 9 PhenoAge Markers based on CDC NHANES trends
    albumin = 4.8 - (chronological_age * 0.015) + np.random.normal(0, 0.2, n_samples)
    glucose = 85 + (chronological_age * 0.4) + np.random.normal(0, 10, n_samples)
    hs_crp = 0.5 + (chronological_age * 0.04) + np.random.normal(0, 0.8, n_samples)
    creatinine = 0.7 + (chronological_age * 0.005) + np.random.normal(0, 0.1, n_samples)
    alp = 50 + (chronological_age * 0.5) + np.random.normal(0, 12, n_samples)
    wbc = 5.5 + (chronological_age * 0.02) + np.random.normal(0, 1.2, n_samples)
    lymph = 35 - (chronological_age * 0.1) + np.random.normal(0, 4, n_samples)
    rdw = 12.0 + (chronological_age * 0.02) + np.random.normal(0, 0.5, n_samples)
    mcv = 88.0 + np.random.normal(0, 3, n_samples)

    dataset = pd.DataFrame({
        'Chronological_Age': chronological_age, 'Albumin': albumin, 'Glucose': glucose, 'hs_CRP': hs_crp,
        'Creatinine': creatinine, 'ALP': alp, 'WBC': wbc, 'Lymph': lymph, 'RDW': rdw, 'MCV': mcv
    })
    
    X = dataset[['Albumin', 'Glucose', 'hs_CRP', 'Creatinine', 'ALP', 'WBC', 'Lymph', 'RDW', 'MCV']]
    y = dataset['Chronological_Age']
    
    model = RandomForestRegressor(n_estimators=100, random_state=42)
    model.fit(X, y)
    return model

ai_clock = train_ai_model()

# 3. Clinical Data Input Fields with Advanced Sex-Specific Controls
st.markdown("### 📋 Patient Biomarker Data Input")
patient_name = st.text_input("Patient Name", value="")
patient_gender = st.selectbox("Patient Biological Sex", ["Female", "Male"], index=None, placeholder="Select Patient Gender")
client_age = st.number_input("Chronological Age (Passport Age)", min_value=1, max_value=120, value=30, step=1)

col1, col2, col3 = st.columns(3)
with col1:
    client_albumin = st.number_input("Albumin Level (g/dL)", min_value=1.0, max_value=10.0, value=4.2, step=0.1)
    
    # Smart Gender-Based Creatinine Baseline (Apollo Hospitals Standard)
    default_creat = 0.8 if patient_gender == "Female" else 0.9
    client_creatinine = st.number_input("Creatinine Level (mg/dL)", min_value=0.1, max_value=15.0, value=default_creat, step=0.1)
    
    client_lymph = st.number_input("Lymphocyte (%)", min_value=1.0, max_value=100.0, value=30.0, step=1.0)
with col2:
    client_glucose = st.number_input("Fasting Glucose (mg/dL)", min_value=30.0, max_value=500.0, value=90.0, step=1.0)
    
    # Smart Gender-Based ALP Baseline (Medscape Standard)
    default_alp = 65.0 if patient_gender == "Female" else 75.0
    client_alp = st.number_input("ALP Level (U/L)", min_value=10.0, max_value=1000.0, value=default_alp, step=1.0)
    
    client_rdw = st.number_input("RDW (%)", min_value=5.0, max_value=50.0, value=13.0, step=0.1)
with col3:
    client_hs_crp = st.number_input("hs-CRP Level (mg/L)", min_value=0.0, max_value=50.0, value=0.8, step=0.1)
    client_wbc = st.number_input("WBC Count (cells/mcL)", min_value=1000.0, max_value=50000.0, value=6000.0, step=100.0)
    client_mcv = st.number_input("MCV Level (fL)", min_value=50.0, max_value=150.0, value=88.0, step=1.0)


# 4. Automated Report Generation Logic
if st.button("Generate Bio-Age Report"):
    new_client_data = pd.DataFrame(
        [[client_albumin, client_glucose, client_hs_crp, client_creatinine, client_alp, client_wbc, client_lymph, client_rdw, client_mcv]], 
        columns=['Albumin', 'Glucose', 'hs_CRP', 'Creatinine', 'ALP', 'WBC', 'Lymph', 'RDW', 'MCV']
    )
    calculated_bio_age = ai_clock.predict(new_client_data)
    final_bio_age = round(calculated_bio_age[0], 1)
    
    st.markdown("---")
    st.subheader(f"📊 Longevity Audit Report for {patient_name if patient_name else 'Valued Client'}")
    st.metric(label="Calculated Biological Age", value=f"{final_bio_age} Years Old")

        # Mathematical Gauge Calculation for the Graph
    age_delta = final_bio_age - client_age
    if age_delta < -2:
        gauge_color = "#2ecc71"  # Green (Younger)
        gauge_label = "YOUNGER THAN PASSPORT AGE (Optimal Cell Health)"
        gauge_percent = 25
    elif -2 <= age_delta <= 2:
        gauge_color = "#f39c12"  # Orange (Matches)
        gauge_label = "MATCHES PASSPORT AGE (Standard Cellular Aging)"
        gauge_percent = 50
    else:
        gauge_color = "#e74c3c"  # Red (Older)
        gauge_label = "OLDER THAN PASSPORT AGE (Accelerated Cellular Aging)"
        gauge_percent = 75

    # Dynamic Visual Gauge Graph using HTML/CSS
    st.markdown("### 📈 Biological Age Aging Gauge")
    st.markdown(f"""
        <div style="width: 100%; background-color: #112240; border-radius: 10px; padding: 20px; border: 1px solid #233554; text-align: center;">
            <div style="font-size: 16px; color: #8892b0; margin-bottom: 10px; font-weight: bold;">AGING RATE PROFILE</div>
            <div style="width: 100%; background-color: #233554; border-radius: 20px; height: 25px; position: relative; margin: 15px 0;">
                <div style="background-color: {gauge_color}; width: {gauge_percent}%; height: 100%; border-radius: 20px;"></div>
            </div>
            <div style="font-size: 16px; color: {gauge_color}; font-weight: bold;">{gauge_label}</div>
            <div style="font-size: 13px; color: #8892b0; margin-top: 5px;">Age Deviation Delta: {round(age_delta, 1)} Years</div>
        </div>
    """, unsafe_allow_html=True)

    # Clinical Risk Triggers & Data Compiling
    glucose_status = "OPTIMAL" if client_glucose <= 100 else ("SUBOPTIMAL" if client_glucose <= 125 else "CRITICAL")
    crp_status = "OPTIMAL" if client_hs_crp <= 1.0 else ("SUBOPTIMAL" if client_hs_crp <= 3.0 else "CRITICAL")
    albumin_status = "OPTIMAL" if client_albumin > 3.5 else "SUBOPTIMAL"
    kidney_status = "OPTIMAL" if client_creatinine <= 1.2 else "SUBOPTIMAL"
    liver_status = "OPTIMAL" if client_alp <= 147 else "SUBOPTIMAL"
    immune_status = "OPTIMAL" if 4500 <= client_wbc <= 11000 and 20 <= client_lymph <= 40 else "SUBOPTIMAL"
    blood_status = "OPTIMAL" if client_rdw <= 14.5 and 80 <= client_mcv <= 100 else "SUBOPTIMAL"

    st.markdown("### 🩺 Clinical Biomarker Systems Analysis")
    
    # Simplified Screen Dashboard Display
    st.info(f"**Metabolic Control (Glucose):** {glucose_status} | **Systemic Inflammation (hs-CRP):** {crp_status}")
    st.info(f"**Organ Vitality (Albumin/Creatinine/ALP):** Kidney: {kidney_status}, Liver: {liver_status}, Protein Status: {albumin_status}")
    st.info(f"**Hematological & Immune Clock (WBC/Lymph/RDW/MCV):** Immune Architecture: {immune_status}, Cellular Uniformity: {blood_status}")

    # Luxury HTML Output Block for direct browser rendering
    html_report = f"""
    <html>
    <head>
        <meta charset="UTF-8">
        <style>
            body {{ font-family: Arial, sans-serif; background-color: #0a192f; color: #ffffff; padding: 40px; }}
            .header {{ text-align: center; border-bottom: 2px solid #c5a059; padding-bottom: 20px; margin-bottom: 30px; }}
            .title {{ color: #c5a059; font-size: 26px; font-weight: bold; }}
            .meta-info {{ font-size: 15px; margin-top: 10px; color: #8892b0; line-height: 1.6; }}
            .box {{ background-color: #112240; border-radius: 8px; padding: 18px; margin-bottom: 20px; border-left: 4px solid #c5a059; }}
            .sec-title {{ font-size: 18px; color: #c5a059; font-weight: bold; margin-bottom: 8px; }}
            .val {{ color: #64ffda; font-weight: bold; }}
            .disclaimer {{ font-size: 12px; color: #8892b0; text-align: justify; margin-top: 30px; border-top: 1px solid #233554; padding-top: 15px; }}
        </style>
    </head>
    <body>
        <div class="header">
            <div class="title">ADVANCED 9-BIOMARKER LONGEVITY AUDIT</div>
            <div class="meta-info">
                <strong>Issuing Entity:</strong> {organization_name if organization_name else 'Global Longevity Network'} <br>
                <strong>Patient Name:</strong> {patient_name if patient_name else 'Valued Client'} &nbsp;|&nbsp; 
                <strong>Chronological Age:</strong> {client_age} Years &nbsp;|&nbsp; 
                <strong>Calculated Biological Age:</strong> {final_bio_age} Years
            </div>
        </div>
                <div class="graph-container">
            <div style="font-size: 14px; color: #8892b0; font-weight: bold; text-align: center; margin-bottom: 10px;">VISUAL BIOLOGICAL AGING METER</div>
            <div class="bar-bg" style="background-color: #233554; border-radius: 15px; height: 20px; width: 100%; margin: 15px 0;"><div class="bar-fill" style="background-color: f_string_color; width: f_string_percent%; height: 100%; border-radius: 15px;"></div></div>
            <div style="color: f_string_color; font-weight: bold; font-size: 16px; text-align: center;">f_string_label</div>
            <div style="font-size: 12px; color: #8892b0; margin-top: 4px; text-align: center;">Calculated Biological Deviation Delta: f_string_delta Years</div>
        </div>


        <div class="box">
            <div class="sec-title">1. METABOLIC REGULATION SYSTEM</div>
            Fasting Glucose: <span class="val">{client_glucose} mg/dL ({glucose_status})</span><br>
            <em>Clinical Insight:</em> Ideal homeostatic regulation mitigates cellular protein glycation and preserves endothelial wall structures from structural decay.
        </div>

        <div class="box">
            <div class="sec-title">2. CARDIOVASCULAR INFLAMMAGING INFRASTRUCTURE</div>
            High-Sensitivity CRP: <span class="val">{client_hs_crp} mg/L ({crp_status})</span><br>
            <em>Clinical Insight:</em> Low Systemic inflammation prevents micro-vascular stiffening and maintains biological protection over cell renewal architectures.
        </div>

        <div class="box">
            <div class="sec-title">3. BIOSYNTHETIC ORGAN VITALITY MATRIX</div>
            Serum Albumin: <span class="val">{client_albumin} g/dL ({albumin_status})</span> &nbsp;|&nbsp;
            Creatinine: <span class="val">{client_creatinine} mg/dL ({kidney_status})</span> &nbsp;|&nbsp;
            Alkaline Phosphatase (ALP): <span class="val">{client_alp} U/L ({liver_status})</span><br>
            <em>Clinical Insight:</em> Reflects clear cellular filtration balance and robust liver-biosynthetic reserve critical to whole-body protein homeostasis.
        </div>

        <div class="box">
            <div class="sec-title">4. HEMATOLOGICAL & CELLULAR UNIFORMITY CLOCK</div>
            WBC Count: <span class="val">{client_wbc} cells/mcL</span> &nbsp;|&nbsp;
            Lymphocyte: <span class="val">{client_lymph}%</span> &nbsp;|&nbsp;
            RDW: <span class="val">{client_rdw}%</span> &nbsp;|&nbsp;
            MCV: <span class="val">{client_mcv} fL</span> ({blood_status})<br>
            <em>Clinical Insight:</em> Evaluates cell-size variability and adaptive immune resilience thresholds to identify underlying markers of immune system aging.
        </div>

        <div class="disclaimer">
            <strong>IMPORTANT CLINICAL DISCLAIMER:</strong> This automated software audit is compiled exclusively for longevity wellness metrics and educational tracking. It is completely independent of specific drug or diet prescriptions. Always consult your practicing healthcare professional for definitive physical evaluations.
        </div>
    </body>
    </html>
    """

    st.markdown("---")
    st.subheader("📩 Download Official Professional Color Report")
    st.download_button(
        label="Download Full 9-Biomarker Color Report",
        data=html_report,
        file_name=f"{patient_name if patient_name else 'Client'}_Longevity_Report.html",
        mime="text/html"
    )
        
st.markdown("---")
st.caption("⚠️ DEMO VERSION ONLY - NOT FOR CLINICAL USE. This website is currently under development for an academic validation project. Do not input real medical patient records.")
