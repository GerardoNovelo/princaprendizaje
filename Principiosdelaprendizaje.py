import streamlit as st

# Título y descripción
st.title("🧠 Quiz: Principios del Aprendizaje")
st.write("Contesta cada pregunta. Solo podrás avanzar si eliges la opción correcta. ¡Buena suerte!")

# Lista de preguntas, opciones, retroalimentaciones y respuesta correcta
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
    {
        "pregunta": "¿Qué papel juega la motivación en el aprendizaje?",
        "opciones": [
            ("Es irrelevante si el contenido es obligatorio", "❌ Incorrecto. Sin motivación, incluso el contenido obligatorio puede ser difícil de asimilar."),
            ("Es un factor clave para mantener la atención y el esfuerzo", "✅ Correcto. La motivación dirige y sostiene la conducta de aprendizaje."),
            ("Solo importa en actividades recreativas", "❌ Incorrecto. La motivación es crucial en todo tipo de aprendizajes, académicos o no.")
        ],
        "correcta": "Es un factor clave para mantener la atención y el esfuerzo"
    },
    {
        "pregunta": "El principio de práctica distribuida sugiere que se aprende mejor cuando...",
        "opciones": [
            ("Se estudia todo de una vez", "❌ Incorrecto. Estudiar de forma intensiva sin pausas puede saturar la memoria."),
            ("Se repite el material varias veces seguidas sin descanso", "❌ Incorrecto. La repetición sin pausas no permite consolidar lo aprendido."),
            ("Se reparte el estudio en sesiones más cortas a lo largo del tiempo", "✅ Correcto. Distribuir la práctica mejora la retención a largo plazo.")
        ],
        "correcta": "Se reparte el estudio en sesiones más cortas a lo largo del tiempo"
    },
    {
        "pregunta": "¿Qué efecto tiene el feedback inmediato en el proceso de aprendizaje?",
        "opciones": [
            ("Dificulta el aprendizaje autónomo", "❌ Incorrecto. Bien utilizado, el feedback fomenta la autonomía al mostrar errores a tiempo."),
            ("Ayuda a corregir errores y afianzar conocimientos", "✅ Correcto. La retroalimentación inmediata permite hacer ajustes rápidos y eficaces."),
            ("Hace que los estudiantes dependan del docente", "❌ Incorrecto. El feedback no crea dependencia si se usa para guiar, no para controlar.")
        ],
        "correcta": "Ayuda a corregir errores y afianzar conocimientos"
    },
    {
        "pregunta": "El principio de atención indica que...",
        "opciones": [
            ("Se puede aprender sin prestar atención", "❌ Incorrecto. La atención es fundamental para procesar y codificar la información."),
            ("La atención es necesaria para codificar la información de forma eficaz", "✅ Correcto. Sin atención, es difícil que el contenido llegue a la memoria de largo plazo."),
            ("La atención es más importante que el interés", "❌ Incorrecto. Ambos son importantes y se complementan: el interés facilita la atención.")
        ],
        "correcta": "La atención es necesaria para codificar la información de forma eficaz"
    },
    {
        "pregunta": "¿Qué tipo de aprendizaje ocurre cuando se observan las consecuencias del comportamiento de otros?",
        "opciones": [
            ("Aprendizaje por condicionamiento clásico", "❌ Incorrecto. El condicionamiento clásico se basa en asociaciones entre estímulos."),
            ("Aprendizaje observacional o vicario", "✅ Correcto. Aprender viendo a otros se conoce como aprendizaje vicario, según Bandura."),
            ("Aprendizaje reflexivo", "❌ Incorrecto. El aprendizaje reflexivo implica análisis propio, no observación externa.")
        ],
        "correcta": "Aprendizaje observacional o vicario"
    },
    {
        "pregunta": "¿Cuál de los siguientes factores favorece el aprendizaje significativo?",
        "opciones": [
            ("Presentar información sin contexto", "❌ Incorrecto. La información sin conexión es difícil de recordar o entender."),
            ("Enseñar de lo complejo a lo simple", "❌ Incorrecto. Generalmente se recomienda ir de lo simple a lo complejo para facilitar comprensión."),
            ("Utilizar ejemplos concretos y relevantes", "✅ Correcto. Los ejemplos contextualizados permiten comprender y aplicar mejor el contenido.")
        ],
        "correcta": "Utilizar ejemplos concretos y relevantes"
    },
    {
        "pregunta": "¿Qué establece el principio de 'transferencia del aprendizaje'?",
        "opciones": [
            ("Que los aprendizajes no pueden aplicarse fuera del aula", "❌ Incorrecto. El objetivo es justamente lo contrario: aplicar lo aprendido a nuevos contextos."),
            ("Que el conocimiento adquirido puede aplicarse a nuevas situaciones", "✅ Correcto. La transferencia permite usar lo aprendido en otras áreas o problemas."),
            ("Que el aprendizaje es únicamente mecánico", "❌ Incorrecto. La transferencia implica comprensión, no solo repetición mecánica.")
        ],
        "correcta": "Que el conocimiento adquirido puede aplicarse a nuevas situaciones"
    },
    {
        "pregunta": "¿Cuál es una característica del aprendizaje activo?",
        "opciones": [
            ("El estudiante es un receptor pasivo de la información", "❌ Incorrecto. El aprendizaje activo implica participación, no pasividad."),
            ("Se basa solo en la escucha y la observación", "❌ Incorrecto. Va más allá de observar; requiere hacer, discutir, resolver problemas."),
            ("El estudiante participa activamente en la construcción del conocimiento", "✅ Correcto. El estudiante construye su propio conocimiento al interactuar con el contenido.")
        ],
        "correcta": "El estudiante participa activamente en la construcción del conocimiento"
    }
]

# Estado inicial
if 'pregunta_actual' not in st.session_state:
    st.session_state.pregunta_actual = 0
if 'respuesta_correcta' not in st.session_state:
    st.session_state.respuesta_correcta = False

# Mostrar la pregunta actual
index = st.session_state.pregunta_actual

if index < len(quiz):
    pregunta = quiz[index]
    st.subheader(f"Pregunta {index + 1} de {len(quiz)}")
    st.write(pregunta["pregunta"])

    opciones_texto = [op[0] for op in pregunta["opciones"]]
    seleccion = st.radio("Selecciona una opción:", opciones_texto, key=f"pregunta_{index}")

    if st.button("Responder", key=f"boton_{index}"):
        for opcion_texto, retro in pregunta["opciones"]:
            if seleccion == opcion_texto:
                st.info(retro)
                st.session_state.respuesta_correcta = (seleccion == pregunta["correcta"])
                break

    # Mostrar botón para avanzar solo si respondió correctamente
    if st.session_state.respuesta_correcta:
        if st.button("Siguiente", key=f"siguiente_{index}"):
            st.session_state.pregunta_actual += 1
            st.session_state.respuesta_correcta = False
            st.experimental_rerun()
else:
    st.success("🎉 ¡Felicidades! Has completado todas las preguntas del quiz sobre los principios del aprendizaje.")
    st.balloons()
