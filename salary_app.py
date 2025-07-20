import streamlit as st
import pandas as pd
import numpy as np
import joblib
import matplotlib.pyplot as plt
from datetime import datetime


# Load model
model = joblib.load("best_model.pkl")

# For dropdowns excess keys()
job_title = [
   'Software Engineer', 'Data Analyst', 'Senior Manager',
       'Sales Associate', 'Director', 'Marketing Analyst',
       'Product Manager', 'Sales Manager', 'Marketing Coordinator',
       'Senior Scientist', 'Software Developer', 'HR Manager',
       'Financial Analyst', 'Project Manager', 'Customer Service Rep',
       'Operations Manager', 'Marketing Manager', 'Senior Engineer',
       'Data Entry Clerk', 'Sales Director', 'Business Analyst',
       'VP of Operations', 'IT Support', 'Recruiter', 'Financial Manager',
       'Social Media Specialist', 'Software Manager', 'Junior Developer',
       'Senior Consultant', 'Product Designer', 'CEO', 'Accountant',
       'Data Scientist', 'Marketing Specialist', 'Technical Writer',
       'HR Generalist', 'Project Engineer', 'Customer Success Rep',
       'Sales Executive', 'UX Designer', 'Operations Director',
       'Network Engineer', 'Administrative Assistant',
       'Strategy Consultant', 'Copywriter', 'Account Manager',
       'Director of Marketing', 'Help Desk Analyst',
       'Customer Service Manager', 'Business Intelligence Analyst',
       'Event Coordinator', 'VP of Finance', 'Graphic Designer',
       'UX Researcher', 'Social Media Manager', 'Director of Operations',
       'Senior Data Scientist', 'Junior Accountant',
       'Digital Marketing Manager', 'IT Manager',
       'Customer Service Representative', 'Business Development Manager',
       'Senior Financial Analyst', 'Web Developer', 'Research Director',
       'Technical Support Specialist', 'Creative Director',
       'Senior Software Engineer', 'Human Resources Director',
       'Content Marketing Manager', 'Technical Recruiter',
       'Sales Representative', 'Chief Technology Officer',
       'Junior Designer', 'Financial Advisor', 'Junior Account Manager',
       'Senior Project Manager', 'Principal Scientist',
       'Supply Chain Manager', 'Senior Marketing Manager',
       'Training Specialist', 'Research Scientist',
       'Junior Software Developer', 'Public Relations Manager',
       'Operations Analyst', 'Product Marketing Manager',
       'Senior HR Manager', 'Junior Web Developer',
       'Senior Project Coordinator', 'Chief Data Officer',
       'Digital Content Producer', 'IT Support Specialist',
       'Senior Marketing Analyst', 'Customer Success Manager',
       'Senior Graphic Designer', 'Software Project Manager',
       'Supply Chain Analyst', 'Senior Business Analyst',
       'Junior Marketing Analyst', 'Office Manager', 'Principal Engineer',
       'Junior HR Generalist', 'Senior Product Manager',
       'Junior Operations Analyst', 'Senior HR Generalist',
       'Sales Operations Manager', 'Senior Software Developer',
       'Junior Web Designer', 'Senior Training Specialist',
       'Senior Research Scientist', 'Junior Sales Representative',
       'Junior Marketing Manager', 'Junior Data Analyst',
       'Senior Product Marketing Manager', 'Junior Business Analyst',
       'Senior Sales Manager', 'Junior Marketing Specialist',
       'Junior Project Manager', 'Senior Accountant', 'Director of Sales',
       'Junior Recruiter', 'Senior Business Development Manager',
       'Senior Product Designer', 'Junior Customer Support Specialist',
       'Senior IT Support Specialist', 'Junior Financial Analyst',
       'Senior Operations Manager', 'Director of Human Resources',
       'Junior Software Engineer', 'Senior Sales Representative',
       'Director of Product Management', 'Junior Copywriter',
       'Senior Marketing Coordinator', 'Senior Human Resources Manager',
       'Junior Business Development Associate', 'Senior Account Manager',
       'Senior Researcher', 'Junior HR Coordinator',
       'Director of Finance', 'Junior Marketing Coordinator',
       'Junior Data Scientist', 'Senior Operations Analyst',
       'Senior Human Resources Coordinator', 'Senior UX Designer',
       'Junior Product Manager', 'Senior Marketing Specialist',
       'Senior IT Project Manager', 'Senior Quality Assurance Analyst',
       'Director of Sales and Marketing', 'Senior Account Executive',
       'Director of Business Development', 'Junior Social Media Manager',
       'Senior Human Resources Specialist', 'Senior Data Analyst',
       'Director of Human Capital', 'Junior Advertising Coordinator',
       'Junior UX Designer', 'Senior Marketing Director',
       'Senior IT Consultant', 'Senior Financial Advisor',
       'Junior Business Operations Analyst',
       'Junior Social Media Specialist',
       'Senior Product Development Manager', 'Junior Operations Manager',
       'Senior Software Architect', 'Junior Research Scientist',
       'Senior Financial Manager', 'Senior HR Specialist',
       'Senior Data Engineer', 'Junior Operations Coordinator',
       'Director of HR', 'Senior Operations Coordinator',
       'Junior Financial Advisor', 'Director of Engineering'
]
education = ["High School", "Associate's Degree", "Bachelor's Degree", "Master's Degree", "Doctorate", "Other"]
gender = ["Male", "Female"]

