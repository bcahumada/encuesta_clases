from usuario import Usuario
from encuesta import Encuesta
from encuesta_limitada_edad import EncuestaLimitadaEdad
from encuesta_limitada_region import EncuestaLimitadaRegion
from pregunta import Pregunta
from alternativa import Alternativa
from listado_respuestas import ListadoRespuestas

def crear_usuario():
    """Crea un usuario solicitando los datos por input con validaciones."""
    while True:
        correo = input("Ingresa tu correo electrónico: ")
        if "@" in correo:
            break
        print("Correo electrónico inválido. El correo debe contener '@'. Intenta de nuevo.")

    while True:
        try:
            edad = int(input("Ingresa tu edad: "))
            if 130 > edad > 0:
                break
            print("Edad inválida. Intenta de nuevo.")
        except ValueError:
            print("Ingresa un número válido para la edad.")

    while True:
        try:
            region = int(input("Ingresa tu región (ID numérico entre 1 y 16): "))
            break
        except ValueError:
            print("Ingresa un ID de región válido (número).")

    return Usuario(correo, edad, region)

def crear_pregunta():
    """Crea una pregunta solicitando los datos por input con validaciones."""
    enunciado = input("Ingresa el enunciado de la pregunta: ")

    while True:
        tipo = input("Ingresa el tipo de pregunta (texto, numerica, seleccion_multiple): ")
        if tipo in Pregunta.TIPOS_PREGUNTA:
            break
        print(f"Tipo de pregunta inválido. Debe ser uno de: {Pregunta.TIPOS_PREGUNTA}")

    ayuda = input("Ingresa la ayuda de la pregunta (opcional): ")
    requerida = input("¿Es obligatoria? (si/no): ").lower() == "si"

    pregunta = Pregunta(enunciado, tipo, ayuda, requerida)

    if tipo == "seleccion_multiple":
        while True:
            alternativa_texto = input("Ingresa el texto de la alternativa (o 'fin' para terminar): ")
            if alternativa_texto.lower() == "fin":
                break
            pregunta.agregar_alternativa(Alternativa(alternativa_texto))

    return pregunta

def responder_encuesta(encuesta: Encuesta, usuario: Usuario):
    """Permite al usuario responder una encuesta."""
    listado_respuestas = ListadoRespuestas(usuario, encuesta)

    print(f"\n--- Respondiendo encuesta: {encuesta.obtener_nombre()} ---\n")
    for pregunta in encuesta.obtener_preguntas():
        print(f"{pregunta.obtener_enunciado()}")
        if pregunta.obtener_ayuda():
            print(f"Ayuda: {pregunta.obtener_ayuda()}")
        if pregunta.obtener_requerida():
            print("(Obligatoria)")
        
        if pregunta.obtener_alternativas():
            for i, alternativa in enumerate(pregunta.obtener_alternativas()):
                print(f"{i + 1}. {alternativa.obtener_contenido()}")
            while True:
                try:
                    opcion = int(input("Elige una opción: "))
                    if 1 <= opcion <= len(pregunta.obtener_alternativas()):
                        respuesta = pregunta.obtener_alternativas()[opcion - 1].obtener_contenido()
                        break
                    else:
                        print("Opción inválida. Intenta de nuevo.")
                except ValueError:
                    print("Ingresa un número válido.")
        else:
            respuesta = input("Tu respuesta: ")

        listado_respuestas.agregar_respuesta(pregunta, respuesta)
        print()

    encuesta.agregar_listado_respuestas(listado_respuestas)
    print("--- Encuesta respondida correctamente ---")

def main():
    """Función principal para ejecutar el sistema de encuestas."""

    # Crear un usuario
    usuario = crear_usuario()

    # Crear una encuesta
    nombre_encuesta = input("Ingresa el nombre de la encuesta: ")
    encuesta = Encuesta(nombre_encuesta)

    # Agregar preguntas a la encuesta
    while True:
        agregar_pregunta = input("¿Deseas agregar una pregunta? (si/no): ").lower()
        if agregar_pregunta == "no":
            break
        elif agregar_pregunta == "si":
            pregunta = crear_pregunta()
            encuesta.agregar_pregunta(pregunta)
        else:
            print("Opción inválida. Intenta de nuevo.")

    # Responder la encuesta
    responder_encuesta(encuesta, usuario)

if __name__ == "__main__":
    main()