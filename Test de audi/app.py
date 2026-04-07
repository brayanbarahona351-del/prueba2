import streamlit as st
import time
import base64

# 1. FUNCIÓN PARA PONER IMAGEN DE FONDO CON TRANSPARENCIA
def add_bg_from_local(image_file):
    with open(image_file, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read())
    st.markdown(
    f"""
    <style>
    .stApp {{
        background-image: url("data:image/png;base64,{encoded_string.decode()}");
        background-attachment: fixed;
        background-size: 60%; /* Tamaño del logo */
        background-repeat: no-repeat;
        background-position: center;
        background-color: rgba(255, 255, 255, 0.85); /* Capa blanca para transparencia */
        background-blend-mode: overlay;
    }}
    
    /* Forzar texto negro para que resalte sobre el fondo */
    h1, h2, h3, p, span, label, div {{ 
        color: #000000 !important; 
        font-weight: 500;
    }}

    .pregunta-titulo {{
        background-color: rgba(240, 242, 246, 0.9); /* Fondo semi-transparente para la pregunta */
        padding: 12px;
        border-radius: 10px;
        margin-top: 20px;
        font-weight: bold;
    }}
    </style>
    """,
    unsafe_allow_html=True
    )

# 2. CONFIGURACIÓN E INYECCIÓN DE FONDO
st.set_page_config(page_title="Test AUDIT - D.S.P. Honduras", page_icon="🛡️")

# --- ¡IMPORTANTE! --- 
# Asegúrate de que tu imagen se llame 'logo.png' o cambia el nombre aquí abajo
try:
    add_bg_from_local('logo.png') 
except FileNotFoundError:
    st.error("⚠️ No se encontró el archivo 'logo.png'. Por favor, súbelo a la carpeta del proyecto.")

# 3. CONTENIDO DEL TEST (10 PREGUNTAS)
st.title("🛡️ Dirección de Sanidad Policial")
st.subheader("Auto-Evaluación de Bienestar (AUDIT)")
st.write("Herramienta de concientización sobre el consumo de alcohol.")

with st.form("audit_dsp"):
    st.markdown("<div class='pregunta-titulo'>Selecciona tu género:</div>", unsafe_allow_html=True)
    genero = st.radio("", ["Hombre", "Mujer"], horizontal=True, label_visibility="collapsed")

    # Preguntas 1-3
    st.markdown("<div class='pregunta-titulo'>1. ¿Con qué frecuencia bebe alcohol?</div>", unsafe_allow_html=True)
    p1 = st.radio("q1", ["Nunca", "1 vez al mes o menos", "2 a 4 al mes", "2 a 3 por semana", "4 o más por semana"], label_visibility="collapsed")

    st.markdown("<div class='pregunta-titulo'>2. En un día normal, ¿cuántos tragos toma?</div>", unsafe_allow_html=True)
    p2 = st.radio("q2", ["1 o 2", "3 o 4", "5 o 6", "7 a 9", "10 o más"], label_visibility="collapsed")

    st.markdown("<div class='pregunta-titulo'>3. ¿Con qué frecuencia bebe 5 o más tragos en una vez?</div>", unsafe_allow_html=True)
    p3 = st.radio("q3", ["Nunca", "Menos de una vez al mes", "Mensualmente", "Semanalmente", "A diario"], label_visibility="collapsed")

    # Preguntas 4-8 (Simplificadas para el ejemplo, mantén la lógica de puntos anterior)
    st.markdown("### Situaciones del último año")
    preguntas_restantes = [
        "4. ¿No pudo parar de beber una vez empezado?",
        "5. ¿Incumplió responsabilidades por beber?",
        "6. ¿Necesitó beber en ayunas tras una borrachera?",
        "7. ¿Sintió remordimiento o culpa?",
        "8. ¿No recordó lo sucedido por beber?"
    ]
    respuestas = []
    for i, texto in enumerate(preguntas_restantes):
        st.markdown(f"<div class='pregunta-titulo'>{texto}</div>", unsafe_allow_html=True)
        respuestas.append(st.radio(f"q{i+4}", ["Nunca", "Menos de una vez al mes", "Mensualmente", "Semanalmente", "A diario"], label_visibility="collapsed"))

    # Preguntas 9-10
    st.markdown("<div class='pregunta-titulo'>9. ¿Alguien resultó herido por su consumo?</div>", unsafe_allow_html=True)
    p9 = st.radio("q9", ["No", "Sí, pero no este año", "Sí, este año"], label_visibility="collapsed")

    st.markdown("<div class='pregunta-titulo'>10. ¿Alguien se ha preocupado por su forma de beber?</div>", unsafe_allow_html=True)
    p10 = st.radio("q10", ["No", "Sí, pero no este año", "Sí, este año"], label_visibility="collapsed")

    if st.form_submit_button("🚀 OBTENER RESULTADO"):
        # (Aquí va la lógica de suma de puntos que ya tienes)
        st.balloons()
        st.success("Test finalizado con éxito.")
