print ("Bienvenido al juego del ahorcado")
import random
palabras= ("manzana","pera","banana","perro","gato","raton","casa","carro")
palabra_secreta= random.choice(palabras)

"""En este apartado se pone un banco de palabras temporal con 8 palabras
para el desarrollo y prueba del código, también se añade la funcion de random.choice para que se elija una palabra al azar
del banco de palabras"""

guiones= ["_"]* len(palabra_secreta)
print(guiones)

"""estas lineas de codigo se encargan de imprimir en una lista tantos guiones como letras tenga la palabra secreta a adivinar el juego
(len) se encarga de ver la cantidad de letras que tiene la palabra secreta, los [] son los que lo hacen una lista"""

while True:
    letra = input("Ingresa una letra: ").lower()

    if len(letra) == 1 and letra.isalpha():

        if letra in palabra_secreta:
            for i in range(len(palabra_secreta)):
                if palabra_secreta[i] == letra:
                    guiones[i] = letra
                    """ aqui comparamos la posicion de las letras en i con la letra del input (linea 23) y remplazamos los guiones por la letra si es correcta (linea 24)
                    range crea una secuencia de números en funcion de la cantidad de letras de la palabra secreta en (len(palabra_secreta))
                    (i) es la indice de posicion de letras, por ejemplo 0 es la primera letra, en "perro" la p es 0"""
        else:
            print("La letra es incorrecta")

        print(" ".join(guiones))
        

    else:
        print("Error, solo puedes ingresar UN carácter")

    
"""en este apartado, se crea un bucle (while true) en el que si la letra no esta dentro de la palabra_secreta y/o no es un solo caracter,
imprime un mensaje de que la letra es incorrecta o que solo se puede ingresar un caracter segun corresponda. En caso contrario reemplaza la letra
correcta con los guiones que correspondan y asi sucesivamente hasta que terminemos de rellenar la palabra"""