# Minimum age logic
min_age_map = {
    "Bachelor's Degree": 22,
    "Master's Degree": 24,
    "Doctorate": 30,
    "High School":18
}

def is_valid_combination(age, experience, education):
    min_required_age = min_age_map.get(education, 18)
    return age >= min_required_age and age >= (experience + min_required_age - 2)

# --------------------------
# Streamlit UI
# --------------------------
st.set_page_config(page_title="Salary Predictor", page_icon="💼")

st.markdown("""
    <style>
    body {
        background-color: #fdf0d5;
        color: #432818;
    }
    .reportview-container .main .block-container {
        color: #432818;
    }
    .stAlert {
        background-color: #c1121f !important;
        color: white !important;
    }
    .stSuccess {
        background-color: #003049 !important;
        color: #fdf0d5 !important;
        font-weight: bold;
        font-size: 18px;
        padding: 1rem;
        border-radius: 10px;
    }
    .stButton > button {
        background-color: #FFEDDF;
        color: #000000;
        border: 1px solid #ccc;
        border-radius: 8px;
        padding: 0.5em 1.2em;
        font-weight: bold;
        transition: background-color 0.3s ease;
    }
    .stButton > button:hover {
        background-color: #f2dac4;
        cursor: pointer;
    }
    .custom-download-button {
        background-color: #283618;
        color: #fefae0;
        padding: 0.6em 1.2em;
        font-size: 16px;
        font-weight: bold;
        border: none;
        border-radius: 10px;
        transition: 0.3s ease;
    }
    .custom-download-button:hover {
        background-color: #2a9d8f;
        color: #fdfdfd;
        cursor: pointer;
    }
    </style>
""", unsafe_allow_html=True)

# Title
st.title("💼 Smart Salary Predictor")
st.write("Fill up the details and get your expected salary")

# Inputs
age = st.number_input("Age", min_value=5, max_value=100, step=1)

with st.expander("💼 Job Details", expanded=True):
    job_title = st.selectbox(" Select Job Title",sorted(job_title))
    experience = st.slider("Years of Experience", 0, 50, 2)

with st.expander("🎓 Education Details", expanded=True):
    education = st.selectbox("Education Level", education)

gender = st.selectbox("Gender", gender)

currency_option = st.radio("Choose your preferred currency:", ["INR (₹)", "USD ($)"])

