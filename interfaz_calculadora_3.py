#IMPORTACIONES
import tkinter as tk
from tkinter import messagebox

from persistencia_3 import guardar_historial, cargar_historial, borrar_historial
from logica_calculadora_3 import *
from logica_calculadora_3 import evaluar_expresion


#ESTADO GLOBAL

#Expresión actual de la calculadora
operacion = ""

#Último resultado calculado (ANS)
ans = 0


#VENTANA PRINCIPAL
def configurar_interfaz(ventana):
    """Configura la ventana principal de la operación.

    Args:
        ventana (tk.Tk): Ventana principal de la aplicación.

    Returns:
        None
    """
    ventana.title("Calculadora Básica Danna")
    ventana.geometry("350x600")
    ventana.config(bg="#000000")
    ventana.resizable(False, False)


#ACTUALIZAR EXPRESIÓN EN PANTALLA
def agregar_valor(valor, pantalla):
    """Agrega un valor a la operación y actualiza la pantalla.

    Args:
        valor (str): Valor que se agregará a la operación.
        pantalla (tk.Entry): Campo de texto donde se muestra la operación.

    Returns:
        None
    """
    global operacion

    #Concatenar el valor presionado a la operación actual
    operacion += str(valor)

    pantalla.delete(0, tk.END)
    pantalla.insert(0, operacion)


#AGREGAR ANS A LA OPERACIÓN
def agregar_ans(pantalla):
    """Reemplaza la operación actual por 'ans' y la muestra en pantalla.

    Args:
        pantalla (tk.Entry): Campo de entrada donde se muestra la operación.

    Returns:
        None
    """

    global operacion

    operacion = "ans"

    pantalla.delete(0, tk.END)
    pantalla.insert(0, operacion)


#LIMPIAR PANTALLA Y REINICIA LA OPERACIÓN
def limpiar_pantalla(pantalla):
    """Limpia la pantalla y reinicia la operación actual.

    Args:
        pantalla (tk.Entry): Campo de entrada donde se muestra la operación.

    Returns:
        None
    """
    global operacion

    operacion = ""
    pantalla.delete(0, tk.END)


#ELIMINAR EL ÚLTIMO DÍGITO DE LA OPERACIÓN
def borrar_ultimo(pantalla):
    """Elimina el último carácter de la operación actual.

    Args:
        pantalla (tk.Entry): Campo de entrada donde se muestra la operación.

    Returns:
        None
    """
    global operacion

    #Eliminar el último carácter ingresado
    operacion = operacion[:-1]

    pantalla.delete(0, tk.END)
    pantalla.insert(0, operacion)


#Formatea números eliminando .0 cuando no hay decimales
def limpiar_numero(n):
    """Formatea números eliminando decimales innecesarios.

    Args:
        n(int|float): Número a formatear.

    Returns:
        int|float: Número formateado.
    """
    return int(n) if isinstance(n, float) and n.is_integer() else n


#CALCULAR LA OPERACIÓN
def calcular_resultado(pantalla):
    """Evalúa la operación ingresada y muestra el resultado.

    Reemplaza operadores visuales, maneja 'ans', ejecuta la operación
    correspondiente y guarda el resultado en el historial.

    Args:
        pantalla (tk.Entry): Campo de entrada de la calculadora.

    Returns:
        None
    """
    
    #Usar variables globales para conservar el estado actual de la calculadora
    global operacion
    global ans

    #USAR EL RESULTADO ANTERIOR SI EL USUARIO ESCRIBE "ans"
    operacion = operacion.replace("ans", str(ans))

    #Reemplazar símbolos por operadores válidos
    operacion = operacion.replace("×", "*")
    operacion = operacion.replace("÷", "/")
    operacion = operacion.replace("−", "-")

    #Validación y cálculo de la operación
    try:
        if operacion == "":
            messagebox.showwarning("Campo vacío", "Ingrese una operación.")
            return

        #Guardar la expresión original para el historial
        operacion_original = operacion

        #Evaluar la expresión completa
        resultado = evaluar_expresion(operacion)

        #GUARDAR RESULTADO EN ans
        ans = resultado

        #Formatear el resultado
        resultado = limpiar_numero(resultado)

        pantalla.delete(0, tk.END)
        pantalla.insert(0, resultado)

        #Guardar la operación realizada en el historial
        guardar_historial(operacion_original, resultado)

        #Mantener el resultado como nueva operación
        operacion = str(resultado)


    #Manejo de errores
    except Exception as e:
        messagebox.showerror("Error", str(e))


