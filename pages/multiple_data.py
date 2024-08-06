import streamlit as st
import pandas as pd
from package.desc_stats import all
st.sidebar.success('Select a page above.')

multiple_data = all.multiple_data()
multiple_data