# Prediction
if st.button("🔮 Predict Salary"):
    if not is_valid_combination(age, experience, education):
        st.error("⚠️ No logical match between age, experience, and education. Please check your inputs.")
    else:
        # Input data for prediction
        input_data = pd.DataFrame([{
            'Age': age,
            'Years of Experience': experience,
            'Education Level': education,
            'Job Title': job_title,
            'Gender': gender
        }])

        # Make prediction
        salary_pred = model.predict(input_data)[0]
        salary_display = salary_pred if currency_option == "INR (₹)" else salary_pred / 83.0

        # Show final prediction 
        if currency_option == "USD ($)":
            st.success(f"💵 Estimated Salary: ${salary_display:,.2f}")
            st.toast("Salary Predicted Successfully!", icon="🎉")
        else:
            st.success(f"💵 Estimated Salary: ₹{salary_display:,.2f}")
            st.toast("Salary Predicted Successfully!", icon="🎉")

        # 📊 Salary Range Chart
        st.markdown("### 📈 Salary Range Visualization")
        min_range = salary_pred * 0.85
        max_range = salary_pred * 1.15
        salaries = [min_range, salary_pred, max_range]
        labels = ['Low Estimate', 'Predicted', 'High Estimate']
        colors = ['#FFDDE2', '#EFD6D2', '#6F5E76']

        fig, ax = plt.subplots()
        ax.bar(labels, salaries, color=colors)
        ax.set_ylabel("Salary")
        st.pyplot(fig)

         # --- Report Section ---

        model_accuracy = 92.56  # Manually written
        def center_text_block(text, width=80):
            return "\n".join(line.center(width) for line in text.strip().split("\n"))

        header = f"""
            Salary Predictor Report
            --------------------------------------------------------------------------------
            📅 Date: {datetime.now().strftime("%Y-%m-%d")}
            """

        user_details_table = f"""
            👤 User Details:
            +------------+----------------------+
            | Field      | Value                |
            +------------+----------------------+
            | Age        | {str(age):<21}|
            | Gender     | {gender:<21}|
            | Education  | {education:<21}|
            | Job Title  | {job_title:<21}|
            | Experience | {(str(experience) + ' years'):<21}|
            +------------+----------------------+
        """
        currency_symbol = "₹" if currency_option == "INR (₹)" else "$"
        salary_prediction_table = f"""
        💼 Salary Prediction:
        +---------------------+-------------------+-------------------+
        | Estimated Salary    | Minimum Salary    | Maximum Salary    |
        +---------------------+-------------------+-------------------+
        |{currency_symbol} {salary_display:>19,.2f}| {currency_symbol} {min_range:>15,.2f}|{currency_symbol} {max_range:>15,.2f}|
        +---------------------+-------------------+-------------------+
        """

        accuracy_section = f"""
        📊 Model Performance:
        Accuracy of the model: {model_accuracy:.2f}%
        """

        footer = """
        🙏 Thank you for using the Salary Predictor!

        📌 Note: Salary predictions are based on machine learning models trained on historical data.
        Actual values may vary depending on location, company, and market trends.
        """

        full_report = "\n\n".join([
            center_text_block(header),
            center_text_block(user_details_table),
            center_text_block(salary_prediction_table),
            center_text_block(accuracy_section),
            "-" * 100,
            center_text_block(footer)
        ])
       
        with st.expander("📄 View Full Salary Report"):
           st.code(full_report, language="text")

        if st.button("💾 Save"):
            with open("salary_report.txt", "w", encoding="utf-8") as file:
                file.write(full_report)

        st.subheader("📄 Download Salary Report")
        if st.download_button(
            label="📅 Download",
            data=full_report,
            file_name="salary_report.txt",
            mime="text/plain"
        ):
            st.toast("Download Successful!", icon="🎉")

# --- website Footer ---
st.markdown("---")
st.markdown("""
<style>
.feedback-link {
    color: #1a73e8;
    font-weight: 400;
    text-decoration: none;
    font-style: italic;
    transition: color 0.3s ease, text-decoration 0.3s ease, font-size 0.3s ease;
}

.feedback-link:hover {
    color: #90caf9; 
    text-decoration: underline;
    text-shadow: 0px 0px 4px #90caf9;
    font-size: 17px;
}

/* Icon hover styles */
.icon-hover {
    transition: transform 0.3s ease, filter 0.3s ease;
}

.icon-hover:hover {
    transform: scale(1.2);
    filter: brightness(1.3);
}
</style>

<p align="center" style="font-size: 16px; color: white;">
    🙏 Thank you for using <strong>Smart Salary Predictor</strong><br><br>
    <span style="font-weight: 300; color: #cccccc;">
        📝 <a href="https://docs.google.com/forms/d/e/1FAIpQLSfztUsU-0QDf98F2rDjkK7mN7BbJYZpc-CNWvBwQrc94ziyNg/viewform?usp=header" 
              target="_blank" 
              class="feedback-link">
            Click here
        </a> to give your valuable feedback
    </span>
</p>

<div style="display: flex; justify-content: center; align-items: center; gap: 24px; margin-top: 10px;">
    <a href="https://github.com/Prachikdhunde04" target="_blank">
        <img class="icon-hover" src="https://cdn-icons-png.flaticon.com/512/25/25231.png" width="30" />
    </a>
    <a href="https://www.linkedin.com/in/prachi-dhunde-408b2825a/" target="_blank">
        <img class="icon-hover" src="https://cdn-icons-png.flaticon.com/512/174/174857.png" width="30" />
    </a>
    <a href="mailto:prachidhunde@gmail.com">
        <img class="icon-hover" src="https://cdn-icons-png.flaticon.com/512/732/732200.png" width="30" />
    </a>
</div>

<p align="center" style="margin-top: 12px; color: #888;">© 2025 Prachi Dhunde. All rights reserved.</p>
""", unsafe_allow_html=True)
