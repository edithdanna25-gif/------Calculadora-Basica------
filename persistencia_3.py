#IMPORTAR LIBRERÍAS PARA EL MANEJO DE ARCHIVOS Y FECHAS
import json
from datetime import datetime


#BORRAR HISTORIAL
def borrar_historial():
    """Elimina todo el contenido del historial de operaciones.

    Reinicia el archivo JSON dejando una lista vacía.

    Args:
        None

    Returns:
        None
    """
    
    #Reiniciar el archivo JSON con una lista vacía.
    with open("historial.json", "w") as archivo:
        archivo.write("[]")


#GUARDAR HISTORIAL
def guardar_historial(operacion, resultado):
    """Guarda en el historial una operación realizada.

    Crea un registro con la operación, resultado y fecha actual,
    y lo almacena en un archivo JSON.

    Args:
        operacion (str): Operación matemática hecha.
        resultado (float): Resultado de la operación.

    Returns:
        None
    """

    #Crear un registro con la operación, resultado y fecha actual.
    registro = {
        "operacion": operacion,
        "resultado": resultado,
        #Formato: Año-Mes-Día Hora:Minuto-Segundo.
        "fecha": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }

    try:
        #Abrir y cargar el historial.
        with open("historial.json", "r") as archivo:
            datos = json.load(archivo)

    #Si el archivo no existe o está vacío, iniciar una lista vacía.
    except:
        datos = []

    #Agregar el nuevo registro al historial.
    datos.append(registro)

    #Guardar nuevamente el historial actualizado.
    with open("historial.json", "w") as archivo:
        json.dump(datos, archivo, indent=4)


#CARGAR HISTORIAL
def cargar_historial():
    """Carga el historial de operaciones almacenado.

    Args:
        None

    Returns:
        list: Lista con los registros almacenados en el historial.
    """

    try:
        #Leer y devolver el contenido del archivo JSON.
        with open("historial.json", "r") as archivo:
            return json.load(archivo)

    #Retornar una lista vacía si ocurre un error al leer el archivo.
    except:
        return []