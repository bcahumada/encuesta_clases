from usuario import Usuario
from respuesta import Respuesta
from pregunta import Pregunta
#from encuesta import Encuesta


class ListadoRespuestas:
    """Representa una lista de respuestas de un usuario a una encuesta."""
    
    def __init__(self, usuario: Usuario, encuesta: 'Encuesta'):
        """
        Inicializa una nueva lista de respuestas.

        Args:
            usuario (Usuario): El usuario que responde la encuesta.
            encuesta (Encuesta): La encuesta a la que se responde.
        """
        from encuesta import Encuesta  # Importación local 
        self.__usuario = usuario
        self.__encuesta = encuesta
        self.__respuestas = []

    def agregar_respuesta(self, pregunta: 'Pregunta', respuesta: str) -> bool:
        """
        Agrega una respuesta a la lista, validándola según el tipo de pregunta.

        Args:
            pregunta (Pregunta): La pregunta a la que se responde.
            respuesta (str): La respuesta del usuario.

        Returns:
            bool: True si la respuesta es válida y se agregó correctamente, False en caso contrario.
        """
        if not pregunta.validar_respuesta(respuesta):
            return False
        self.__respuestas.append(Respuesta(pregunta, respuesta))
        return True

    def obtener_respuestas(self) -> list[Respuesta]:
        """Devuelve la lista de respuestas."""
        return self.__respuestas

    def obtener_usuario(self) -> Usuario:
        """Devuelve el usuario asociado a la lista de respuestas."""
        return self.__usuario