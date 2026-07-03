from chatbot import chat_with_dataset
import streamlit as st
import os

from eda import load_data, dataset_summary
from visualization import create_visualizations
from gemini_ai import generate_insights
from report import generate_report

# ----------------------------------
# Page Configuration
# ----------------------------------
st.set_page_config(
    page_title="AI Powered EDA Assistant",
    page_icon="📊",
    layout="wide"
)

st.title("📊 AI Powered EDA Assistant")
st.write("Upload a CSV or Excel file to perform automatic EDA with Gemini AI.")

# ----------------------------------
# Upload File
# ----------------------------------
uploaded_file = st.file_uploader(
    "Upload CSV or Excel File",
    type=["csv", "xlsx"]
)

if uploaded_file:

    # Load Dataset
    df = load_data(uploaded_file)

    st.success("Dataset Loaded Successfully!")

    # ----------------------------------
    # Dataset Preview
    # ----------------------------------
    st.header("Dataset Preview")
    st.dataframe(df)

    # ----------------------------------
    # Dataset Summary
    # ----------------------------------
    summary = dataset_summary(df)

    st.header("Dataset Summary")

    st.write("### Rows")
    st.write(summary["Rows"])

    st.write("### Columns")
    st.write(summary["Columns"])

    st.write("### Column Names")
    st.write(summary["Column Names"])

    st.write("### Data Types")
    st.write(summary["Data Types"])

    st.write("### Missing Values")
    st.write(summary["Missing Values"])

    st.write("### Duplicate Rows")
    st.write(summary["Duplicate Rows"])

    st.write("### Statistics")
    st.dataframe(summary["Statistics"])

    # ----------------------------------
    # Visualizations
    # ----------------------------------
    st.header("Visualizations")

    create_visualizations(df)

    if os.path.exists("charts/histogram.png"):
        st.image("charts/histogram.png")

    if os.path.exists("charts/heatmap.png"):
        st.image("charts/heatmap.png")

    if os.path.exists("charts/boxplot.png"):
        st.image("charts/boxplot.png")

    # ----------------------------------
    # Gemini AI Insights
    # ----------------------------------
    st.header("Gemini AI Insights")

    with st.spinner("Generating AI Insights..."):

        ai_response = generate_insights(summary)

    st.write(ai_response)
    # ----------------------------------
# Chat with Dataset (Future Enhancement)
# ----------------------------------
st.header("💬 Chat with Your Dataset")

question = st.text_input(
    "Ask any question about your dataset"
)

if st.button("Ask Gemini"):

    if question.strip():

        with st.spinner("Thinking..."):

            answer = chat_with_dataset(summary, question)

        st.success(answer)

    else:
        st.warning("Please enter a question.")

    # ----------------------------------
    # PDF Report
    # ----------------------------------
    st.header("Download Report")

    report_path = generate_report(summary, ai_response)

    with open(report_path, "rb") as pdf:

        st.download_button(
            label="Download PDF Report",
            data=pdf,
            file_name="EDA_Report.pdf",
            mime="application/pdf"
        )
        