#VENTANA DEL HISTORIAL
def ver_historial():
    """Abre una ventana con el historial de operaciones.

    Args:
        None
    
    Returns:
        None
    """
    
    datos = cargar_historial()

   #Crear ventana del historial
    ventana_hist = tk.Toplevel()
    ventana_hist.title("Historial")
    ventana_hist.geometry("350x400")
    ventana_hist.config(bg="#0f0f0f")

    #Crear área de texto para mostrar el historial
    texto = tk.Text(
        ventana_hist,
        bg="black",
        fg="#ff4fa3",
        font=("Segoe UI", 15)
    )
    texto.pack(expand=True, fill="both", padx=10, pady=10)

    #Mostrar contenido en el historial o mensaje vacío
    if not datos:
        texto.insert(tk.END, "Sin historial :( ")
    else:
        #Mostrar cada operación almacenada en el historial
        for item in datos:
            texto.insert(
                tk.END,
                f"{item.get('operacion','?')} = {item.get('resultado','?')} | {item.get('fecha','sin fecha')}\n"
            )


#CREAR E INICIAR INTERFAZ
def iniciar_interfaz():
    """Crea e inicia la interfaz gráfica de la calculadora.  

    Args:
        None

    Returns:
        None
    """

    ventana = tk.Tk()

    #CONFIRMACIÓN AL CERRAR VENTANA (X)
    def confirmar_salida():
        """Pregunta al usuario si desea cerrar la aplicación.

        Args:
            None

        Returns:
            None
        """

    #Devuelve True si el usuario confirma, False si cancela
        respuesta = messagebox.askyesno(
           "Salir",
           "¿Estás seguro que quieres salir?"
        )

        if respuesta:
            ventana.destroy()

    ventana.protocol("WM_DELETE_WINDOW", confirmar_salida)

    #Configurar propiedades principales de la ventana
    configurar_interfaz(ventana)

    #Hacer que las columnas ocupen el mismo espacio.
    for i in range(3):
        ventana.grid_columnconfigure(i, weight=1, uniform="cols")

    #Título
    titulo = tk.Label(
        ventana,
        text="Calculadora",
        font=("Segoe UI", 15, "bold"),
        bg="#0f0f0f",
        fg="white"
    )
    titulo.grid(row=0, column=0, columnspan=3, pady=10, sticky="nsew")

    #Campo donde se muestra la expresión
    pantalla = tk.Entry(
        ventana,
        font=("Segoe UI", 24),
        justify="right",
        bd=10,
        relief=tk.RIDGE,
        bg="black",
        fg="#ff4fa3",
        insertbackground="#ff4fa3"
    )
    pantalla.grid(row=1, column=0, columnspan=3, padx=8, pady=5, sticky="nsew")

    #Lista de botones de la calculadora
    botones = [
        "7", "8", "9",
        "4", "5", "6",
        "1", "2", "3",
        "0", ".", "=",
        "+", "−", "×",
        "÷", "C", "⌫"
    ]
    
    #Posición inicial en grid para organizar los botones
    fila = 2
    columna = 0

    #Crear los botones de la calculadora
    for boton in botones:

        if boton == "=":
            comando = lambda: calcular_resultado(pantalla)

        elif boton == "C":
            comando = lambda: limpiar_pantalla(pantalla)

        elif boton == "⌫":
            comando = lambda: borrar_ultimo(pantalla)

        else:
            comando = lambda v=boton: agregar_valor(v, pantalla)

        #Definir colores según el tipo de botón
        if boton in ["+", "−", "×", "÷", "="]:
            color_boton = "#f03f94"

        elif boton in ["C", "⌫"]:
            color_boton = "#FF0873"

        else:
            color_boton = "#f085b2"

        #Crear botón y asignar función según corresponda
        tk.Button(
            ventana,
            text=boton,
            font=("Segoe UI", 14, "bold"),
            bg=color_boton,
            fg="white",
            relief="flat",
            command=comando
        ).grid(
            row=fila,
            column=columna,
            padx=1,
            pady=1,
            ipadx=12,
            ipady=10,
            sticky="nsew",
        )
        
        #Moverse a la siguiente columna
        columna += 1
        
        #Salto de fila cuando se llenan 3 columnas
        if columna > 2:
            columna = 0
            fila += 1


    #BOTÓN HISTORIAL
    tk.Button(
        ventana,
        text="Historial",
        font=("Segoe UI", 14, "bold"),
        bg="#CA0849",
        fg="white",
        relief="flat",
        command=ver_historial
    ).grid(
        row=fila,
        column=0,
        padx=1,
        pady=1,
        ipadx=8,
        ipady=8,
        sticky="nsew",
    )

    #BOTÓN BORRAR HISTORIAL
    tk.Button(
        ventana,
        text="Borrar\nhistorial",
        font=("Segoe UI", 14, "bold"),
        bg="#CA0849",
        fg="white",
        relief="flat",
        command=borrar_historial
    ).grid(
        row=fila,
        column=1,
        padx=1,
        pady=1,
        ipadx=8,
        ipady=1,
        sticky="nsew",
    )

    #BOTÓN ANS
    tk.Button(
        ventana,
        text="ANS",
        font=("Segoe UI", 14, "bold"),
        bg="#EC1C38",
        fg="white",
        relief="flat",
        command=lambda: agregar_ans(pantalla)
    ).grid(
        row=fila,
        column=2,
        padx=1,
        pady=1,
        ipadx=8,
        ipady=8,
        sticky="nsew",
    )

    # Mantener la ventana en ejecución
    ventana.mainloop()