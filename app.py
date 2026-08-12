import streamlit as st
import joblib
import pandas as pd

# Load model
model = joblib.load("credit_approval_model.pkl")

# Page setup
st.set_page_config(
    page_title="Credit Card Approval Prediction",
    page_icon="💳"
)

st.title("💳 Credit Card Approval Prediction")
st.write("Enter applicant information below.")

# =========================
# INPUTS
# =========================

st.subheader("Applicant Information")

gender = st.selectbox("Gender", ["Female", "Male"])

age = st.number_input(
    "Age",
    min_value=0.0,
    max_value=100.0,
    value=30.0
)

debt = st.number_input(
    "Debt",
    min_value=0.0,
    value=0.0
)

married = st.selectbox(
    "Marital Status",
    ["Other", "Single", "Married"]
)

bank_customer = st.selectbox(
    "Bank Customer",
    ["Government", "Other", "Private"]
)

education = st.selectbox(
    "Education Level",
    [f"Category {i}" for i in range(14)]
)

ethnicity = st.selectbox(
    "Ethnicity",
    [f"Category {i}" for i in range(9)]
)

years_employed = st.number_input(
    "Years Employed",
    min_value=0.0,
    value=1.0
)

prior_default = st.selectbox(
    "Prior Default",
    ["No", "Yes"]
)

employed = st.selectbox(
    "Employed",
    ["No", "Yes"]
)

credit_score = st.number_input(
    "Credit Score",
    min_value=0,
    value=1
)

driver_license = st.selectbox(
    "Driver's License",
    ["No", "Yes"]
)

citizen = st.selectbox(
    "Citizen",
    [f"Category {i}" for i in range(3)]
)

zip_code = st.number_input(
    "ZIP Code",
    min_value=0,
    value=0
)

income = st.number_input(
    "Income",
    min_value=0.0,
    value=0.0
)

# =========================
# ENCODING
# =========================

gender_encoded = 0 if gender == "Female" else 1

married_encoded = {
    "Other": 0,
    "Single": 1,
    "Married": 2
}[married]

bank_customer_encoded = {
    "Government": 0,
    "Other": 1,
    "Private": 2
}[bank_customer]

prior_default_encoded = 0 if prior_default == "No" else 1

employed_encoded = 0 if employed == "No" else 1

driver_license_encoded = 0 if driver_license == "No" else 1

education_encoded = int(education.split()[-1])

ethnicity_encoded = int(ethnicity.split()[-1])

citizen_encoded = int(citizen.split()[-1])

# =========================
# CREATE MODEL INPUT
# =========================

input_data = pd.DataFrame(
    [[
        income,
        zip_code,
        citizen_encoded,
        driver_license_encoded,
        credit_score,
        employed_encoded,
        prior_default_encoded,
        years_employed,
        ethnicity_encoded,
        education_encoded,
        bank_customer_encoded,
        married_encoded,
        debt,
        age,
        gender_encoded
    ]],
    columns=[
        "A15",
        "A14",
        "A13",
        "A12",
        "A11",
        "A10",
        "A9",
        "A8",
        "A7",
        "A6",
        "A5",
        "A4",
        "A3",
        "A2",
        "A1"
    ]
)

# =========================
# PREDICTION
# =========================

if st.button("Predict Approval"):

    prediction = model.predict(input_data)[0]

    if prediction == 1:
        st.success("✅ Credit Card Approved")
    else:
        st.error("❌ Credit Card Not Approved")
