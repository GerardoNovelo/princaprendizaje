import streamlit as st

# Título de la app
st.title("Quiz: Principios del Aprendizaje")
st.write("Responde cada pregunta. Solo podrás avanzar si contestas correctamente.")

# Lista de preguntas, opciones y retroalimentaciones
quiz = [
    {
        "pregunta": "¿Cuál de los siguientes principios es fundamental para que el aprendizaje sea significativo?",
        "opciones": [
            ("Repetir sin comprender", "❌ Incorrecto. La repetición mecánica ayuda poco si no se comprende el contenido."),
            ("Relacionar la nueva información con conocimientos previos", "✅ Correcto. Aprender de forma significativa implica conectar lo nuevo con lo que ya se sabe."),
            ("Memorizar datos al azar", "❌ Incorrecto. Memorizar sin contexto no favorece la comprensión ni la retención duradera.")
        ],
        "correcta": "Relacionar la nueva información con conocimientos previos"
    },
    {
        "pregunta": "Según la teoría del aprendizaje, ¿qué aumenta la probabilidad de que un comportamiento se repita?",
        "opciones": [
            ("La fatiga mental", "❌ Incorrecto. El cansancio disminuye la motivación y la eficacia del aprendizaje."),
            ("Un castigo inmediato", "❌ Incorrecto. El castigo puede generar evitación, pero no necesariamente fomenta el aprendizaje."),
            ("Un refuerzo positivo", "✅ Correcto. Los refuerzos positivos (elogios, recompensas) incrementan la repetición del comportamiento.")
        ],
        "correcta": "Un refuerzo positivo"
    },
    # Puedes continuar con las otras 8 preguntas aquí...
]

# Estado de la aplicación
if 'pregunta_actual' not in st.session_state:
    st.session_state.pregunta_actual = 0
if 'respuesta_correcta' not in st.session_state:
    st.session_state.respuesta_correcta = False

# Mostrar la pregunta actual
index = st.session_state.pregunta_actual

if index < len(quiz):
    pregunta = quiz[index]
    st.subheader(f"Pregunta {index + 1}")
    st.write(pregunta["pregunta"])

    opciones_texto = [op[0] for op in pregunta["opciones"]]
    seleccion = st.radio("Selecciona una opción:", opciones_texto, key=f"pregunta_{index}")

    if st.button("Responder", key=f"boton_{index}"):
        for opcion_texto, retro in pregunta["opciones"]:
            if seleccion == opcion_texto:
                st.info(retro)
                if seleccion == pregunta["correcta"]:
                    st.session_state.respuesta_correcta = True
                else:
                    st.session_state.respuesta_correcta = False

    # Mostrar botón para continuar solo si respondió correctamente
    if st.session_state.respuesta_correcta:
        if st.button("Siguiente pregunta", key=f"siguiente_{index}"):
            st.session_state.pregunta_actual += 1
            st.session_state.respuesta_correcta = False
            st.experimental_rerun()
else:
    st.success("🎉 ¡Felicidades! Has completado todas las preguntas del quiz sobre los principios del aprendizaje.")
    st.balloons()
