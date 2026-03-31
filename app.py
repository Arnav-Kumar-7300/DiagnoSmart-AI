import streamlit as st

st.set_page_config(page_title="DiagnoSmart AI", layout="centered")

st.title("🧠DiagnoSmart AI : Intelligent Diagnostic Report Analyzer")
st.info("ℹ️Values are based on general clinical reference ranges commonly reported in India.")
st.warning("⚠️This tool is for educational purposes only and not a substitute for professional medical advice.")

# ---------------- ANALYSIS ----------------

def analyze(values, ranges, disease_name):
    score = 0
    total = len(values)

    for v, (low, high) in zip(values, ranges):
        if v < low or v > high:
            deviation = abs(v - (low + high)/2)
            if deviation > (high - low):
                score += 2
            else:
                score += 1

    # ✅ If all values normal
    if score == 0:
        return "Normal (No Disease Risk)", None

    ratio = score / (2 * total)

    if ratio < 0.3:
        severity = "Mild"
    elif ratio < 0.6:
        severity = "Moderate"
    else:
        severity = "High"

    return f"{disease_name} Risk", severity


# ---------------- RECOMMENDATION ----------------

def recommendation(severity):
    if severity == "Mild":
        return [
            "Improve diet quality",
            "Drink more water",
            "Exercise daily",
            "Avoid junk food",
            "Get proper sleep"
        ], "Monitor condition. Consult doctor if it persists"

    elif severity == "Moderate":
        return [
            "Follow strict diet plan",
            "Avoid processed foods",
            "Regular monitoring required",
            "Take proper rest",
            "Reduce sugar/salt intake"
        ], "Consult a doctor soon"

    else:
        return [
            "Immediate lifestyle changes required",
            "Avoid harmful foods completely",
            "Do not ignore symptoms",
            "Take medical tests immediately",
            "Continuous monitoring needed"
        ], "⚠️ Consult a doctor as soon as possible"


# ---------------- TEST ----------------

test = st.selectbox("Select Diagnostic Test", [
    "Blood Test","LFT","KFT","Diabetes","Lipid Profile",
    "Thyroid","Urine","Bone","Blood Pressure","Sonography"
])

# ---------------- INPUTS ----------------

if test == "Blood Test":
    st.subheader("📊 Normal Ranges")
    st.table({
        "Parameter": ["Hemoglobin", "WBC", "Platelets"],
        "Range": ["12–16 g/dL", "4000–11000 cells/µL", "150000–450000 cells/µL"]
    })

    Hb = st.number_input("Hemoglobin (g/dL)", value=13.0)
    WBC = st.number_input("WBC (cells/µL)", value=8000.0)
    Platelets = st.number_input("Platelets (cells/µL)", value=250000.0)

    values = [Hb, WBC, Platelets]
    ranges = [(12,16),(4000,11000),(150000,450000)]
    disease = "Anemia / Infection"


elif test == "LFT":
    st.table({
        "Parameter": ["Bilirubin", "SGOT", "SGPT"],
        "Range": ["0.1–1.2 mg/dL", "10–40 U/L", "7–56 U/L"]
    })

    Bilirubin = st.number_input("Bilirubin (mg/dL)", value=0.8)
    SGOT = st.number_input("SGOT (U/L)", value=30.0)
    SGPT = st.number_input("SGPT (U/L)", value=30.0)

    values = [Bilirubin, SGOT, SGPT]
    ranges = [(0.1,1.2),(10,40),(7,56)]
    disease = "Jaundice / Liver Disease"


elif test == "KFT":
    st.table({
        "Parameter": ["Creatinine", "Urea"],
        "Range": ["0.6–1.3 mg/dL", "15–40 mg/dL"]
    })

    Creatinine = st.number_input("Creatinine (mg/dL)", value=1.0)
    Urea = st.number_input("Urea (mg/dL)", value=30.0)

    values = [Creatinine, Urea]
    ranges = [(0.6,1.3),(15,40)]
    disease = "Kidney Dysfunction"


elif test == "Diabetes":
    st.table({
        "Parameter": ["Fasting Sugar", "Post Meal"],
        "Range": ["70–99 mg/dL", "<140 mg/dL"]
    })

    Fasting = st.number_input("Fasting Sugar (mg/dL)", value=90.0)
    PP = st.number_input("Post Meal Sugar (mg/dL)", value=120.0)

    values = [Fasting, PP]
    ranges = [(70,99),(0,140)]
    disease = "Diabetes"


