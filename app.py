import streamlit as st
import joblib
import pandas as pd

# Load trained model
model = joblib.load("credit_approval_model.pkl")

# Page configuration
st.set_page_config(
    page_title="Credit Card Approval Prediction",
    page_icon="💳"
)

# Title
st.title("💳 Credit Card Approval Prediction")

st.write(
    "Enter the applicant information below "
    "to predict credit card approval."
)

# Input features
st.subheader("Applicant Information")

# Categorical features
gender = st.selectbox("Gender", ["Female", "Male"])

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

prior_default = st.selectbox(
    "Prior Default",
    ["No", "Yes"]
)

employed = st.selectbox(
    "Employed",
    ["No", "Yes"]
)

driver_license = st.selectbox(
    "Driver's License",
    ["No", "Yes"]
)

citizen = st.selectbox(
    "Citizen",
    [f"Category {i}" for i in range(3)]
)

# Continuous features
age = st.number_input("Age", min_value=0.0, max_value=100.0, value=30.0)

debt = st.number_input("Debt", min_value=0.0, value=0.0)

years_employed = st.number_input(
    "Years Employed",
    min_value=0.0,
    value=1.0
)

credit_score = st.number_input(
    "Credit Score",
    min_value=0,
    value=1
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

# Create input DataFrame
input_data = pd.DataFrame([[
    income,                  # A15
    zip_code,                # A14
    citizen_encoded,         # A13
    driver_license_encoded,  # A12
    credit_score,            # A11
    employed_encoded,        # A10
    prior_default_encoded,   # A9
    years_employed,          # A8
    ethnicity_encoded,       # A7
    education_encoded,       # A6
    bank_customer_encoded,   # A5
    married_encoded,         # A4
    debt,                    # A3
    age,                     # A2
    gender_encoded           # A1
]], columns=[
    "A15", "A14", "A13", "A12", "A11",
    "A10", "A9", "A8", "A7", "A6",
    "A5", "A4", "A3", "A2", "A1"
])
# Convert categorical values to encoded values

gender_encoded = {
    "Female": 0,
    "Male": 1
}[gender]

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

prior_default_encoded = {
    "No": 0,
    "Yes": 1
}[prior_default]

employed_encoded = {
    "No": 0,
    "Yes": 1
}[employed]

driver_license_encoded = {
    "No": 0,
    "Yes": 1
}[driver_license]

education_encoded = int(education.split()[-1])

ethnicity_encoded = int(ethnicity.split()[-1])

citizen_encoded = int(citizen.split()[-1])

input_data = pd.DataFrame([[
    income,                  # A15
    zip_code,                # A14
    citizen_encoded,         # A13
    driver_license_encoded,  # A12
    credit_score,            # A11
    employed_encoded,        # A10
    prior_default_encoded,   # A9
    years_employed,          # A8
    ethnicity_encoded,       # A7
    education_encoded,       # A6
    bank_customer_encoded,   # A5
    married_encoded,         # A4
    debt,                    # A3
    age,                     # A2
    gender_encoded           # A1
]], columns=[
    "A15", "A14", "A13", "A12", "A11",
    "A10", "A9", "A8", "A7", "A6",
    "A5", "A4", "A3", "A2", "A1"
])

# Prediction
if st.button("Predict Approval"):

    prediction = model.predict(input_data)[0]

    if prediction == 1:
        st.success("✅ Credit Card Approved")
    else:
        st.error("❌ Credit Card Not Approved")
