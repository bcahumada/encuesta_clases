class Alternativa:
    """Representa una alternativa de respuesta para una pregunta."""

    def __init__(self, contenido: str, ayuda: str = ""):
        """
        Inicializa una nueva alternativa.

        Args:
            contenido (str): Texto de la alternativa.
            ayuda (str, optional): Texto de ayuda para la alternativa. Defaults to "".
        """
        self.__contenido = contenido
        self.__ayuda = ayuda

    def obtener_contenido(self) -> str:
        """Devuelve el texto de la alternativa."""
        return self.__contenido

    def establecer_contenido(self, contenido: str):
        """Establece el texto de la alternativa."""
        self.__contenido = contenido

    def obtener_ayuda(self) -> str:
        """Devuelve el texto de ayuda de la alternativa."""
        return self.__ayuda

    def establecer_ayuda(self, ayuda: str):
        """Establece el texto de ayuda de la alternativa."""
        self.__ayuda = ayuda