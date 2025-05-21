import streamlit as st
import joblib

# CSS for background image
page_bg_img = '''
<style>
body {
    background-image: url("email_bg.jpg");
    background-size: cover;
    background-position: center;
    background-repeat: no-repeat;
    background-attachment: fixed;
}
.stApp {
    background: transparent !important;
}
</style>
'''
st.markdown(page_bg_img, unsafe_allow_html=True)

# Title and description
st.title("Email Spam Classifier")
st.write("Enter your email text below and check whether it is spam or not.")

# Load vectorizer and model
vectorizer = joblib.load("vectorizer.pkl")
model = joblib.load("naive_bayes_model.pkl")

# User input
user_input = st.text_area("Enter email text here:")

# Prediction logic
if st.button("Check Spam/Ham"):
    if user_input.strip() == "":
        st.warning("Please enter some email text.")
    else:
        user_vector = vectorizer.transform([user_input])
        prediction = model.predict(user_vector)[0]

        # Make sure: 0 = Spam, 1 = Ham
        if prediction == 0:
            st.error("⚠️ This email is **Spam(Be carefull)**!")
        else:
            st.success("✅ This email is **Ham **.")

# Footer
st.markdown("<br><hr><center>Developed by Yasir</center>", unsafe_allow_html=True)
