import streamlit as st
import joblib


# CSS for background image
page_bg_img = '''
<style>
body {
    background-image: url("./email_bg.jpg");
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

# User input
user_input = st.text_area("Enter email text here:")

# Load model and vectorizer
vectorizer = joblib.load("vectorizer.pkl")
model = joblib.load("naive_bayes_model.pkl")


# Button for prediction
if st.button("Check Spam/Ham"):
    if user_input.strip() == "":
        st.warning("Please enter some email text.")
    else:
        # Transform input text to vector
        user_vec = vectorizer.transform([user_input])

        # Predict spam or ham
        prediction = model.predict(user_vec)[0]

        if prediction == 1:
            st.error("This email is **Spam**!")
        else:
            st.success("This email is **Ham (Not Spam)**.")

# Footer
st.markdown("<br><hr><center>Developed by Yasir</center>", unsafe_allow_html=True)
