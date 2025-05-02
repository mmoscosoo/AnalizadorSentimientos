import streamlit as st
from textblob import TextBlob
from googletrans import Translator

# Estilos generales con tema claro suave y minimalista
st.markdown("""
    <style>
    .stApp {
        background-color: #f4f4f9;
        color: #333333;
        font-family: 'Arial', sans-serif;
    }
    textarea, .stTextInput>div>div>input {
        background-color: #ffffff;
        color: #333333;
        border: 1px solid #cccccc;
    }
    </style>
""", unsafe_allow_html=True)

# Sidebar sin imágenes y con otro color
st.markdown("""
    <style>
    .css-1d391kg {
        background-color: #dceef2 !important;
    }
    .css-1v3fvcr, .css-1d391kg .sidebar-content {
        color: #005f73 !important;
    }
    </style>
""", unsafe_allow_html=True)

translator = Translator()

# Título y subtítulo diferentes
st.title("LENGUA EMOCIONAL")
st.subheader("Transforma tus palabras en datos sobre emociones y percepción")

# Sidebar sin imágenes
with st.sidebar:
    st.subheader("Indicadores emocionales")
    st.markdown("""
    <div style='color:#005f73'>
    <b>Polaridad:</b> Representa si el texto tiene un tono negativo (-1), neutro (0) o positivo (1).
    <br><br>
    <b>Subjetividad:</b> Señala si el contenido es objetivo (0) o subjetivo (1), útil para saber si se basa en hechos o emociones.
    </div>
    """, unsafe_allow_html=True)

# Área de análisis
with st.expander('Interpretar emociones a partir del texto'):
    text1 = st.text_area('Escribe algo (en inglés o español) para analizar su tono emocional:')
    if text1:
        translation = translator.translate(text1, src="auto", dest="en")
        trans_text = translation.text
        blob = TextBlob(trans_text)

        polarity = round(blob.sentiment.polarity, 2)
        subjectivity = round(blob.sentiment.subjectivity, 2)

        st.write('**Polaridad:**', polarity)
        st.write('**Subjetividad:**', subjectivity)

        if polarity >= 0.5:
            st.success("Mensaje con carga positiva.")
        elif polarity <= -0.5:
            st.error("Mensaje con carga negativa.")
        else:
            st.info("Mensaje con tono neutral.")

