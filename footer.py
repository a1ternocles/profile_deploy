import streamlit as st        
# Agrega HTML personalizado para el footer
def footer():
    st.markdown(
                """
                <style>
                    .footer {
                        display: flex;
                        justify-content: space-between;
                        align-items: center;
                        padding: 10px;
                        background-color: #f1f1f1; /* Color de fondo del footer */
                        position: fixed;
                        bottom: 0;
                        width: 100%;
                    }
                    .column {
                        display: flex;
                        align-items: center;
                    }
                    .column img {
                        width: 30px; /* Ajusta el tamaño de las imágenes según sea necesario */
                        margin-right: 10px;
                    }
                </style>
                """,
                unsafe_allow_html=True
            )

        # Contenido del footer en formato HTML y CSS
    footer = """
                <style>
                    .footer {
                        position: fixed;
                        bottom: 0;
                        left: 0;
                        width: 100%;
                        background-color: #f1f1f1;
                        text-align: center;
                        padding: 10px;
                    }
                </style>
                <div class="footer">
                    <p>© 2024 Andres Ruiz. All rights reserved.</p>
                </div>
            """

            # Mostrar el contenido del footer en la aplicación
    st.markdown(footer, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)