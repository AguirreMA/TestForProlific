import random

def resolver_paso_a_paso(cadena, reglas):
    pasos = [cadena]

    while any(caracter in reglas for caracter in cadena):
        nueva_cadena = ""
        for caracter in cadena:
            if caracter in reglas:
                nueva_cadena += random.choice(reglas[caracter])
            else:
                nueva_cadena += caracter
        cadena = nueva_cadena
        pasos.append(cadena)

    return pasos

# Solicitar al usuario ingresar el conjunto de reglas
conjunto_reglas = {}
while True:
    simbolo = input("Ingrese un símbolo del conjunto (o 'fin' para terminar): ")
    if simbolo.lower() == 'fin':
        break
    opciones = input("Ingrese las opciones para {}: ".format(simbolo)).split('|')
    conjunto_reglas[simbolo] = opcionesm

# Solicitar al usuario ingresar la cadena inicial
cadena_inicial = input("Ingrese la cadena inicial: ")

# Resolver el conjunto paso a paso
pasos_resolucion = resolver_paso_a_paso(cadena_inicial, conjunto_reglas)

# Imprimir los pasos de la resolución
for i, paso in enumerate(pasos_resolucion):
    print("Paso {}: {}".format(i + 1, paso))