from pregunta import Pregunta

class Respuesta:
    """Representa una respuesta individual a una pregunta."""

    def __init__(self, pregunta: Pregunta, valor: str):
        """
        Inicializa una nueva respuesta.

        Args:
            pregunta (Pregunta): La pregunta a la que se responde.
            valor (str): La respuesta del usuario.
        """
        self.__pregunta = pregunta
        self.__valor = valor

    def obtener_valor(self) -> str:
        """Devuelve la respuesta del usuario."""
        return self.__valor

    def obtener_pregunta(self) -> Pregunta:
        """Devuelve la pregunta a la que se responde."""
        return self.__pregunta
