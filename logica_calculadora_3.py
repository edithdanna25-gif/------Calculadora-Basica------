#SUMA
def sumar(*numeros):
    """Suma una cantidad de números.

    Args:
        *numeros (float): Números que se desean sumar.

    Returns:
        float: Resultado de la suma de todos los números.
    """
    #La función sum() realiza la suma de todos los elementos.
    return sum(numeros)


#RESTA
def restar(*numeros):
    """Resta una cantidad de números.

    El primer número se toma como valor inicial y los siguientes
    se restan en orden.

    Args:
        *numeros (float): Números que participan en la resta.

    Returns:
        float: Resultado de la resta.

    Raises:
        ValueError: Si no se proporcionan números.
    """
    #Validar que existan números para realizar las operaciones.
    if len(numeros) == 0:
        raise ValueError("Debe proporcionar al menos un número")

    #Tomar como base el primer número.
    resultado = numeros[0]

    #Restar los demás números.
    for numero in numeros[1:]:
        resultado -= numero

    return resultado



#MULTIPLICACIÓN
def multiplicar(*numeros):
    """Multiplica una cantidad de números.

    Args:
        *numeros (float): Números que se desean multiplicar.

    Returns:
        float: Resultado de la multiplicación.
    """
    #Inicializar resultado en 1 porque es el neutro multiplicativo.
    resultado = 1

    #Multiplicar cada número recibido.
    for numero in numeros:
        resultado *= numero

    return resultado


#DIVISIÓN
def dividir(*numeros):
    """Divide una cantidad de números.

    El primer número se toma como dividendo inicial y los siguientes
    se utilizan como divisores en orden.

    Args:
        *numeros (float): Números que participan en la división.

    Returns:
        float: Resultado de la división.

    Raises:
        ValueError: Si no se proporcionan números o si existe una
        división entre cero.
    """
    #Validar que existan números para operar.
    if len(numeros) == 0:
        raise ValueError("Debe proporcionar al menos un número")

    #Tomar el primer número como base
    resultado = numeros[0]

    #Dividir secuencialmente entre los demás números
    for numero in numeros[1:]:
        # Validar división entre cero
        if numero == 0:
            raise ValueError("No se puede dividir entre cero")

        resultado /= numero

    return resultado

#EVALUACIÓN DE EXPRESIÓN
def evaluar_expresion(expresion):
    """Evalúa una expresión matemática respetando la prioridad
    de multiplicación y división sobre suma y resta.

    Convierte la expresión en una lista de números y operadores.
    Primero resuelve multiplicaciones y divisiones, y después
    realiza sumas y restas.

    Args:
        expresion (str): Expresión en forma de string.

    Returns:
        float: Resultado de la expresión.
    """
    #Reemplazar símbolos visuales por operadores
    expresion = expresion.replace("×", "*")
    expresion = expresion.replace("÷", "/")
    expresion = expresion.replace("−", "-")

    #Separar números y operadores
    elementos = []
    numero = ""

    for c in expresion:
        if c in "+-*/":
            if numero == "":
                continue

            elementos.append(float(numero))
            elementos.append(c)
            numero = ""

        else:
            numero += c

    if numero != "":
        elementos.append(float(numero))

    #Resolver primero multiplicaciones y divisiones
    i = 0

    while i < len(elementos):

        if elementos[i] == "*":

            resultado = multiplicar(
                elementos[i - 1],
                elementos[i + 1]
            )

            elementos[i - 1:i + 2] = [resultado]
            i = 0

        elif elementos[i] == "/":

            resultado = dividir(
                elementos[i - 1],
                elementos[i + 1]
            )

            elementos[i - 1:i + 2] = [resultado]
            i = 0

        else:
            i += 1

    #Resolver sumas y restas de izquierda a derecha
    resultado = elementos[0]
    i = 1

    while i < len(elementos):

        operador = elementos[i]
        numero = elementos[i + 1]

        if operador == "+":
            resultado = sumar(resultado, numero)

        elif operador == "-":
            resultado = restar(resultado, numero)

        i += 2

    return resultado