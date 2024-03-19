import streamlit as st
from streamlit_option_menu import option_menu
import streamlit.components.v1 as com

def maincss(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>",unsafe_allow_html=True)

def contact():

        # Estilos CSS
    st.markdown(
            """
            <style>
            .contact-container {
                max-width: 600px;
                margin: auto;
                padding: 20px;
                background-color: #f9f9f9;
                border-radius: 10px;
                box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
            }
            .contact-header {
                font-size: 24px;
                font-weight: bold;
                margin-bottom: 20px;
            }
            .contact-input {
                width: 100%;
                padding: 10px;
                margin-bottom: 15px;
                border: 1px solid #ccc;
                border-radius: 5px;
            }
            .contact-button {
                background-color: #007bff;
                color: #fff;
                border: none;
                border-radius: 5px;
                padding: 10px 20px;
                cursor: pointer;
            }
            .contact-button:hover {
                background-color: #0056b3;
            }
            </style>
            """,
            unsafe_allow_html=True
        )
        # Sección de Información de Contacto
        #st.markdown('<div class="contact-container">', unsafe_allow_html=True)        
    
    col1,col2,col3 = st.columns([1,4,1])
    
    with col2:
            st.image('lets.png',use_column_width=None)

    col1,col2,col3 = st.columns([1,2,1])
    
    with col2:
         
        contact_form = '''
        <form action="https://formsubmit.co/anmruizto@gmail.com" method="POST">
            <input type="text" name="name" required placeholder = 'Your Name'>
            <input type="email" name="email" required placeholder = 'Your Email'>
            <textarea name="message" placeholder="Here your Message"></textarea>
            <input type="hidden" name="_captcha" value="false">
            <button type="submit" class = button>Send</button>
        </form>'''
        st.markdown(contact_form, unsafe_allow_html=True)
        maincss("main.css")
        st.markdown('</div>', unsafe_allow_html=True)   
