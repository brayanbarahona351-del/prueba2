import streamlit as st
import time

# 1. Configuración visual de la pestaña
st.set_page_config(page_title="Test AUDIT - Concientización", page_icon="🍷", layout="centered")

# 2. Título y Introducción
st.title("📊 Auto-Evaluación: Hábitos de Consumo")
st.markdown("""
Esta herramienta es **anónima y privada**. Utilízala para reflexionar sobre tu salud.
*Responde basándote en tu consumo del último año.*
""")

# 3. Definición de equivalencias (Importante para que el usuario no se confunda)
with st.expander("❓ ¿Qué se considera 'un trago'?", expanded=False):
    st.info("""
    **Un trago estándar equivale a:**
    - 🍺 Una cerveza (330ml / 12oz)
    - 🍷 Una copa de vino (150ml / 5oz)
    - 🥃 Un trago corto de licor (40ml / 1.5oz)
    """)

# 4. Inicio del Formulario
with st.form("test_audit"):
    col1, col2 = st.columns(2)
    with col1:
        genero = st.radio("Selecciona tu género:", ["Hombre", "Mujer"])
    with col2:
        st.caption("Nota: El género ajusta los rangos de riesgo según el manual OMS.")

    st.divider()

    # Preguntas 1 a 8 (Escala 0 a 4 puntos)
    # Usamos select_slider para que sea más interactivo que un simple botón
    p1 = st.select_slider("1. ¿Con qué frecuencia bebes alcohol?", 
                         options=["Nunca", "1 o menos al mes", "2 a 4 al mes", "2 a 3 por semana", "4 o más por semana"])
    
    p2 = st.select_slider("2. ¿Cuántos tragos consumes en un día típico?", 
                         options=["1 o 2", "3 o 4", "5 o 6", "7 a 9", "10 o más"])
    
    p3 = st.select_slider("3. ¿Con qué frecuencia bebes 5 o más tragos en una sola ocasión?", 
                         options=["Nunca", "Menos de una vez al mes", "Mensualmente", "Semanalmente", "A diario o casi diario"])
    
    st.subheader("En el último año...")
    
    p4 = st.radio("4. ¿Sentiste que no podías parar de beber una vez empezado?", ["Nunca", "Menos de una vez al mes", "Mensualmente", "Semanalmente", "A diario"])
    p5 = st.radio("5. ¿Dejaste de hacer tus tareas normales por la bebida?", ["Nunca", "Menos de una vez al mes", "Mensualmente", "Semanalmente", "A diario"])
    p6 = st.radio("6. ¿Necesitaste beber en ayunas tras una noche de consumo?", ["Nunca", "Menos de una vez al mes", "Mensualmente", "Semanalmente", "A diario"])
    p7 = st.radio("7. ¿Sentiste culpa o remordimiento después de beber?", ["Nunca", "Menos de una vez al mes", "Mensualmente", "Semanalmente", "A diario"])
    p8 = st.radio("8. ¿Has tenido lagunas mentales (no recordar nada)?", ["Nunca", "Menos de una vez al mes", "Mensualmente", "Semanalmente", "A diario"])
    
    # Preguntas 9 y 10 (Escala especial: 0, 2, 4 puntos)
    st.divider()
    p9 = st.radio("9. ¿Tú o alguien más resultó herido por tu forma de beber?", ["No", "Sí, pero no este año", "Sí, durante este año"])
    p10 = st.radio("10. ¿Algún familiar o médico te ha sugerido dejar de beber?", ["No", "Sí, pero no este año", "Sí, durante este año"])

    # Botón de envío
    enviar = st.form_submit_button("VER MI RESULTADO")

# 5. Lógica de Puntuación y Resultados
if enviar:
    # Calculamos puntos de P1 a P8 (el índice de la opción elegida es el puntaje)
    puntos = 0
    puntos += ["Nunca", "1 o menos al mes", "2 a 4 al mes", "2 a 3 por semana", "4 o más por semana"].index(p1)
    puntos += ["1 o 2", "3 o 4", "5 o 6", "7 a 9", "10 o más"].index(p2)
    puntos += ["Nunca", "Menos de una vez al mes", "Mensualmente", "Semanalmente", "A diario o casi diario"].index(p3)
    
    for r in [p4, p5, p6, p7, p8]:
        puntos += ["Nunca", "Menos de una vez al mes", "Mensualmente", "Semanalmente", "A diario"].index(r)

    # Puntos de P9 y P10 (0, 2 o 4 según manual)
    map_especial = {"No": 0, "Sí, pero no este año": 2, "Sí, durante este año": 4}
    puntos += map_especial[p9]
    puntos += map_especial[p10]

    # Animación de carga
    with st.spinner('Procesando datos...'):
        time.sleep(1)

    st.subheader(f"Tu puntaje final es: {puntos}")

    # --- Interpretación Dinámica ---
    # Rangos según género (Imagen de referencia)
    limite_bajo = 4 if genero == "Hombre" else 3
    limite_riesgo = 14 if genero == "Hombre" else 12
    limite_perjudicial = 19 if genero == "Hombre" else 18

    if puntos <= limite_bajo:
        st.balloons() # Animación de globos
        st.success("### Nivel I: Riesgo Bajo")
        st.write("Tu consumo está dentro de los límites saludables. ¡Sigue así!")
        
    elif puntos <= limite_riesgo:
        st.warning("### Nivel II: Consumo de Riesgo")
        st.write("Atención: Estás consumiendo en niveles que podrían afectar tu salud a largo plazo. Se recomienda moderación.")
        
    elif puntos <= limite_perjudicial:
        st.error("### Nivel III: Consumo Perjudicial")
        st.write("Tu patrón de consumo ya muestra signos de daño físico o mental. Considera hablar con un profesional.")
        
    else:
        st.snow() # Animación de nieve (efecto visual de alerta)
        st.markdown("## 🚨 Nivel IV: Posible Dependencia")
        st.write("Es muy probable que necesites ayuda especializada. No ignores estas señales.")
    
    st.info("💡 **Consejo:** Esta herramienta es informativa. Si tienes dudas, consulta a un médico.")
