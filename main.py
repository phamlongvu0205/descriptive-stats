import streamlit as st
from pages import single_data

# --- PAGE SETUP ---
st.set_page_config(layout='wide', initial_sidebar_state='expanded', )

single_data = st.Page(
    page = "pages/single_data.py",
    title = "Single Data",
    default=True
)

multiple_data = st.Page(
    page = "pages/multiple_data.py",
    title = "Multiple Data"
)

import_file = st.Page(
    page = "pages/import_file.py",
    title = "Import File"
)

import_file_app = st.Page(
    page = "pages/import_file_app.py",
    title = "Import File App"
)

# --- NAVIGATION SETUP [WITHOUT SECTION] ---
# pg = st.navigation(pages=[import_file,input_data])

# --- NAVIGATION SETUP [WITH SECTION]
pg = st.navigation(
    {
        "Input Data": [single_data, multiple_data],
        "Import Data": [import_file, import_file_app],
        
    }
    
)

# --- RUN NAVIGATION ---
pg.run()
