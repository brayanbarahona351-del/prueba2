import streamlit as st
import time

# 1. FORZAR MODO CLARO Y ALTO CONTRASTE PARA LECTURA FÁCIL
st.set_page_config(page_title="Test AUDIT Completo", page_icon="🌱", layout="centered")

st.markdown("""
    <style>
    /* Forzar fondo blanco y texto negro */
    .stApp { background-color: white !important; }
    h1, h2, h3, p, span, label, div { color: #1a1a1a !important; }
    
    /* Diseño de las preguntas (Grandes y Legibles) */
    .pregunta-titulo {
        font-size: 20px;
        font-weight: bold;
        background-color: #f0f2f6;
        padding: 12px;
        border-radius: 10px;
        margin-top: 20px;
    }
    /* Espaciado para las opciones */
    div[role="radiogroup"] {
        padding: 10px 20px;
        margin-bottom: 10px;
    }
    </style>
    """, unsafe_allow_html=True)

# 2. ENCABEZADO
st.title("🛡️ Auto-Evaluación de Bienestar")
st.write("Responde las 10 preguntas con sinceridad. Tus respuestas son **100% privadas**.")

st.info("💡 **Recuerda:** 1 Trago = 1 Cerveza pequeña = 1 Copa de vino = 1 Shot de licor.")

# 3. FORMULARIO COMPLETO (10 PREGUNTAS)
with st.form("audit_completo"):
    
    st.markdown("<div class='pregunta-titulo'>Selecciona tu género:</div>", unsafe_allow_html=True)
    genero = st.radio("Dato necesario para el rango médico:", ["Hombre", "Mujer"], horizontal=True, label_visibility="collapsed")
    
    st.divider()

    # --- BLOQUE 1: FRECUENCIA ---
    st.markdown("<div class='pregunta-titulo'>1. ¿Con qué frecuencia bebes alcohol?</div>", unsafe_allow_html=True)
    p1 = st.radio("P1", ["Nunca", "1 vez al mes o menos", "2 a 4 veces al mes", "2 a 3 veces por semana", "4 o más veces por semana"], label_visibility="collapsed")

    st.markdown("<div class='pregunta-titulo'>2. En un día de consumo normal, ¿cuántos tragos tomas?</div>", unsafe_allow_html=True)
    p2 = st.radio("P2", ["1 o 2", "3 o 4", "5 o 6", "7 a 9", "10 o más"], label_visibility="collapsed")

    st.markdown("<div class='pregunta-titulo'>3. ¿Qué tan seguido tomas 5 o más tragos en una sola vez?</div>", unsafe_allow_html=True)
    p3 = st.radio("P3", ["Nunca", "Menos de una vez al mes", "Mensualmente", "Semanalmente", "A diario"], label_visibility="collapsed")

    # --- BLOQUE 2: COMPORTAMIENTO (Último año) ---
    st.markdown("### En el último año...")

    st.markdown("<div class='pregunta-titulo'>4. ¿Sentiste que no podías parar de beber una vez empezado?</div>", unsafe_allow_html=True)
    p4 = st.radio("P4", ["Nunca", "Menos de una vez al mes", "Mensualmente", "Semanalmente", "A diario"], label_visibility="collapsed")

    st.markdown("<div class='pregunta-titulo'>5. ¿Faltaste a tus tareas normales por haber bebido?</div>", unsafe_allow_html=True)
    p5 = st.radio("P5", ["Nunca", "Menos de una vez al mes", "Mensualmente", "Semanalmente", "A diario"], label_visibility="collapsed")

    st.markdown("<div class='pregunta-titulo'>6. ¿Necesitaste beber en ayunas tras una borrachera?</div>", unsafe_allow_html=True)
    p6 = st.radio("P6", ["Nunca", "Menos de una vez al mes", "Mensualmente", "Semanalmente", "A diario"], label_visibility="collapsed")

    st.markdown("<div class='pregunta-titulo'>7. ¿Sentiste culpa o remordimiento después de beber?</div>", unsafe_allow_html=True)
    p7 = st.radio("P7", ["Nunca", "Menos de una vez al mes", "Mensualmente", "Semanalmente", "A diario"], label_visibility="collapsed")

    st.markdown("<div class='pregunta-titulo'>8. ¿Has tenido lagunas mentales (no recordar nada)?</div>", unsafe_allow_html=True)
    p8 = st.radio("P8", ["Nunca", "Menos de una vez al mes", "Mensualmente", "Semanalmente", "A diario"], label_visibility="collapsed")

    # --- BLOQUE 3: CONSECUENCIAS ---
    st.markdown("<div class='pregunta-titulo'>9. ¿Tú o alguien más resultó herido por tu consumo?</div>", unsafe_allow_html=True)
    p9 = st.radio("P9", ["No", "Sí, pero no en el último año", "Sí, durante el último año"], label_visibility="collapsed")

    st.markdown("<div class='pregunta-titulo'>10. ¿Alguien se ha preocupado por tu forma de beber?</div>", unsafe_allow_html=True)
    p10 = st.radio("P10", ["No", "Sí, pero no en el último año", "Sí, durante el último año"], label_visibility="collapsed")

    st.divider()
    boton = st.form_submit_button("🚀 CALCULAR MI NIVEL DE RIESGO")

# 4. LÓGICA DE PUNTUACIÓN
if boton:
    score = 0
    # Preguntas 1 a 8 (0 a 4 puntos)
    score += ["Nunca", "1 vez al mes o menos", "2 a 4 veces al mes", "2 a 3 veces por semana", "4 o más veces por semana"].index(p1)
    score += ["1 o 2", "3 o 4", "5 o 6", "7 a 9", "10 o más"].index(p2)
    score += ["Nunca", "Menos de una vez al mes", "Mensualmente", "Semanalmente", "A diario"].index(p3)
    for r in [p4, p5, p6, p7, p8]:
        score += ["Nunca", "Menos de una vez al mes", "Mensualmente", "Semanalmente", "A diario"].index(r)
    
    # Preguntas 9 y 10 (0, 2 o 4 puntos)
    map_9_10 = {"No": 0, "Sí, pero no en el último año": 2, "Sí, durante el último año": 4}
    score += map_9_10[p9]
    score += map_9_10[p10]

    with st.spinner('Analizando...'):
        time.sleep(1)

    st.markdown(f"<h2 style='text-align: center;'>Puntaje Total: {score}</h2>", unsafe_allow_html=True)

    # Rangos según género
    r1, r2, r3 = (4, 14, 19) if genero == "Hombre" else (3, 12, 18)

    if score <= r1:
        st.balloons()
        st.success("✅ **Nivel I: Riesgo Bajo**. Tu consumo es saludable.")
    elif score <= r2:
        st.warning("⚠️ **Nivel II: Riesgo Medio**. Considera reducir tu consumo.")
    elif score <= r3:
        st.error("🚨 **Nivel III: Consumo Perjudicial**. Tu salud podría estar en riesgo.")
    else:
        st.snow()
        st.error("🆘 **Nivel IV: Posible Dependencia**. Se recomienda buscar ayuda profesional.")

    st.info("Nota: Este test es educativo. Si necesitas ayuda profesional, acude a tu centro de salud.")
