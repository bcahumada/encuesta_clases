from encuesta import Encuesta
from listado_respuestas import ListadoRespuestas

class EncuestaLimitadaRegion(Encuesta):
    """Representa una encuesta limitada a usuarios de ciertas regiones."""

    def __init__(self, nombre: str, regiones: list[int]):
        """
        Inicializa una nueva encuesta limitada por región.

        Args:
            nombre (str): Nombre de la encuesta.
            regiones (list[int]): Lista de IDs de regiones permitidas.
        """
        super().__init__(nombre)
        self.__regiones = regiones

    def obtener_regiones(self) -> list[int]:
        """Devuelve la lista de IDs de regiones permitidas."""
        return self.__regiones

    def establecer_regiones(self, regiones: list[int]):
        """Establece la lista de IDs de regiones permitidas."""
        self.__regiones = regiones

    def agregar_listado_respuestas(self, listado_respuestas: ListadoRespuestas):
        """
        Agrega una lista de respuestas a la encuesta si la región del usuario cumple con la restricción.

        Args:
            listado_respuestas (ListadoRespuestas): La lista de respuestas a agregar.

        Raises:
            ValueError: Si la región del usuario no cumple con la restricción.
        """
        region_usuario = listado_respuestas.obtener_usuario().obtener_region()
        if region_usuario in self.__regiones:
            super().agregar_listado_respuestas(listado_respuestas)
        else:
            raise ValueError("La región del usuario no cumple con las restricciones de la encuesta.")