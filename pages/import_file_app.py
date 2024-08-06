import pandas as pd
from package import all
import streamlit as st
from io import BytesIO

# Upload file
uploaded_file = st.file_uploader("Upload file", type=["xlsx", "csv"])

if uploaded_file:
    try:
        # Read the file based on its extension
        if uploaded_file.name.endswith(".xlsx"):
            # Attempt to read as Excel
            try:
                df = pd.read_excel(uploaded_file, engine='openpyxl', header=None)  # Specify the engine for Excel files
            except Exception as e:
                st.error(f"Excel file reading error: {e}")
                df = None
        elif uploaded_file.name.endswith(".csv"):
            # Attempt to read as CSV
            try:
                df = pd.read_csv(uploaded_file, header=None)  # Read CSV file
            except Exception as e:
                st.error(f"CSV file reading error: {e}")
                df = None
        else:
            st.error("Unsupported file format")
            df = None

        # Display the DataFrame if successfully read
        if df is not None:
            st.write('')
    except Exception as e:
        st.error(f"General error: {e}")

data_dict = df.squeeze().to_dict()  # Convert the single column DataFrame to a dictionary

data_df = pd.DataFrame(list(data_dict.values()))
# data_df

desc1 = pd.DataFrame([all.descriptive_stats(data_df[0])]).T

col1, col2 = st.columns(2)
with col1:
    st.write(df)
    
with col2:
    st.write(desc1)
