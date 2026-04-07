import streamlit as st
import time

# 1. CONFIGURACIÓN DE LA PÁGINA
st.set_page_config(page_title="Test de Salud y Bienestar", page_icon="🌱", layout="centered")

# Estilos personalizados para que se vea limpio y profesional
st.markdown("""
    <style>
    .stRadio > label {
        font-size: 1.2rem !important;
        font-weight: bold !important;
        color: #2E4053;
        padding-top: 10px;
    }
    .stAlert {
        border-radius: 10px;
    }
    div[role="radiogroup"] {
        background-color: #F8F9F9;
        padding: 15px;
        border-radius: 15px;
        border: 1px solid #EAECEE;
        margin-bottom: 20px;
    }
    </style>
    """, unsafe_allow_html=True)

# 2. ENCABEZADO
st.title("🛡️ Auto-Evaluación de Bienestar")
st.write("Responde estas preguntas de forma **anónima**. Los resultados son solo para tu conocimiento personal.")

# Guía visual rápida
st.info("💡 **Guía rápida:** 1 Trago = 1 Cerveza (330ml) = 1 Copa de vino = 1 Shot de licor.")

# 3. INICIO DEL FORMULARIO
with st.form("audit_form"):
    
    # Perfil básico para calcular el riesgo exacto
    genero = st.radio("Primero, selecciona tu género:", ["Hombre", "Mujer"], horizontal=True)
    
    st.markdown("---")
    st.header("📌 Parte 1: Hábitos Generales")

    # Pregunta 1
    p1 = st.radio(
        "1. ¿Con qué frecuencia bebes alcohol?",
        ["Nunca", "1 vez al mes o menos", "2 a 4 veces al mes", "2 a 3 veces por semana", "4 o más veces por semana"]
    )

    # Pregunta 2
    p2 = st.radio(
        "2. En un día de consumo normal, ¿cuántos tragos te tomas?",
        ["1 o 2", "3 o 4", "5 o 6", "7 a 9", "10 o más"]
    )

    # Pregunta 3
    p3 = st.radio(
        "3. ¿Qué tan seguido tomas 5 o más tragos en una sola ocasión?",
        ["Nunca", "Menos de una vez al mes", "Mensualmente", "Semanalmente", "A diario o casi a diario"]
    )

    st.markdown("---")
    st.header("📌 Parte 2: En el último año...")

    p4 = st.radio("4. ¿Sentiste que no podías parar de beber una vez que empezaste?", 
                  ["Nunca", "Menos de una vez al mes", "Mensualmente", "Semanalmente", "A diario"])
    
    p5 = st.radio("5. ¿Faltaste a tus responsabilidades (trabajo/estudio) por beber?", 
                  ["Nunca", "Menos de una vez al mes", "Mensualmente", "Semanalmente", "A diario"])
    
    p6 = st.radio("6. ¿Necesitaste beber en ayunas para recuperarte de una borrachera?", 
                  ["Nunca", "Menos de una vez al mes", "Mensualmente", "Semanalmente", "A diario"])
    
    p7 = st.radio("7. ¿Sentiste remordimiento o culpa después de beber?", 
                  ["Nunca", "Menos de una vez al mes", "Mensualmente", "Semanalmente", "A diario"])
    
    p8 = st.radio("8. ¿Has tenido lagunas mentales (no recordar nada) por la bebida?", 
                  ["Nunca", "Menos de una vez al mes", "Mensualmente", "Semanalmente", "A diario"])

    st.markdown("---")
    st.header("📌 Parte 3: Consecuencias")

    p9 = st.radio("9. ¿Tú o alguien más resultó herido porque habías bebido?", 
                  ["No", "Sí, pero no en el último año", "Sí, durante el último año"])
    
    p10 = st.radio("10. ¿Algún familiar o médico se ha preocupado por tu forma de beber?", 
                   ["No", "Sí, pero no en el último año", "Sí, durante el último año"])

    # BOTÓN DE ENVÍO
    boton_resultado = st.form_submit_button("🚀 VER MI RESULTADO FINAL")

# 4. LÓGICA DE RESULTADOS
if boton_resultado:
    # Mapeo de puntos (Índices 0-4)
    puntos = 0
    
    # P1 a P8 (Suman según el orden de la lista 0,1,2,3,4)
    opciones_std = ["Nunca", "1 vez al mes o menos", "2 a 4 veces al mes", "2 a 3 veces por semana", "4 o más veces por semana",
                    "1 o 2", "3 o 4", "5 o 6", "7 a 9", "10 o más",
                    "Menos de una vez al mes", "Mensualmente", "Semanalmente", "A diario", "A diario o casi a diario"]
    
    puntos += ["Nunca", "1 vez al mes o menos", "2 a 4 veces al mes", "2 a 3 veces por semana", "4 o más veces por semana"].index(p1)
    puntos += ["1 o 2", "3 o 4", "5 o 6", "7 a 9", "10 o más"].index(p2)
    puntos += ["Nunca", "Menos de una vez al mes", "Mensualmente", "Semanalmente", "A diario o casi a diario"].index(p3)
    
    # Preguntas 4 a 8
    for r in [p4, p5, p6, p7, p8]:
        puntos += ["Nunca", "Menos de una vez al mes", "Mensualmente", "Semanalmente", "A diario"].index(r)
    
    # Preguntas 9 y 10 (Suman 0, 2 o 4)
    map_especial = {"No": 0, "Sí, pero no en el último año": 2, "Sí, durante el último año": 4}
    puntos += map_especial[p9]
    puntos += map_especial[p10]

    # Efecto de carga
    with st.spinner('Analizando tus respuestas...'):
        time.sleep(1.2)

    # Mostrar puntaje
    st.divider()
    st.markdown(f"<h2 style='text-align: center;'>Puntaje Total: {puntos}</h2>", unsafe_allow_html=True)

    # Interpretación oficial basada en la tabla de la OMS
    r_bajo = 4 if genero == "Hombre" else 3
    r_riesgo = 14 if genero == "Hombre" else 12
    r_perjudicial = 19 if genero == "Hombre" else 18

    if puntos <= r_bajo:
        st.balloons()
        st.success("✅ **NIVEL I: RIESGO BAJO**\n\nTu consumo se mantiene en niveles saludables. ¡Sigue cuidándote!")
    elif puntos <= r_riesgo:
        st.warning("⚠️ **NIVEL II: CONSUMO DE RIESGO**\n\nEstás en un nivel donde el alcohol podría empezar a afectar tu salud. Se recomienda reducir la cantidad o frecuencia.")
    elif puntos <= r_perjudicial:
        st.error("🚨 **NIVEL III: CONSUMO PERJUDICIAL**\n\nTu patrón de consumo ya está causando daños. Sería muy valioso buscar orientación profesional o hablar con un experto en salud.")
    else:
        st.snow()
        st.error("🆘 **NIVEL IV: POSIBLE DEPENDENCIA**\n\nLos resultados sugieren una posible dependencia. Te animamos a buscar apoyo especializado lo antes posible para mejorar tu calidad de vida.")

    st.info("🔍 *Nota: Este test es una herramienta de orientación educativa, no reemplaza una consulta médica profesional.*")
