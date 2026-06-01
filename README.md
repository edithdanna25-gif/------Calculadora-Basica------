Descripción

Este programa es una calculadora básica desarrollada en lenguaje Python, capaz de realizar operaciones aritméticas como suma, resta, multiplicación y división con números enteros y decimales.
A diferencia de las calculadoras que solo permiten operar con dos números a la vez, este programa acepta expresiones más largas en una sola línea. 
En su versión actual se implementa una jerarquía básica de operaciones, donde primero se resuelven multiplicaciones y divisiones, y posteriormente sumas y restas.
Además, el programa incluye la función ANS, que almacena el último resultado obtenido, permitiendo reutilizarlo en nuevas operaciones sin necesidad de volver a escribirlo.


Partes implementadas

1. Interfaz gráfica: la interfaz del programa fue desarrollada con Tkinter en Python. La ventana principal incluye una pantalla para mostrar la expresión matemática y el resultado, junto con botones organizados para el uso de la calculadora.
Estos botones permiten ingresar números del 0 al 9, punto decimal, operaciones básicas (suma, resta, multiplicación y división), además de funciones como igual (=), borrar todo (C), borrar un carácter (⌫), ANS, y opciones para ver y borrar el historial.
También se añadió una ventana secundaria que muestra el historial de operaciones, donde se visualizan los cálculos realizados junto con su resultado,fecha y hora en que fueron registrados.

2. Lógica: la lógica del programa evalúa expresiones matemáticas respetando una jerarquía básica de operaciones. Para ello, la expresión ingresada se convierte en una lista de números y operadores, que posteriormente se procesa en dos etapas:
   1. Primero se resuelven todas las multiplicaciones y divisiones en el orden en que aparecen.
   2. Después se resuelven las sumas y restas de izquierda a derecha.
      
Esto permite simular la prioridad de operaciones sin utilizar estructuras avanzadas.

El botón ANS permite reutilizar el último resultado obtenido. Cada vez que se presiona “=”, el resultado se guarda en una variable (ans). Al usar ANS, este valor se inserta en la expresión como si hubiera sido escrito manualmente, integrándose como un número más dentro del cálculo.
El manejo de errores se realiza mediante bloques try-except, lo que permite detectar expresiones inválidas, errores de formato o divisiones entre cero.

3. Persistencia de datos: el proyecto incluye un sistema de persistencia de datos utilizando archivos JSON. Cada vez que se realiza una operación válida, se guarda la expresión, el resultado y la fecha y hora del cálculo utilizando el módulo datetime.
Se implementaron tres funciones principales: una para guardar el historial, otra para cargarlo y otra para borrarlo completamente. El historial se almacena en el archivo historial.json.
La ventana de historial muestra los registros y permite visualizar todas las operaciones realizadas. También existe un botón para borrar el historial, que reinicia el archivo.

4. Main y Módulos: el archivo principal del proyecto (main) funciona como punto de entrada de la aplicación. En él se importan los módulos de interfaz, lógica y persistencia.
Este archivo inicializa la interfaz gráfica y conecta los botones con sus respectivas funciones, permitiendo que la calculadora funcione de manera integrada. También se encarga de ejecutar el bucle principal de la aplicación.


Aprendizajes obtenidos

- Durante el desarrollo de este proyecto aprendí a estructurar un programa en Python utilizando módulos separados para organizar mejor el código, dividiendo la lógica, la interfaz y la persistencia de datos.
- También reforcé el uso de la librería Tkinter para la creación de interfaces gráficas, aprendiendo a manejar botones, eventos y ventanas secundarias.
- Además, comprendí cómo trabajar con archivos JSON para guardar y cargar información, así como el uso del módulo datetime para registrar fechas y horas en los datos almacenados.
- Otro aprendizaje importante fue la implementación de lógica para evaluar expresiones matemáticas respetando una jerarquía básica de operaciones y el uso de variables como ANS para reutilizar resultados dentro de nuevas operaciones.
- También aprendí a implementar un sistema de historial de operaciones que permite guardar, visualizar y eliminar registros de cálculos, lo que facilitó el seguimiento de los resultados del programa.
- Finalmente, mejoré mi capacidad para manejar errores con bloques try-except, lo que permite que el programa funcione de forma más estable sin cerrarse ante entradas inválidas.
