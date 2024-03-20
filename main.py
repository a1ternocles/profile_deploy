import streamlit as st
from streamlit_option_menu import option_menu
import streamlit.components.v1 as com
import projects
import about_me
import contact
from selenium import webdriver
import time



st.set_page_config(layout="wide")
def load_pdf(filename):
    with open(filename, "rb") as file:
        pdf_content = file.read()
    return pdf_content

# 1. as sidebar menu
with st.sidebar:
    col1,col2,col3 = st.columns([1,2,1])
    with col2:
        st.image('Andres.png', width=125)

    col1,col2,col3 = st.columns([1,3,1])
    with col2:
        st.markdown('''
        * Spanish: Native
        * English: Advance
        * Portugues: Mid ''')

        pdf_file ='Andres Ruiz Resume DE.pdf'
        pdf_contents = load_pdf(pdf_file)

        st.download_button(
            label= 'My Resume',
            data= pdf_contents,
            file_name= pdf_file,
            mime='application/pdf',
            use_container_width=True,
            type='primary'

        )
    
    col1,col2,col3,col4 = st.columns([1,6,6,1])
    with col2:
        if st.button('🐈‍⬛ GitHub',type='secondary'):
            
            driver = webdriver.Chrome()
            driver.get('https://github.com/a1ternocles')
    with col3:
        if st.button('🖥️ Linkedin',type='secondary'):
            
            driver = webdriver.Chrome()
            driver.get('https://www.linkedin.com/in/andresruiz94/')

    st.markdown("<div style='margin: 25px;' ></div>", unsafe_allow_html=True)

    selected = option_menu("Navigation", ["About Me",'Projects','Contact Me'],
        icons=['people','code','phone'], menu_icon="cast", default_index=0)
    # Define la URL de la imagen y el enlace

if selected == 'About Me':
    about_me.aboutme()
elif selected == 'Projects':
    projects.project()
elif selected == 'Contact Me':
    contact.contact()