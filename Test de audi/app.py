import streamlit as st
import time

# 1. FORZAR MODO CLARO Y ALTO CONTRASTE
st.set_page_config(page_title="Test de Bienestar", page_icon="🌱", layout="centered")

st.markdown("""
    <style>
    /* Forzar fondo blanco y texto negro en toda la app */
    .stApp {
        background-color: white !important;
    }
    h1, h2, h3, p, span, label {
        color: #1a1a1a !important; /* Negro casi puro */
    }
    /* Hacer las preguntas más grandes y legibles */
    .stRadio > label {
        font-size: 22px !important;
        font-weight: bold !important;
        background-color: #f0f2f6;
        padding: 10px;
        border-radius: 8px;
        display: block;
    }
    /* Estilo para las opciones */
    div[role="radiogroup"] {
        padding: 15px;
        border: 2px solid #e0e0e0;
        border-radius: 10px;
        margin-bottom: 25px;
    }
    </style>
    """, unsafe_allow_html=True)

# 2. ENCABEZADO CLARO
st.title("🛡️ Auto-Evaluación de Bienestar")
st.markdown("### Responde de forma anónima. Tus resultados son privados.")

st.info("💡 **1 Trago =** 1 Cerveza (330ml) = 1 Copa de vino = 1 Shot de licor.")

with st.form("audit_form_v2"):
    
    # Género con etiqueta visible
    st.markdown("### Selecciona tu género:")
    genero = st.radio("Este dato ajusta el resultado médico:", ["Hombre", "Mujer"], label_visibility="collapsed")
    
    st.markdown("---")
    
    # PREGUNTA 1
    st.markdown("### 1. ¿Con qué frecuencia bebes alcohol?")
    p1 = st.radio("", ["Nunca", "1 vez al mes o menos", "2 a 4 veces al mes", "2 a 3 veces por semana", "4 o más veces por semana"], key="q1", label_visibility="collapsed")

    # PREGUNTA 2
    st.markdown("### 2. En un día normal, ¿cuántos tragos te tomas?")
    p2 = st.radio("", ["1 o 2", "3 o 4", "5 o 6", "7 a 9", "10 o más"], key="q2", label_visibility="collapsed")

    # PREGUNTA 3
    st.markdown("### 3. ¿Qué tan seguido tomas 5 o más tragos en una vez?")
    p3 = st.radio("", ["Nunca", "Menos de una vez al mes", "Mensualmente", "Semanalmente", "A diario"], key="q3", label_visibility="collapsed")

    # (Puedes seguir añadiendo el resto de preguntas con este mismo formato st.markdown + st.radio)

    st.markdown("---")
    boton_resultado = st.form_submit_button("🚀 VER MI RESULTADO")

if boton_resultado:
    st.balloons()
    st.success("¡Cálculo completado! (Aquí aparecería tu resultado)")
