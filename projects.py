import streamlit as st
from streamlit_option_menu import option_menu
import streamlit.components.v1 as com
import webbrowser


def latest_project():
    
    col1,col2,col3 = st.columns([1,1,1])

    with col1:
        st.markdown("<div style='margin: 120px;' ></div>", unsafe_allow_html=True)

        st.subheader('🧑🏻‍💻 Great Team')
        st.markdown("<div style='margin: 15px;' ></div>", unsafe_allow_html=True)

        st.markdown('''An excellent team that tackled the challenge of building a clean, automated, and analytical system in less than 6 weeks, showcasing exceptional commitment, outstanding technical skills, and extraordinary collaboration abilities.''')

        st.image('Presentacion.png', use_column_width=None)
    
    with col2:
         st.markdown("<div style='margin: 120px;' ></div>", unsafe_allow_html=True)

         st.subheader('🌐 Great Tech')
         st.markdown("<div style='margin: 15px;' ></div>", unsafe_allow_html=True)

         st.markdown('New, secure, and fast technologies that enabled the creation of a recommendation model, an analytical dashboard, and a website, all in one.')
         st.markdown("<div style='margin: 50px;' ></div>", unsafe_allow_html=True)

         st.image('Presentacion1.png', use_column_width=None)
         
    with col3:
         st.markdown("<div style='margin: 120px;' ></div>", unsafe_allow_html=True)

         st.subheader('📦 Great Product')
         st.markdown("<div style='margin: 15px;' ></div>", unsafe_allow_html=True)

         st.markdown("A product that meets the client's expectations, thus enabling the development and growth of a company. Understanding of customer needs, effective communication, and a commitment to delivering value-added solutions.")
         st.markdown("<div style='margin: 20px;' ></div>", unsafe_allow_html=True)

         st.image('arcolweb.png',use_column_width=None)
         st.markdown(f'[Arcol Data Solution Web Site]({"https://arcolsolutions.streamlit.app"})')

    st.markdown("<div style='margin: 75px;' ></div>", unsafe_allow_html=True)

    col1,col2,col3 = st.columns([1,9,1])
    with col2:
        st.video('https://www.youtube.com/watch?v=BA9xd8gic8I')

def business():
    

    col1,col2,col3 = st.columns([1,1,1])
    with col1:
        st.markdown("<div style='margin: 75px;' ></div>", unsafe_allow_html=True)
        st.image('collage1.png',width=250)
        st.markdown("<div style='margin: 15px;' ></div>", unsafe_allow_html=True)
        st.subheader('💼 Job Assesments')
        
        if st.button('Power Point Presentation!'):
            webbrowser.open('https://docs.google.com/presentation/d/1sFG5Vs5xQt27blU2d-7lPe0ABdNwefQwYjx6rxnpWoM/edit#slide=id.p')
        
        if st.button('Dashboard!'):
            webbrowser.open('https://lookerstudio.google.com/reporting/7eb6720e-ca57-4282-98c6-234d981da03a')
        
    with col2:
        st.markdown("<div style='margin: 75px;' ></div>", unsafe_allow_html=True)
        st.image('collage2.png',width=250)

    with col3:
        st.markdown("<div style='margin: 75px;' ></div>", unsafe_allow_html=True)
        st.image('collage3.png',width=250)

def future():
    st.markdown("<div style='margin: 120px;' ></div>", unsafe_allow_html=True)

    col1,col2 = st.columns([1,1])
    with col1:
        st.subheader('👾 My First Videogame')
        st.markdown(
        "As a technology enthusiast and video game fan, I aspire to learn how to create one myself to delve deeper into this realm. This journey not only satisfies my curiosity but also fuels my passion for exploring the intricate dynamics and creativity behind gaming."
        ,unsafe_allow_html=True)
    with col2:
        st.video('https://www.youtube.com/watch?v=QU1pPzEGrqw&t=33s')
    
    st.markdown("<div style='margin: 100 px;' ></div>", unsafe_allow_html=True)

    st.markdown("<div style='margin: 75px;' ></div>", unsafe_allow_html=True)

    col1,col2 = st.columns([1,1])
    with col2:
        st.subheader('🛡️ Cyber Security World')
        st.markdown("I aim to delve into the realm of cybersecurity to complement it with my skills as a data engineer. This fusion not only enhances my proficiency in safeguarding data but also expands my capabilities to address emerging cyber threats effectively.")
    with col1:
        st.video('https://www.youtube.com/watch?v=FGdiSJakIS4&list=PLQIXaoKWER84rsnx72tYwKDyz_isF69RR')

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

    col1,col2 = st.columns([1,1])
    with col2:
            st.markdown('''
	As a Data engineer and Data Analyst, my work involves designing efficient data pipelines and performing in-depth analysis to extract 	valuable insights.
	
	- Robust Architectures
	- Statistical Analysis
	- Data-driven
	- Decision-making
	''')
    with col1:

        com.iframe('https://lottie.host/embed/d7699c04-5784-4698-8e77-a15cd09f98e4/CdBnEDqZh6.json', height=250)

    # Mostrar el título con estilo CSS 
    st.markdown("<div style='margin: 100px;' ></div>", unsafe_allow_html=True)

    col1,col2,col3 = st.columns([1,1,1])
    with col1:
        st.markdown("<h2 style='text-align: center;'>Latest Project</h2>", unsafe_allow_html=True)

        com.iframe('https://lottie.host/embed/22d88acf-3335-473d-a956-34bb92e8d94e/aO1AjIBkda.json')

        st.markdown('### Arcol Data Solutions')
        st.markdown(''' A binational company with a serious focus on business. 
	                We concentrate on the opportunities and potential of your venture. 
	                In short periods of time and with exceptional quality, we propel your business to new heights.''')
        
        st.markdown("<div style='margin: 10 px;' ></div>", unsafe_allow_html=True)
        latest_btn = st.button('# 🚀 SoyHenry:  Arcol Data Solution', key='henry,') 

    with col2:
        st.markdown("<h2 style='text-align: center;'>Business</h2>", unsafe_allow_html=True)
        com.iframe('https://lottie.host/embed/a27508db-c51f-46f8-90f6-652255a78905/7QZWdVsBHd.json')

        st.markdown('### Relevant Projects')
        st.markdown(''' Academic and professional projects that I consider significant in the field of technology. 
		            Showcasing my dedication and passion for innovation and problem-solving in the ever-evolving landscape of technology.''')
        
        st.markdown("<div style='margin: 12px;' ></div>", unsafe_allow_html=True)
        other_btn = st.button('💻 More',key='other')

    with col3:
        st.markdown("<h2 style='text-align: center;'>New Things!</h2>", unsafe_allow_html=True)
        com.iframe('https://lottie.host/embed/fa19c371-ce3d-4024-aa3b-55f81ab2379e/QUZR5I7n1N.json')

        st.markdown('### Future Projects')
        st.markdown(''' Committed to learning and continual improvement, I aim to elevate my skills to new heights, fostering confidence and creativity.
                     Embracing lifelong learning, I strive to realize my full potential both __personally and professionally__.''')

        st.markdown("<div style='margin: 12px;' ></div>", unsafe_allow_html=True)

        future_btn = st.button('🧩 Click Here!', key='future')
    
    
    if latest_btn:
        latest_project()

    elif other_btn:
        business()
    
    elif future_btn:
        future()
    
    