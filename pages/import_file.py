import pandas as pd
from package import *
import streamlit as st

file_path = "raw_data/raw_data.xlsx"

# Read data from Excel
cars = pd.read_excel(file_path, header=None).squeeze()

# Calculate statistics
desc = all.descriptive_stats(cars)
desc1 = pd.DataFrame([desc]).T


col1, col2 = st.columns(2)

with col1:
    st.write(cars)
    
with col2:
    st.write(desc1)
