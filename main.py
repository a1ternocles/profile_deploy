import streamlit as st
import numpy as np
from st_on_hover_tabs import on_hover_tabs


st.set_page_config(
    layout="wide",
    page_title="Andres Ruiz",
    initial_sidebar_state="expanded"
)



with st.sidebar:
    tabs = on_hover_tabs(tabName=['Home', 'Dashboard', 'ML'], 
                         iconName=['home', 'dashboard', 'search'], default_choice=0)
    