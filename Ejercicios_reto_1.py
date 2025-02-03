# Ejercicio 1: operaciones básicas
def b_operations(numero_1, numero_2, operacion):
    """La función b_operations realiza operaciones aritméticas entre dos 
    números enteros y un signo proporcionados por el usuario.
    
    Args

    numero 1: primer número con el que se quiere operar.
    numero 2: segundo número con el que se quiere operar.
    operación: corresponde al signo de la operación que se desee realizar
    (+, -, /, *).
    """

    # Verificaciones de tipos de datos
        # Verificación de que los argumentos "números" sean enteros
    if type(numero_1) != int or type(numero_2) != int:
        print("No ha ingresado números enteros a la función")
        return None
    else:
        numero_1 = str(numero_1) ; numero_2 = str(numero_2)

        #  Validación del signo proporcionado
    signos_validos = ["+", "-", "*", "/"]
    
    if operacion not in signos_validos:
        print("No se puede realizar una operación válida " 
              "con el signo que proporciono")
        return None

    # Operaciones y entrega de resultados
    try:
        operacion = numero_1 + operacion + numero_2
        resultado_op = eval(operacion)
        
        print(f"El resultado de {numero_1}{operacion}{numero_2} "
              f"es {resultado_op}")
        
        return resultado_op
    except ZeroDivisionError:
        print ("No se puede realizar una division entre 0.")
        return None

# Ejercicio 2: palindromos
def palindrome_verifier(palabra = None):
    """La función palindrome_verifier comprueba que la palabra proporcionada
    sea un palindromo, retornando 'True' en el caso de que la palabra sea uno y
    'False' en caso negativo.

    Args:
    palabra: corresponde a la palabra que se quiere comprobar si es un
    palindromo, tiene un valor de None por defecto.
    """
    try:
        # En caso de que el usuario no ingrese un argumento a la función
        if palabra == None:
            print("Debe ingresar un argumento a la función")
            return None

        # Verificación del tipo de dato que proporciono el usuario
        if palabra.isdigit():
            print("Debe ingresar palabras")
            return None
        
        # Minusculización de la palabra que ingreso el usuario
        palabra = palabra.lower()

        # Revertir la palabra original para ver si es un palindromo
        supuesto_palindromo = ""
        indice = -1
        
        for i in palabra: # El ciclo itera por cada letra que tenga la palabra 
            constructor = (palabra[indice])# Toma la última letra de la palabra
            indice -= 1

            supuesto_palindromo = supuesto_palindromo + constructor
        
        # Verificacion de la similitud entre el supuesto palindromo y 
        # la palabra proporcionada

        # Caso en el que la palabra no sea un palindromo
        if supuesto_palindromo != palabra:
            print("La palabra que ingreso no es un palíndromo")
            return False

            # Caso en el que la palabra no sea un palindromo
        if supuesto_palindromo == palabra:
            print("La palabra que ingreso es un palíndromo")
            return True
    except AttributeError:
        # En caso de que palabra no sea un str
        print("Solo se permiten cadenas de texto.")
        return None

# Ejercicio 3: números primos en una lista
def prime_finder(lista):
    """La función prime_finder encuentra y devuelve los números primos que se 
    encuentren dentro de la lista de números enteros proporcionada.

    Args:
    lista: representa la lista de números de la que se quiere extraer los
    números primos.
    """
    try:
        # Revisión de que todos los elementos sean números enteros
        for cada_elemento in lista:
            if type(cada_elemento) == int:
                continue
            else:
                print("La lista que ingreso contiene elementos no válidos "
                    "(valores que no son números enteros.)")
                return None
                    
        # Obtencion de numneros primos de la lista
            # Obtención de los divisores de cada número
        
        Numeros_primos = [] # Lista que contiene los números primos encontrados
            
            # En este caso se supone que todos los elementos de la lista son 
            # primos hasta demostrar lo contrario, representado en la variable 
            # validez.

        for numero in lista:
            validez = True

            # Aqui se generan los divisores del numero
            for Divisores in range(2, int(numero**0.5) + 1):
                if numero % Divisores == 0:
                    validez = False
                    break
            
            # 1 no se considera un numero primo  
            if numero < 2:
                validez = False

            if validez == True:
                Numeros_primos.append(numero)

            validez = True # Reinicio de la variable validez para seguir 
                           # agregando elementos a la lista Numeros_primos 

        if len(Numeros_primos) == 0:
                print("Dentro del rango que ingreso no existen numeros primos")
                return None
        else:
            print(f"Los numeros primos encontrados son: {Numeros_primos}")
            return Numeros_primos
    except TypeError:
        print(f"El elemento que ha ingresado no es iterable, ej. (None)")
        return None

