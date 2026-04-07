import streamlit as st
import time

# Configuración de la página
st.set_page_config(page_title="Test de Salud y Bienestar", page_icon="🌱")

# Estilo visual mejorado
st.markdown("""
    <style>
    .main { background-color: #f8f9fa; }
    .stRadio > label { font-weight: bold; font-size: 18px; }
    </style>
    """, unsafe_allow_html=True)

st.title("🌱 ¿Cómo es tu relación con el alcohol?")
st.write("Responde estas 10 preguntas rápidas para conocer tu nivel de riesgo. **Es totalmente anónimo.**")

# --- Explicación Sencilla de 'Un Trago' ---
st.warning("⚠️ **Dato clave:** 1 Trago = 1 Cerveza pequeña = 1 Copa de vino = 1 Shot de tequila.")

with st.form("audit_facil"):
    # Sección de Perfil
    col1, col2 = st.columns(2)
    with col1:
        genero = st.radio("Soy:", ["Hombre", "Mujer"])
    
    st.divider()
    st.subheader("📌 Hábitos Generales")

    p1 = st.select_slider("1. ¿Qué tan seguido bebes?", 
                         options=["Nunca", "Casi nunca", "2 a 4 veces al mes", "2 a 3 veces por semana", "Casi todos los días"])
    
    p2 = st.select_slider("2. En un día de fiesta, ¿cuántos tragos te tomas?", 
                         options=["1 o 2", "3 o 4", "5 o 6", "7 a 9", "10 o más"])
    
    p3 = st.select_slider("3. ¿Qué tan seguido tomas más de 5 tragos en una sola vez?", 
                         options=["Nunca", "Casi nunca", "Una vez al mes", "Cada semana", "A diario"])
    
    st.divider()
    st.subheader("📌 Situaciones del último año")
    
    p4 = st.radio("4. ¿Sentiste que no podías parar de beber una vez que empezaste?", ["Nunca", "Casi nunca", "A veces", "Seguido", "Siempre"])
    p5 = st.radio("5. ¿Faltaste al trabajo o estudio por haber bebido?", ["Nunca", "Casi nunca", "A veces", "Seguido", "Siempre"])
    p6 = st.radio("6. ¿Necesitaste beber apenas te despertaste para 'curar' la resaca?", ["Nunca", "Casi nunca", "A veces", "Seguido", "Siempre"])
    p7 = st.radio("7. ¿Sentiste culpa después de haber bebido?", ["Nunca", "Casi nunca", "A veces", "Seguido", "Siempre"])
    p8 = st.radio("8. ¿Se te 'borró la cinta' (no recordabas nada) por beber?", ["Nunca", "Casi nunca", "A veces", "Seguido", "Siempre"])
    
    st.divider()
    st.subheader("📌 Consecuencias")
    p9 = st.radio("9. ¿Alguien salió herido (tú u otro) porque habías bebido?", ["No", "Sí, pero hace tiempo", "Sí, este último año"])
    p10 = st.radio("10. ¿Algún amigo o médico te ha dicho que deberías bajarle al alcohol?", ["No", "Sí, pero hace tiempo", "Sí, este último año"])

    enviar = st.form_submit_button("⭐ OBTENER MI RESULTADO")

# Lógica de Puntos
if enviar:
    puntos = 0
    # Mapeo simple de 0 a 4
    lista_comun = ["Nunca", "Casi nunca", "2 a 4 veces al mes", "2 a 3 veces por semana", "Casi todos los días", 
                   "1 o 2", "3 o 4", "5 o 6", "7 a 9", "10 o más",
                   "Una vez al mes", "Cada semana", "A diario", "A diario o casi diario",
                   "A veces", "Seguido", "Siempre"]
    
    # (El cálculo de puntos sigue la misma lógica oficial interna)
    puntos += ["Nunca", "Casi nunca", "2 a 4 veces al mes", "2 a 3 veces por semana", "Casi todos los días"].index(p1)
    puntos += ["1 o 2", "3 o 4", "5 o 6", "7 a 9", "10 o más"].index(p2)
    puntos += ["Nunca", "Casi nunca", "Una vez al mes", "Cada semana", "A diario"].index(p3)
    for r in [p4, p5, p6, p7, p8]:
        puntos += ["Nunca", "Casi nunca", "A veces", "Seguido", "Siempre"].index(r)
    
    map_especial = {"No": 0, "Sí, pero hace tiempo": 2, "Sí, este último año": 4}
    puntos += map_especial[p9]
    puntos += map_especial[p10]

    with st.spinner('Calculando...'):
        time.sleep(1)

    # Resultados entendibles
    st.markdown("---")
    st.header(f"Tu resultado: {puntos} puntos")

    # Ajuste de rangos
    r_bajo = 4 if genero == "Hombre" else 3
    r_medio = 14 if genero == "Hombre" else 12

    if puntos <= r_bajo:
        st.balloons()
        st.success("✅ **¡Todo bien!** Tu consumo es de bajo riesgo. Sigue disfrutando con moderación.")
    elif puntos <= r_medio:
        st.warning("⚠️ **¡Cuidado!** Estás en un nivel de riesgo. Podrías empezar a tener problemas de salud pronto. Sería bueno bajarle un poco.")
    else:
        st.snow()
        st.error("🚨 **¡Alerta!** Tu nivel de consumo es muy alto y puede ser peligroso. Te recomendamos buscar ayuda profesional o hablar con alguien de confianza.")

    st.info("ℹ️ *Recuerda: Este test es una guía educativa, no un diagnóstico médico.*")
