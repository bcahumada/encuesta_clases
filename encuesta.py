from pregunta import Pregunta
from listado_respuestas import ListadoRespuestas

class Encuesta:
    """Representa una encuesta genérica."""

    def __init__(self, nombre: str):
        """
        Inicializa una nueva encuesta.

        Args:
            nombre (str): Nombre de la encuesta.
        """
        self.__nombre = nombre
        self.__preguntas = []
        self.__listado_respuestas = []

    def agregar_pregunta(self, pregunta: Pregunta):
        """Agrega una pregunta a la encuesta."""
        self.__preguntas.append(pregunta)

    def agregar_listado_respuestas(self, listado_respuestas: ListadoRespuestas):
        """Agrega una lista de respuestas a la encuesta."""
        self.__listado_respuestas.append(listado_respuestas)

    def obtener_nombre(self) -> str:
        """Devuelve el nombre de la encuesta."""
        return self.__nombre

    def establecer_nombre(self, nombre: str):
        """Establece el nombre de la encuesta."""
        self.__nombre = nombre

    def obtener_preguntas(self) -> list[Pregunta]:
        """Devuelve la lista de preguntas de la encuesta."""
        return self.__preguntas

    def obtener_listado_respuestas(self) -> list[ListadoRespuestas]:
        """Devuelve la lista de respuestas a la encuesta."""
        return self.__listado_respuestas