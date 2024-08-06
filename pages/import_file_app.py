import pandas as pd
from package.desc_stats import all
import streamlit as st
from io import BytesIO

# Upload file
uploaded_file = st.file_uploader("Upload file", type=["xlsx", "csv"])

# Initialize df as None
df = None

if uploaded_file:
    try:
        # Read the file based on its extension
        if uploaded_file.name.endswith(".xlsx"):
            # Attempt to read as Excel
            try:
                df = pd.read_excel(uploaded_file, engine='openpyxl', header=None)  # Specify the engine for Excel files
            except Exception as e:
                st.error(f"Excel file reading error: {e}")
        elif uploaded_file.name.endswith(".csv"):
            # Attempt to read as CSV
            try:
                df = pd.read_csv(uploaded_file, header=None)  # Read CSV file
            except Exception as e:
                st.error(f"CSV file reading error: {e}")
        else:
            st.error("Unsupported file format")
    except Exception as e:
        st.error(f"General error: {e}")

# Check if df is not None before proceeding
if df is not None:
    data_dict = df.squeeze().to_dict()  # Convert the single column DataFrame to a dictionary
    data_df = pd.DataFrame(list(data_dict.values()))
    desc1 = pd.DataFrame([all.descriptive_stats(data_df[0])]).T

    col1, col2 = st.columns(2)
    with col1:
        st.write(df)
    
    with col2:
        st.write(desc1)
else:
    st.warning("Please upload a file to see the data and statistics.")
