# Sistema de Encuestas con Diagrama de Clases
Sistema:
Este código es un sistema de encuestas que permite definir preguntas con diferentes tipos de validación de respuestas (por ejemplo, numéricas, de selección múltiple, de texto libre) y que además aplica las restricciones de edad y región para las encuestas limitadas.

Diagrama:
Este diagrama de clases modela la estructura del sistema de encuestas, definiendo las clases, sus atributos, métodos y las relaciones entre ellas. Contiene la información necesaria para entender cómo se organizan los datos y cómo interactúan las diferentes partes del sistema.


## Descripción de las Clases
**Usuario**: Representa a un usuario del sistema, con información como correo electrónico, edad y región.
**ListadoRespuestas**: Almacena las respuestas de un usuario a una encuesta.
**Respuesta**: Representa una respuesta individual a una pregunta.
**Encuesta**: Define una encuesta genérica con nombre, preguntas y respuestas de usuarios.
**EncuestaLimitadaRegion**: Especialización de Encuesta que restringe la participación a usuarios de ciertas regiones.
**EncuestaLimitadaEdad**: Especialización de Encuesta que restringe la participación a usuarios dentro de un rango de edad.
**Pregunta**: Representa una pregunta de la encuesta, con enunciado, ayuda, si es obligatoria y alternativas de respuesta.
**Alternativa**: Representa una opción de respuesta para una pregunta.




## Las clases con sus atributos y métodos:

### Usuario: Representa a un usuario del sistema de encuestas.
**Atributos**:
correo: Correo electrónico del usuario (string).
edad: Edad del usuario (int).
region: Región del usuario (int).

**Métodos**:
obtener_correo(), establecer_correo(): Permiten acceder y modificar el correo electrónico.
obtener_edad(), establecer_edad(): Permiten acceder y modificar la edad.
obtener_region(), establecer_region(): Permiten acceder y modificar la región.

### ListadoRespuestas: Representa una lista de respuestas a una encuesta, asociada a un usuario.
**Atributos**:
usuario: El usuario que generó la lista de respuestas (tipo Usuario).
respuestas: Lista de respuestas, representadas como números enteros (list[int]).

**Métodos**:
agregar_respuesta(): Agrega una nueva respuesta a la lista.
obtener_respuestas(): Devuelve la lista de respuestas.

### Respuesta: Representa una respuesta individual a una pregunta de la encuesta.
**Atributos**:
valor: Valor de la respuesta, representado como un número entero (int).

**Métodos**:
obtener_valor(): Devuelve el valor de la respuesta.

### Encuesta: Representa una encuesta genérica.
**Atributos**:
nombre: Nombre de la encuesta (string).
preguntas: Lista de preguntas que componen la encuesta (list[Pregunta]).
listado_respuestas: Lista de ListadoRespuestas, que contiene las respuestas de los usuarios (list[ListadoRespuestas]).

**Métodos**:
agregar_pregunta(): Agrega una nueva pregunta a la encuesta.
agregar_listado_respuestas(): Agrega una nueva lista de respuestas a la encuesta.

### EncuestaLimitadaRegion: Representa una encuesta que solo pueden responder usuarios de ciertas regiones. Hereda de Encuesta.
**Atributos**:
regiones: Lista de regiones permitidas (list[int]).

**Métodos**:
obtener_regiones(), establecer_regiones(): Permiten acceder y modificar la lista de regiones.

### EncuestaLimitadaEdad: Representa una encuesta que solo pueden responder usuarios dentro de un rango de edad. Hereda de Encuesta.
**Atributos**:
edad_minima: Edad mínima permitida (int).
edad_maxima: Edad máxima permitida (int).

**Métodos**:
obtener_edad_minima(), establecer_edad_minima(): Permiten acceder y modificar la edad mínima.
obtener_edad_maxima(), establecer_edad_maxima(): Permiten acceder y modificar la edad máxima.

### Pregunta: Representa una pregunta de la encuesta.
**Atributos**:
enunciado: Texto de la pregunta (string).
ayuda: Texto de ayuda opcional para la pregunta (string).
requerida: Indica si la pregunta es obligatoria (bool).
alternativas: Lista de alternativas de respuesta para la pregunta (list[Alternativa]).

**Métodos**:
obtener_enunciado(), establecer_enunciado(): Permiten acceder y modificar el enunciado.
obtener_ayuda(), establecer_ayuda(): Permiten acceder y modificar la ayuda.
obtener_requerida(), establecer_requerida(): Permiten acceder y modificar si la pregunta es requerida.
agregar_alternativa(): Agrega una nueva alternativa a la pregunta.

