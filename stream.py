import streamlit as st
import requests

st.title("Marketing ROI Prediction & Recommendations")

input_type = st.radio("Input type:", ["Upload file", "JSON input"])

if input_type == "Upload file":
    uploaded_file = st.file_uploader("Upload CSV/XLSX", type=["csv", "xlsx"])
    if uploaded_file and st.button("Predict"):
        files = {"file": uploaded_file.getvalue()}
        res = requests.post("https://gcp-1-jgzq.onrender.com/predict/file", files={"file": uploaded_file})
        if res.status_code == 200:
            data = res.json()
            st.write("Predictions:", data["predictions"])
            st.write("Recommendations:", data["recommendations"])
        else:
            st.error(res.text)

else:  # JSON input
    user_input = st.text_area("Paste JSON data here")
    if st.button("Predict"):
        import json
        payload = {"data": json.loads(user_input)}
        res = requests.post("https://gcp-1-jgzq.onrender.com/predict/json", json=payload)
        if res.status_code == 200:
            data = res.json()
            st.write("Predictions:", data["predictions"])
            st.write("Recommendations:", data["recommendations"])
        else:
            st.error(res.text)
