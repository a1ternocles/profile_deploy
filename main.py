import streamlit as st
from streamlit_option_menu import option_menu
import streamlit.components.v1 as com
    

def load_pdf(filename):
    with open(filename, "rb") as file:
        pdf_content = file.read()
    return pdf_content

# 1. as sidebar menu
with st.sidebar:
    col1,col2,col3 = st.columns([1,6,1])
    
    with col2:
        st.image('Andres.png', width=100,)
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
            use_container_width=True

        )
    st.markdown("<div style='margin: 25px;' ></div>", unsafe_allow_html=True)

    selected = option_menu("Navigation", ["About Me",'Projects','Contact Me'],
        icons=['people','code','phone'], menu_icon="cast", default_index=1)
    # Define la URL de la imagen y el enlace

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
def aboutme():

    titulo_css = """
    <style>
    h1 {
        color: white; /* Color del texto */
        font-size: 30px; /* Tamaño de la fuente */
        font-weight: bold; /* Negrita */
        text-align: center; /* Alineación del texto */
        text-shadow: 2px 2px 4px #000000; /* Sombra del texto */
        margin-bottom: 30px; /* Margen inferior */
        padding: 30px; /* Espaciado interno */
        border-radius: 10px; /* Borde redondeado */
    }
    </style>
    """