# Ejercicio 4: recibir una lista de numeros enteros y retornar la mayor suma 
# entre dos elementos consecutivo
def consecutive_sum(lista):
    """La función consecutive_sum realiza una suma con los elementos 
    consecutivos de una lista proporcionada y devuelve la que sea mayor.

    Args:
    lista: corresponde a la lista con los elementos que se van a sumar.
    """
    try:
        # Revisión de que todos los elementos sean números enteros
        for cada_elemento in lista:
            if type(cada_elemento) == int:
                continue
            else:
                print("La lista que ingreso contiene elementos no válidos "
                    "(no númericos o no enteros)")
                return None      
        
        # Suma de elementos consecutivos
        sumas = [] # Lista que lmacena las sumas parciales
        indice = 1 # Indice del elemento consecutivo

        # Realización de las sumas
        for numero in lista:    
            # Para evitar una excepción del tipo indexerror
            if indice == len(lista):
                break
            Suma_parcial = numero + lista[indice]

            sumas.append(Suma_parcial)
            indice += 1
        
        # Organización de los elementos de la lista "sumas"
        sumas.sort()
        print(f"La mayor suma de elementos consecutivos es: {sumas[-1]}")
        return (sumas[-1])
    except TypeError:
        print(f"El elemento que ha ingresado no es iterable, ej. (None)")
        return None
    except IndexError:
        print(f"La lista que ha proporcionado no posee pares de elementos.")
        return None

# Ejercicio 5: anagramas
def same_caracters(string_lista): 
    """la función same_caracters evalúa qué elementos de la lista son 
    anagramas.
    
    Args:
    string_lista: lista que contiene los elementos que son considerados como
    supuestos anagramas.
    """
    try:
        # Filtro para tipos de datos no válidos
        for cada_elemento in string_lista:
            if cada_elemento.isdigit ():
                print ("La lista contiene tipos de datos no validos")
                return None
    except AttributeError:
        print("La lista que proporciono contine elementos no validos como "
              "(int,float,bool).")
    
    # Lista para almacenar los anagramas encontrados
    final_list = []
    
    # Comparación de anagramas
    for repeticion in range(len(string_lista)): # Recorre la lista
        # Recorre el indice consecutivo al elemento del ciclo anterior ^
        for elemento_comparable in range(repeticion + 1, len (string_lista)):
            # Se ordenan los caracteres de ambas palabras para compararlos
            # como tienen los mismos caracteres entonces cuando se 
            # organicen alfabeticamente, estos seran iguales y se añadiran 
            # a "final_list"
            try:
                if sorted(string_lista[repeticion]) == sorted(
                    string_lista[elemento_comparable]
                    ):
                    final_list.append([
                        string_lista[repeticion], 
                        string_lista[elemento_comparable]
                        ])
            except TypeError:
                print("La lista que proporciono contine elementos no validos "
                      "como (int,float,bool).")
                return None

    # Resultados de la comparación
    # Si la lista no esta vacia, se imprimen los anagramas encontrados y 
    # retorna "Final_list"
    if len (final_list) != 0:
        print("Anagramas encontrados en la lista proporcionada:", final_list)
        return final_list
    else:
        print("No se encontraron anagramas en la lista que proporciono")
        return None

# Ejemplos de uso
b_operations (9, 5, "*")

palindrome_verifier ("Hannah")
palindrome_verifier ("Carlos")

lista_1 = [1, 3, 4, 56, 97, 1542, 163,33, 47]
prime_finder (lista_1)

lista_2 = [1,2,6,7,5,3,4,8,1,3,5]
consecutive_sum (lista_2)

lista_3 = ["rosa", "roma", "mora", "amor", "sora", "pepe", "perro", "manzana"]
same_caracters (lista_3)