import streamlit as st
import pandas as pd
from package.desc_stats import all
st.sidebar.success('Select a page above.')

single_data = all.single_data()
single_data