# Mostrar el título con estilo CSS
    col1,col2,col3 = st.columns([1,6,1])
    
    with col2:
        st.image('name.png')

    col1, col2 = st.columns([1,1])

    with col1:
        st.markdown('''
                    ##### I'm a Data Engineer passionate about Database Management Systems (DBMS), data analysis, and Machine Learning. 
                    ##### Committed to continuous learning in Automations, Data Lake, Statistical Methods, and Cybersecurity.''' )
    with col2:

        com.iframe('https://lottie.host/embed/e68840a7-c28b-490f-9457-1750db8b52bc/koQHy36OjP.json', height=250)

    st.markdown("<div style='margin: 30 px;' ></div>", unsafe_allow_html=True)
    # Mostrar el título con estilo CSS
    
    st.title('🧠 Knowledge')


    col1,col2,col3,col4 = st.columns([1,1,1,1])

    with col1:
        com.iframe('https://lottie.host/embed/1f893cd9-1912-45e6-bd2c-6c4d435ef42e/3mSBlS40oV.json', width=125)
        st.markdown('''
        ![Python](https://img.shields.io/badge/Python-333333?style=flat&logo=python)
        ![LaTeX](https://img.shields.io/badge/LaTeX-333333?style=flat-square&logo=LaTeX&logoColor=white)
                    ''')
    
    with col2:
        com.iframe('https://lottie.host/embed/7a0ba435-814b-4ae0-b99c-c77fb9fd4550/cAWva9oadU.json', width=110)
        st.markdown('''
        ![Apache Spark](https://img.shields.io/badge/-Apache%20Spark-333333?style=flat&logo=apache-spark)
        ![PySpark](https://img.shields.io/badge/-PySpark-333333?style=flat&logo=apache-spark)
                    ''')
    
    with col3:
        com.iframe('https://lottie.host/embed/2146b27b-17e5-47af-993e-a3da16ba458f/TrSxeghbvl.json', width=110)
        st.markdown('''
        ![Pandas](https://img.shields.io/badge/-Pandas-333333?style=flat&logo=pandas)
        ![Numpy](https://img.shields.io/badge/-Numpy-333333?style=flat&logo=numpy)
        ![Matplotlib](https://img.shields.io/badge/-Matplotlib-333333?style=flat&logo=matplotlib)
        ![Seaborn](https://img.shields.io/badge/-Seaborn-333333?style=flat&logo=seaborn)
        ![Scikitlearn](https://img.shields.io/badge/-Scikitlearn-333333?style=flat&logo=scikitlearn)
        ![Wordcloud](https://img.shields.io/badge/-Wordcloud-333333?style=flat&logo=wordcloud)
        ![Streamlit](https://img.shields.io/badge/-Streamlit-333333?style=flat&logo=streamlit)
                    ''')
    
    with col4:
        com.iframe('https://lottie.host/embed/627ea233-3a10-4a33-84e6-163f069bd74e/nNzQd3thpX.json', width=110)
        st.markdown('''
        ![Jupyter Notebook](https://img.shields.io/badge/-Jupyter_Notebook-333333?style=flat&logo=jupyter)
        ![MySQL](https://img.shields.io/badge/-MySQL-333333?style=flat&logo=mysql)
        ![Microsoft Azure](https://img.shields.io/badge/-Microsoft%20Azure-333333?style=flat&logo=microsoft-azure)
        ![PowerBI](https://img.shields.io/badge/-PowerBI-333333?style=flat&logo=powerbi)
        ![Visual Studio Code](https://img.shields.io/badge/Visual_Studio_Code-333333?style=flat&logo=visual%20studio%20code&logoColor=white)
        ![Google Suite](https://img.shields.io/badge/-Google%20Suite-333333?style=flat&logo=google)
        ![Microsoft Office Suite](https://img.shields.io/badge/-Microsoft%20Office%20Suite-333333?style=flat&logo=microsoft)
        ![Looker Data Studio](https://img.shields.io/badge/-Looker%20Data%20Studio-333333?style=flat&logo=looker)
        ![Tableau](https://img.shields.io/badge/-Tableau-333333?style=flat&logo=tableau)
                    ''')
    
    st.markdown("<div style='margin: 75px;' ></div>", unsafe_allow_html=True)
    st.title(' 🆙 Experience')

    st.markdown("<div style='margin: 50px;' ></div>", unsafe_allow_html=True)

    col1,col2 = st.columns([1,1])
    
    with col1:

        com.iframe('https://lottie.host/embed/ad49855b-1b31-46b5-b3ba-de144172b980/UDQNP9jZrf.json', height=250)

    with col2:
        st.subheader('🦾 Data Engineering')
        st.markdown('''
        - __Design and creation__ of a smart download process using ![Microsoft Azure](https://img.shields.io/badge/-Microsoft%20Azure-333333?style=flat&logo=microsoft-azure)
                    __increasing 50%__ efectiveness and __reducing 20%__ usage of machine resources.
        - Creation of an __Automated connection structure__ between __local and cloud__. Allowing to work easily with new incoming data.
        - Tools Usage: ![Apache Spark](https://img.shields.io/badge/-Apache%20Spark-333333?style=flat&logo=apache-spark) ![Pandas](https://img.shields.io/badge/-Pandas-333333?style=flat&logo=pandas)
        ![Numpy](https://img.shields.io/badge/-Numpy-333333?style=flat&logo=numpy) ![Python](https://img.shields.io/badge/Python-333333?style=flat&logo=python) ![MySQL](https://img.shields.io/badge/-MySQL-333333?style=flat&logo=mysql) to ETL. 
         __Save Up to 70%__ of cloud storage by using __.parquet__ format''')

    st.markdown("<div style='margin: 50px;' ></div>", unsafe_allow_html=True)

    col1,col2 = st.columns([1,1])
    
    with col2:

        com.iframe('https://lottie.host/embed/61eaa909-466b-4f9a-a31d-956e8311da89/vK6VUUGwJ2.json', height=250)

    with col1:
        st.subheader('🛢 Data Base Manager')
        st.markdown('''
        - __Design and creation__ of a standardized company database, streamlining data management and 
            utilization.
        - Establishing database connections with multiple __low-cost tools__, resulting in a monthly cost reduction 
            of $500 US.
        - Leveraging SQL and No-SQL databases creatively, leading to a __75% annual increase__ in 
            company-client interaction and profit. ''')

    st.markdown("<div style='margin: 50px;' ></div>", unsafe_allow_html=True)
    col1,col2 = st.columns([1,1])
    
    with col1:
        st.markdown("<div style='margin: 30px;' ></div>", unsafe_allow_html=True)

        com.iframe('https://lottie.host/embed/6631453c-4392-4a1c-be7d-b420786cff3c/rWAVKmy9gq.json', height=250)

    with col2:
        st.subheader('📈 Data Analyst')
        st.markdown('''
        - Creation of __25+__ executive dashboard using ![Tableau](https://img.shields.io/badge/-Tableau-333333?style=flat&logo=tableau)
        & ![Looker Data Studio](https://img.shields.io/badge/-Looker%20Data%20Studio-333333?style=flat&logo=looker).
        - Creation and optimization of IT tools using ![Microsoft Office Suite](https://img.shields.io/badge/-Microsoft%20Office%20Suite-333333?style=flat&logo=microsoft) and ![Google Suite](https://img.shields.io/badge/-Google%20Suite-333333?style=flat&logo=google) for production 
            accounts. Exceeding __Performance__ and __Speed__ on production.
        - Supervising ___best practices methods__, __KPI’s__ and __organizational 
            development__ on a team of 2 - 3 people.
        - Tool automatization, allowing me to __save 80%__ of my work time and more than __30%__ of team 
            time ''')
def project():

    titulo_css = """
    <style>
    h1 {
        color: white; /* Color del texto */
        font-size: 30px; /* Tamaño de la fuente */
        font-weight: bold; /* Negrita */
        text-align: center; /* Alineación del texto */
        text-shadow: 2px 2px 4px #000000; /* Sombra del texto */
        margin-bottom: 30px; /* Margen inferior */
        padding: 30px; /* Espaciado interno */
        border-radius: 10px; /* Borde redondeado */
    }
    </style>
    """

# Mostrar el título con estilo CSS
    col1,col2,col3 = st.columns([1,6,1])
    
    with col2:
        st.image('projects.png')  

if selected == 'About Me':
    aboutme()
elif selected == 'Projects':
    project()
elif selected == 'Contact Me':
    contact()