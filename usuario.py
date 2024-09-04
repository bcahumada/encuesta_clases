class Usuario:
    """Representa un usuario del sistema de encuestas."""

    def __init__(self, correo: str, edad: int, region: int):
        """
        Inicializa un nuevo usuario.

        Args:
            correo (str): Correo electrónico del usuario.
            edad (int): Edad del usuario.
            region (int): Región del usuario.
        """
        self.__correo = correo
        self.__edad = edad
        self.__region = region

    def obtener_correo(self) -> str:
        """Devuelve el correo electrónico del usuario."""
        return self.__correo

    def establecer_correo(self, correo: str):
        """Establece el correo electrónico del usuario."""
        self.__correo = correo

    def obtener_edad(self) -> int:
        """Devuelve la edad del usuario."""
        return self.__edad

    def establecer_edad(self, edad: int):
        """Establece la edad del usuario."""
        self.__edad = edad

    def obtener_region(self) -> int:
        """Devuelve la región del usuario."""
        return self.__region

    def establecer_region(self, region: int):
        """Establece la región del usuario."""
        self.__region = region