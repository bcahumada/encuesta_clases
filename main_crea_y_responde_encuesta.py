from usuario import Usuario
from encuesta import Encuesta
from encuesta_limitada_edad import EncuestaLimitadaEdad
from pregunta import Pregunta
from alternativa import Alternativa
from listado_respuestas import ListadoRespuestas

def main():
    """Función principal para ejecutar el sistema de encuestas."""

    # Crear un usuario
    usuario = Usuario("juan@blabla.com", 25, 1)

    # Crear una encuesta limitada por edad
    encuesta_edad = EncuestaLimitadaEdad("Encuesta para jóvenes", 18, 30)

    # Agregar preguntas a la encuesta
    pregunta1 = Pregunta("¿Cuál es tu color favorito?", "texto")
    encuesta_edad.agregar_pregunta(pregunta1)

    pregunta2 = Pregunta("¿Cuántos años tienes?", "numerica", requerida=True)
    encuesta_edad.agregar_pregunta(pregunta2)

    pregunta3 = Pregunta("¿Qué te gusta hacer en tu tiempo libre?", "seleccion_multiple")
    pregunta3.agregar_alternativa(Alternativa("Leer"))
    pregunta3.agregar_alternativa(Alternativa("Deportes"))
    pregunta3.agregar_alternativa(Alternativa("Videojuegos"))
    encuesta_edad.agregar_pregunta(pregunta3)

    # Crear una lista de respuestas para el usuario
    listado_respuestas = ListadoRespuestas(usuario, encuesta_edad)

    # Responder las preguntas
    listado_respuestas.agregar_respuesta(pregunta1, "Azul")
    listado_respuestas.agregar_respuesta(pregunta2, "25")
    listado_respuestas.agregar_respuesta(pregunta3, "Deportes")

    # Agregar la lista de respuestas a la encuesta
    encuesta_edad.agregar_listado_respuestas(listado_respuestas)

    # Imprimir las respuestas
    for respuesta in listado_respuestas.obtener_respuestas():
        print(f"Pregunta: {respuesta.obtener_pregunta().obtener_enunciado()}")
        print(f"Respuesta: {respuesta.obtener_valor()}\n")


if __name__ == "__main__":
    main()