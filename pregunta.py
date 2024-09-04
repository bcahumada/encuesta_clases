from typing import List, Union
from alternativa import Alternativa

class Pregunta:
    """Representa una pregunta de la encuesta."""

    TIPOS_PREGUNTA = ["texto", "numerica", "seleccion_multiple"]

    def __init__(self, enunciado: str, tipo: str, ayuda: str = "", requerida: bool = False):
        """
        Inicializa una nueva pregunta.

        Args:
            enunciado (str): Texto de la pregunta.
            tipo (str): Tipo de pregunta (texto, numerica, seleccion_multiple).
            ayuda (str, optional): Texto de ayuda para la pregunta. Defaults to "".
            requerida (bool, optional): Indica si la pregunta es obligatoria. Defaults to False.

        Raises:
            ValueError: Si el tipo de pregunta no es válido.
        """
        if tipo not in self.TIPOS_PREGUNTA:
            raise ValueError(f"Tipo de pregunta inválido: {tipo}. Debe ser uno de: {self.TIPOS_PREGUNTA}")
        
        self.__enunciado = enunciado
        self.__tipo = tipo
        self.__ayuda = ayuda
        self.__requerida = requerida
        self.__alternativas = [] if tipo == "seleccion_multiple" else None

    def obtener_enunciado(self) -> str:
        """Devuelve el enunciado de la pregunta."""
        return self.__enunciado

    def establecer_enunciado(self, enunciado: str):
        """Establece el enunciado de la pregunta."""
        self.__enunciado = enunciado

    def obtener_ayuda(self) -> str:
        """Devuelve el texto de ayuda de la pregunta."""
        return self.__ayuda

    def establecer_ayuda(self, ayuda: str):
        """Establece el texto de ayuda de la pregunta."""
        self.__ayuda = ayuda

    def obtener_requerida(self) -> bool:
        """Devuelve True si la pregunta es obligatoria, False en caso contrario."""
        return self.__requerida

    def establecer_requerida(self, requerida: bool):
        """Establece si la pregunta es obligatoria."""
        self.__requerida = requerida

    def agregar_alternativa(self, alternativa: Alternativa):
        """
        Agrega una alternativa a la pregunta (solo para preguntas de tipo 'seleccion_multiple').

        Args:
            alternativa (Alternativa): La alternativa a agregar.

        Raises:
            ValueError: Si se intenta agregar una alternativa a una pregunta que no es de tipo 'seleccion_multiple'.
        """
        if self.__tipo != "seleccion_multiple":
            raise ValueError("Solo se pueden agregar alternativas a preguntas de tipo 'seleccion_multiple'")
        self.__alternativas.append(alternativa)

    def obtener_alternativas(self) -> Union[List[Alternativa], None]:
        """Devuelve la lista de alternativas de la pregunta (None si no es de tipo 'seleccion_multiple')."""
        return self.__alternativas

    def validar_respuesta(self, respuesta: str) -> bool:
        """
        Valida la respuesta del usuario según el tipo de pregunta.

        Args:
            respuesta (str): La respuesta del usuario.

        Returns:
            bool: True si la respuesta es válida, False en caso contrario.
        """
        if self.__tipo == "texto":
            return True  # Cualquier texto es válido
        elif self.__tipo == "numerica":
            try:
                float(respuesta)
                return True
            except ValueError:
                return False
        elif self.__tipo == "seleccion_multiple":
            return respuesta in [alt.obtener_contenido() for alt in self.__alternativas]
        else:
            return False
        