### Alternativa: Representa una alternativa de respuesta para una pregunta.
**Atributos**:
contenido: Texto de la alternativa (string).
ayuda: Texto de ayuda opcional para la alternativa (string).

**Métodos**:
obtener_contenido(), establecer_contenido(): Permiten acceder y modificar el contenido.
obtener_ayuda(), establecer_ayuda(): Permiten acceder y modificar la ayuda.


## Relaciones y multiplicidad
**Multiplicidad**:
Se indica en cada extremo de las relaciones para especificar cuántos objetos de cada clase pueden estar relacionados. Por ejemplo, un Usuario tiene un (1) ListadoRespuestas, pero una Encuesta puede tener muchos (0..*) ListadoRespuestas.

**Relaciones**:
### Composición (1 a 1):
Un Usuario "tiene" una y solo una ListadoRespuestas.
Un ListadoRespuestas "pertenece a" un y solo un Usuario.
*Se representa con un rombo negro sólido en el lado de Usuario.


### Asociación (1 a muchos):
Un ListadoRespuestas "contiene" una o más/varias (1..*) Respuestas.
Una Encuesta "contiene" cero o más/varias (0..*) Preguntas.
Una Pregunta "contiene" una o más/varias (1..*) Alternativas.


### Herencia:
EncuestaLimitadaRegion y EncuestaLimitadaEdad "son" tipos de Encuesta. Se utiliza una flecha con punta triangular blanca apuntando a Encuesta.


## Funcionamiento del Sistema
El sistema se puede ejecutar de dos maneras:

### 1. Creación de Encuesta Predefinida
El archivo main_crea_y_responde_encuesta.py contiene un ejemplo de cómo se puede crear una encuesta con preguntas y respuestas predefinidas. Este código crea una instancia de EncuestaLimitadaEdad, agrega preguntas con diferentes tipos de validación (texto, numerica, seleccion_multiple) y simula las respuestas de un usuario.

**Ejemplo de uso:**

# ... (código de las clases) ... 

def main():
    """Función principal para ejecutar el sistema de encuestas."""

    # Crear un usuario
    usuario = Usuario("juan@example.com", 25, 1)

    # Crear una encuesta limitada por edad
    encuesta_edad = EncuestaLimitadaEdad("Encuesta para jóvenes", 18, 30)

    # Agregar preguntas a la encuesta
    # ... (código para agregar preguntas) ...

    # Crear una lista de respuestas para el usuario
    listado_respuestas = ListadoRespuestas(usuario, encuesta_edad)

    # Responder las preguntas
    # ... (código para responder preguntas) ...

    # Agregar la lista de respuestas a la encuesta
    encuesta_edad.agregar_listado_respuestas(listado_respuestas)

    # Imprimir las respuestas
    # ... (código para imprimir respuestas) ...


if __name__ == "__main__":
    main()


### 2. Creación de Encuesta Interactiva**
El archivo main_encuesta_interactiva.py permite al usuario crear una encuesta de forma interactiva a través de inputs. El usuario puede definir el nombre de la encuesta, agregar preguntas con diferentes tipos y validaciones, y responder las preguntas.

**Ejemplo de uso:**

# ... (código de las clases) ...

def crear_usuario():
    # ... (código para crear usuario con inputs) ...

def crear_pregunta():
    # ... (código para crear pregunta con inputs) ...

def responder_encuesta(encuesta: Encuesta, usuario: Usuario):
    # ... (código para responder encuesta con inputs) ...

def main():
    """Función principal para ejecutar el sistema de encuestas."""

    # Crear un usuario
    usuario = crear_usuario()

    # Crear una encuesta
    nombre_encuesta = input("Ingresa el nombre de la encuesta: ")
    encuesta = Encuesta(nombre_encuesta)

    # Agregar preguntas a la encuesta
    # ... (código para agregar preguntas con inputs) ...

    # Responder la encuesta
    responder_encuesta(encuesta, usuario)

if __name__ == "__main__":
    main()


## Ejecución del código
Para ejecutar el sistema de encuestas, sigue estos pasos:
Para la encuesta estática:
Desde la terminal ejecuta el archivo con el comando python main_crea_y_responde_encuesta.py 
Para la encuesta interactiva:
Desde la terminal ejecuta el archivo con el comando python main_encuesta_interactiva.py

## Requisitos
- Python 3.6 o superior

## Autor
- Bárbara HA
- GitHub: https://github.com/bcahumada