from encuesta import Encuesta
from listado_respuestas import ListadoRespuestas


class EncuestaLimitadaEdad(Encuesta):
    """Representa una encuesta limitada a usuarios dentro de un rango de edad."""

    def __init__(self, nombre: str, edad_minima: int, edad_maxima: int):
        """
        Inicializa una nueva encuesta limitada por edad.

        Args:
            nombre (str): Nombre de la encuesta.
            edad_minima (int): Edad mínima permitida.
            edad_maxima (int): Edad máxima permitida.
        """
        super().__init__(nombre)
        self.__edad_minima = edad_minima
        self.__edad_maxima = edad_maxima

    def obtener_edad_minima(self) -> int:
        """Devuelve la edad mínima permitida."""
        return self.__edad_minima

    def establecer_edad_minima(self, edad_minima: int):
        """Establece la edad mínima permitida."""
        self.__edad_minima = edad_minima

    def obtener_edad_maxima(self) -> int:
        """Devuelve la edad máxima permitida."""
        return self.__edad_maxima

    def establecer_edad_maxima(self, edad_maxima: int):
        """Establece la edad máxima permitida."""
        self.__edad_maxima = edad_maxima

    def agregar_listado_respuestas(self, listado_respuestas: ListadoRespuestas):
        """
        Agrega una lista de respuestas a la encuesta si la edad del usuario cumple con la restricción.

        Args:
            listado_respuestas (ListadoRespuestas): La lista de respuestas a agregar.

        Raises:
            ValueError: Si la edad del usuario no cumple con la restricción.
        """
        edad_usuario = listado_respuestas.obtener_usuario().obtener_edad()
        if self.__edad_minima <= edad_usuario <= self.__edad_maxima:
            super().agregar_listado_respuestas(listado_respuestas)
        else:
            raise ValueError("La edad del usuario no cumple con las restricciones de la encuesta.")