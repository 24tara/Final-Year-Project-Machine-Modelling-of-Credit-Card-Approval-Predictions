
import streamlit as st
st.title("SoftCredit") 
st.header("Credit Card Approval Prediciton")
st.warning ("WARNING: Sensitive data that is collected will be deleted imediately, softcredit does not collect cookies. We vlaue privacy. ")
st.info("SoftCredit is a new way to check if you are eligilble for credit card approval without it negatively impacting your credit score. Unlike other platforms that perform hard credit checks, SoftCredit uses machine learning models to evaluate your application. This allows individuals to explore their financial options without the setback.")

#questions based feature vairables
no_of_dependents = st.number_input("How many dependents do you have?", 0,5)

education = st.selectbox("Are you a graduate?", ["Yes", "No"])
education = 1 if education == "Yes" else 2 

self_employed = st.selectbox("Are you self Employed" ,["Yes", "No"])
self_employed = 1 if self_employed == "Yes" else 0

income_annum = st.number_input("How much do you earn per annum?")

loan_amount = st.number_input ("What amount would you like to borrow from the bank?")

loan_term = st.slider ("Across how many month do you wish to pay back your loan?", 1,36)

cibil_score = st.number_input("What is your credit Score?")

residential_assets_value = st.number_input ("What value is your residential assets worth?", 0,20000000)

commercial_assets_value = st.number_input ("What value is your commercial assets worth?", 0,20000000)

luxury_assets_value = st.number_input ("What value is your luxury assets worth?", 0,20000000)

bank_asset_value = st.number_input ("What value is your bank asset worth?", 0,20000000)

st.subheader ("Why SoftCredit?")
st.info ("Current approval systems face many challenges such as manual reviewing systems, slow results, inconsistencies within approval applications, human error and bias, There is a lack of explainability for clients that are rejected and approved, meaning there is no clarity for a potential customers to improve their situation as they have little to no explanation sometimes. The results are based off a model that uses pycaret in a notebook. Users enter their details and it gets logged into the code and generates insights into the users results. Machine models remove ethical concerns. It improves the quality of checking the data in faster time.")

st.write("Thank you for using our service :) ") 