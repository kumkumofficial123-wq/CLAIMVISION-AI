import streamlit as st

st.title("CLAIMVISION-AI")

claim = st.text_input(
    "Enter Claim"
)

image = st.file_uploader(
    "Upload Image"
)

if st.button("Analyze"):

    st.success(
        "Claim Analysis Started"
    )