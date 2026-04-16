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
    /* Cajas de resultados */
    .resultado-box {
        padding: 20px;
        border-radius: 10px;
        margin-top: 20px;
        background-color: #f8f9fa;
        border-left: 5px solid #007bff;
    }
    </style>
    """, unsafe_allow_html=True)

# 2. ENCABEZADO Y GUÍA DE NIVELES
st.title("🛡️ Auto-Evaluación de Bienestar")

with st.expander("📚 Ver explicación de los Niveles de Riesgo (Guía AUDIT)"):
    st.markdown("""
    El cuestionario AUDIT (Alcohol Use Disorders Identification Test) de la OMS clasifica el consumo en 4 niveles. *Nota: Los puntajes de corte varían ligeramente entre hombres y mujeres por factores biológicos y metabólicos.*
    
    * **Nivel I (Riesgo Bajo):** Consumo moderado que no representa un peligro evidente para la salud física o mental.
    * **Nivel II (Riesgo Medio):** Consumo que podría llevar a problemas de salud si se mantiene a largo plazo. Se recomienda prevención.
    * **Nivel III (Consumo Perjudicial):** Ya existe un patrón de consumo que causa daños a la salud física o mental. Requiere intervención y estrategias de cambio.
    * **Nivel IV (Posible Dependencia):** Patrón de consumo compulsivo con alta probabilidad de dependencia física o psicológica. Requiere abordaje multidisciplinario inmediato.
    """)

st.write("Responde las 10 preguntas con sinceridad. Tus respuestas son **100% privadas y confidenciales**.")
st.info("💡 **Recuerda:** 1 Trago = 1 Cerveza pequeña = 1 Copa de vino = 1 Shot de licor.")

# 3. FORMULARIO COMPLETO (10 PREGUNTAS)
with st.form("audit_completo"):
    
    st.markdown("<div class='pregunta-titulo'>Selecciona tu género:</div>", unsafe_allow_html=True)
    genero = st.radio("Dato necesario para ajustar el rango metabólico y médico:", ["Hombre", "Mujer"], horizontal=True, label_visibility="collapsed")
    
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

# 4. LÓGICA DE PUNTUACIÓN Y RECOMENDACIONES TERAPÉUTICAS
if boton:
    score = 0
    score += ["Nunca", "1 vez al mes o menos", "2 a 4 veces al mes", "2 a 3 veces por semana", "4 o más veces por semana"].index(p1)
    score += ["1 o 2", "3 o 4", "5 o 6", "7 a 9", "10 o más"].index(p2)
    score += ["Nunca", "Menos de una vez al mes", "Mensualmente", "Semanalmente", "A diario"].index(p3)
    for r in [p4, p5, p6, p7, p8]:
        score += ["Nunca", "Menos de una vez al mes", "Mensualmente", "Semanalmente", "A diario"].index(r)
    
    map_9_10 = {"No": 0, "Sí, pero no en el último año": 2, "Sí, durante el último año": 4}
    score += map_9_10[p9]
    score += map_9_10[p10]

    with st.spinner('Procesando perfil y generando análisis terapéutico...'):
        time.sleep(1.5)

    st.markdown(f"<h2 style='text-align: center;'>Puntaje Total Obtenido: {score}</h2>", unsafe_allow_html=True)

    # Rangos de corte clínico según género
    r1, r2, r3 = (4, 14, 19) if genero == "Hombre" else (3, 12, 18)

    if score <= r1:
        st.balloons()
        st.success("✅ **Nivel I: Riesgo Bajo / Consumo Saludable**")
        st.markdown("""
        <div class='resultado-box' style='border-left-color: #28a745;'>
        <strong>Análisis y Conclusiones:</strong><br>
        Tus resultados indican que tu patrón de consumo actual no representa un riesgo significativo para tu salud física, mental o entorno social. Mantienes un excelente control preventivo.
        <br><br>
        <strong>Recomendaciones Terapéuticas:</strong>
        <ul>
            <li><strong>Refuerzo Positivo:</strong> Mantén tus límites actuales. Conocer tu tolerancia es una habilidad protectora fundamental.</li>
            <li><strong>Hidratación:</strong> Si decides beber ocasionalmente, alterna siempre cada trago de alcohol con un vaso de agua para proteger tu función renal y neurológica.</li>
            <li><strong>Consumo Consciente:</strong> Evita el alcohol como mecanismo de afrontamiento ante el estrés; sigue priorizando estrategias saludables como el ejercicio o el diálogo.</li>
        </ul>
        </div>
        """, unsafe_allow_html=True)

    elif score <= r2:
        st.warning("⚠️ **Nivel II: Riesgo Medio / Consumo de Precaución**")
        st.markdown("""
        <div class='resultado-box' style='border-left-color: #ffc107;'>
        <strong>Análisis y Conclusiones:</strong><br>
        Estás en un nivel donde tu consumo está comenzando a rozar límites que pueden generar problemas de salud metabólica o episodios de pérdida de control. Aunque no hay dependencia, es el momento ideal para una intervención breve preventiva.
        <br><br>
        <strong>Recomendaciones Terapéuticas y Plan de Acción:</strong>
        <ul>
            <li><strong>Identificación de Disparadores:</strong> Lleva un registro mental o escrito de qué situaciones (estrés laboral, problemas familiares, presión social) te impulsan a beber más de lo planeado.</li>
            <li><strong>Pausas Programadas:</strong> Establece al menos 3 a 4 días consecutivos a la semana totalmente libres de alcohol para permitir la desintoxicación hepática.</li>
            <li><strong>Reducción de Daños:</strong> Limita la velocidad de consumo (no más de un trago por hora) y asegúrate de haber comido bien antes de ingerir alcohol.</li>
        </ul>
        </div>
        """, unsafe_allow_html=True)

    elif score <= r3:
        st.error("🚨 **Nivel III: Consumo Perjudicial / Riesgo Alto**")
        st.markdown("""
        <div class='resultado-box' style='border-left-color: #dc3545;'>
        <strong>Análisis y Conclusiones:</strong><br>
        Tu puntaje sugiere un patrón de consumo perjudicial. Esto significa que el alcohol ya podría estar causando, o está muy cerca de causar, un impacto negativo directo en tu salud física (hígado, sistema nervioso), en tus relaciones interpersonales o en tu desempeño diario.
        <br><br>
        <strong>Recomendaciones Terapéuticas y Plan de Acción:</strong>
        <ul>
            <li><strong>Evaluación Clínica:</strong> Se sugiere fuertemente programar una evaluación con un profesional de la salud mental o un médico general para realizar chequeos de rutina (perfil hepático).</li>
            <li><strong>Sustitución de Hábitos:</strong> Es crucial desarrollar nuevas estrategias de regulación emocional. El alcohol está actuando como un sedante a corto plazo, pero aumenta la ansiedad a largo plazo.</li>
            <li><strong>Red de Apoyo:</strong> Comparte tu deseo de reducir el consumo con alguien de confianza. Evita temporalmente los círculos sociales donde la única actividad gire en torno a la bebida.</li>
            <li><strong>Metas a Corto Plazo:</strong> Intenta un período de abstinencia voluntaria de 2 a 4 semanas para evaluar cómo mejora tu sueño, tu energía y tu estado de ánimo.</li>
        </ul>
        </div>
        """, unsafe_allow_html=True)

    else:
        st.snow()
        st.error("🆘 **Nivel IV: Posible Dependencia / Alerta Crítica**")
        st.markdown("""
        <div class='resultado-box' style='border-left-color: #8b0000; color: #8b0000;'>
        <strong>Análisis y Conclusiones:</strong><br>
        Los resultados son indicativos de una posible dependencia al alcohol. En este nivel, la fuerza de voluntad por sí sola rara vez es suficiente debido a las adaptaciones neuroquímicas que ha sufrido el cerebro. Intentar detener el consumo abruptamente sin supervisión puede llevar a un síndrome de abstinencia peligroso.
        <br><br>
        <strong>Recomendaciones Terapéuticas Estrictas:</strong>
        <ul>
            <li><strong>Atención Profesional Inmediata:</strong> Acude a un centro de salud, psicólogo clínico o psiquiatra. Necesitas un protocolo de desintoxicación seguro y estructurado.</li>
            <li><strong>Acompañamiento Constante:</strong> No te aísles. Involucra a un familiar directo o amigo cercano en este proceso. Considera grupos de apoyo mutuo (como AA).</li>
            <li><strong>Reestructuración Ambiental:</strong> Retira todo el alcohol de tu entorno inmediato (casa, vehículo). </li>
            <li><strong>Sin Estigmas:</strong> Reconocer este nivel es el paso más valiente e importante. La dependencia es una condición médica tratable, no un fracaso moral.</li>
        </ul>
        </div>
        """, unsafe_allow_html=True)

    st.info("📌 **Nota Institucional:** Este reporte es automatizado y tiene fines de tamizaje y psicoeducación. No sustituye un diagnóstico clínico formal. Si sientes que necesitas apoyo, no dudes en buscar la ayuda de un profesional capacitado.")