elif test == "Lipid Profile":
    st.table({
        "Parameter": ["Cholesterol", "Triglycerides", "HDL"],
        "Range": ["<200 mg/dL", "50–150 mg/dL", "40–60 mg/dL"]
    })

    Chol = st.number_input("Cholesterol (mg/dL)", value=180.0)
    TG = st.number_input("Triglycerides (mg/dL)", value=120.0)
    HDL = st.number_input("HDL (mg/dL)", value=50.0)

    values = [Chol, TG, HDL]
    ranges = [(0,200),(50,150),(40,60)]
    disease = "Heart Disease / Cholesterol"


elif test == "Thyroid":
    st.table({
        "Parameter": ["TSH", "T3", "T4"],
        "Range": ["0.4–4 mIU/L", "0.8–2 ng/mL", "5–12 µg/dL"]
    })

    TSH = st.number_input("TSH (mIU/L)", value=2.0)
    T3 = st.number_input("T3 (ng/mL)", value=1.5)
    T4 = st.number_input("T4 (µg/dL)", value=9.0)

    values = [TSH, T3, T4]
    ranges = [(0.4,4),(0.8,2),(5,12)]
    disease = "Thyroid Disorder"


elif test == "Urine":
    st.table({
        "Parameter": ["pH", "Protein", "Glucose"],
        "Range": ["4.5–8.5", "<0.3 mg/dL", "<0.3 mg/dL"]
    })

    pH = st.number_input("pH", value=6.0)
    Protein = st.number_input("Protein (mg/dL)", value=0.1)
    Glucose = st.number_input("Glucose (mg/dL)", value=0.1)

    values = [pH, Protein, Glucose]
    ranges = [(4.5,8.5),(0,0.3),(0,0.3)]
    disease = "Urinary Infection"


elif test == "Bone":
    st.table({
        "Parameter": ["Calcium", "Vitamin D"],
        "Range": ["8.5–10.5 mg/dL", "20–50 ng/mL"]
    })

    Calcium = st.number_input("Calcium (mg/dL)", value=9.5)
    VitaminD = st.number_input("Vitamin D (ng/mL)", value=30.0)

    values = [Calcium, VitaminD]
    ranges = [(8.5,10.5),(20,50)]
    disease = "Bone Weakness / Vitamin Deficiency"


elif test == "Blood Pressure":
    st.table({
        "Parameter": ["Systolic", "Diastolic"],
        "Range": ["90–140 mmHg", "60–90 mmHg"]
    })

    Sys = st.number_input("Systolic (mmHg)", value=120.0)
    Dia = st.number_input("Diastolic (mmHg)", value=80.0)

    values = [Sys, Dia]
    ranges = [(90,140),(60,90)]
    disease = "Hypertension"


elif test == "Sonography":
    st.table({
        "Parameter": ["Liver Size", "Gallbladder", "Kidney Size"],
        "Range": ["10–16 cm", "0 = Normal", "9–12 cm"]
    })

    Liver = st.number_input("Liver Size (cm)", value=14.0)
    Gall = st.number_input("Gallbladder (0 Normal / 1 Abnormal)", value=0.0)
    Kidney = st.number_input("Kidney Size (cm)", value=11.0)

    values = [Liver, Gall, Kidney]
    ranges = [(10,16),(0,0),(9,12)]
    disease = "Gallstones / Organ Issue"


# ---------------- OUTPUT ----------------

if st.button("Analyze"):
    result, severity = analyze(values, ranges, disease)

    # ✅ NORMAL CASE
    if severity is None:
        st.success("✅ Normal (No Disease Risk)")
        st.write("✔️ Your parameters are within healthy range.")
        st.write("✔️ Maintain a healthy lifestyle.")

    # ✅ ABNORMAL CASE
    else:
        tips, doctor_msg = recommendation(severity)

        st.subheader("🔍 Predicted Disease Risk")
        st.write(result)

        st.subheader("⚠️ Severity Level")
        st.write(severity)

        st.subheader("💡 Tips & Precautions")
        for tip in tips:
            st.write("•", tip)

        st.subheader("👨‍⚕️ Medical Recommendation")
        st.write(doctor_msg)