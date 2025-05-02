import streamlit as st
from textblob import TextBlob
from googletrans import Translator
from streamlit_lottie import st_lottie
import json

# Estilos personalizados
st.markdown("""
    <style>
    .stApp {
        background-color: #1e1e1e;
        color: #dce2e8;
        font-family: 'Segoe UI', sans-serif;
    }

    textarea, .stTextInput>div>div>input {
        background-color: #2c2f33;
        color: #dce2e8;
        border: 1px solid #3a3f47;
    }

    .stImage {
        display: block;
        margin-left: auto;
        margin-right: auto;
    }
    </style>
""", unsafe_allow_html=True)

# Sidebar estilo
sidebar_css = """
    <style>
    .css-1d391kg {
        background-color: #0e1117 !important;
    }

    .css-1v3fvcr, .css-1d391kg .sidebar-content {
        color: #50fa7b !important;
    }
    </style>
"""
st.markdown(sidebar_css, unsafe_allow_html=True)

translator = Translator()

# Título
st.title('🔍 LENS: Language Emotion & Nuance Scanner')
st.caption("Analiza el tono emocional y la perspectiva de cualquier texto.")

with st.sidebar:
    st.image('lens_logo.png', use_container_width=True)  # Reemplaza con un logo más neutro
    st.subheader("¿Qué mide LENS?")
    st.markdown("""
    <div style='color:#50fa7b'>
    <b>Polaridad:</b> Evalúa el tono emocional del texto, desde negativo (-1) a positivo (1).<br><br>
    <b>Subjetividad:</b> Indica cuán opinativo es el texto (0 = objetivo, 1 = subjetivo).
    </div>
    """, unsafe_allow_html=True)

with st.expander("📘 Analiza tu texto:"):
    text1 = st.text_area("Introduce un texto para evaluar su tono emocional (preferiblemente en inglés):")

    if text1:
        translation = translator.translate(text1, src="es", dest="en")
        trans_text = translation.text
        blob = TextBlob(trans_text)

        polarity = round(blob.sentiment.polarity, 2)
        subjectivity = round(blob.sentiment.subjectivity, 2)

        st.markdown("### 🧠 Resultados del análisis")
        st.write('**Polaridad:**', polarity)
        st.write('**Subjetividad:**', subjectivity)

        if polarity >= 0.5:
            st.success("🔵 El texto tiene una carga emocional positiva.")
            with open('positive.json') as source:
                animation = json.load(source)
                st_lottie(animation, width=350)
        elif polarity <= -0.5:
            st.error("🔴 El texto expresa un sentimiento negativo.")
            with open('negative.json') as source:
                animation = json.load(source)
                st_lottie(animation, width=350)
        else:
            st.info("🟡 El texto se percibe como neutral.")
            with open('neutral.json') as source:
                animation = json.load(source)
                st_lottie(animation, width=350)
