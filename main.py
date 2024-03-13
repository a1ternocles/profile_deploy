import streamlit as st
import numpy as np
import os
import socket
import pandas as pd
import pickle

from st_on_hover_tabs import on_hover_tabs


st.set_page_config(
    layout="wide",
    page_title="Datavision",
    page_icon="logo_full.png",
    initial_sidebar_state="expanded"
)

st.markdown('<style>' + open('./style.css').read() + '</style>', unsafe_allow_html=True)


with st.sidebar:
    tabs = on_hover_tabs(tabName=['Home', 'Dashboard', 'ML'], 
                         iconName=['home', 'dashboard', 'search'], default_choice=0)
