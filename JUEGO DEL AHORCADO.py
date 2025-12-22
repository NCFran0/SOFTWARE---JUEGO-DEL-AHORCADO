while True:
    print ("Bienvenido al juego del ahorcado")
    print("Elige la dificultad del juego")
    print("1. Difícil🔴 (4 intentos)")
    print("2. Normal🟡 (6 intentos)")
    print("3. Fácil🟢 (8 intentos)")
    dificultad=input("Dificultad: ")
    if dificultad == "1":
        intentos=4
        print("La dificultad será Díficil")
    elif dificultad == "2":
        intentos=6
        print("La dificultad Normal")
    elif dificultad == "3":
        intentos=8
        print("La dificultad será Fácil")
    else:
        print("Dificultad inválida, la dificultad será Normal")
        intentos=6
#El jugador elige la dificultad que quiera en el input, y segun este se asignan el número de intentos en las líneas 8-19.
    import random
    palabras= ("manzana","pera","banana","perro","gato","raton","casa","carro") #banco de palabras donde se guardan las palabras para el juego
    palabra_secreta= random.choice(palabras)
#importamos el módulo "random" para elegir aleatoriamente una palabra_secreta de las palabras

    guiones= ["_"]* len(palabra_secreta)
#len cuenta los elementos de la palabra
    print(guiones)
#imprimimos tantos guiones como letras tenga la palabra
    while intentos >0:
#iniciamos un bucle que se encarga de que el juego siga si el jugador tiene mas de 0 intentos
        letra=input("Ingresa una letra: ")
        if len(letra) ==1 and letra.isalpha(): #si la cantidad de letras ingresadas es 1 y la letra es del abecedario:
            if letra in palabra_secreta: 
                for i in range(len(palabra_secreta)):# cuenta cuantas letras tiene la palabra secreta y crea una secuencia de números segun la palabra
                    if palabra_secreta[i] == letra:
                        guiones[i] = letra
        
            else:
                intentos -= 1
                print("Letra incorrecta, te quedan",intentos,"intentos.")
                #restamos intentos si la letra elegida no esta en la palabra_secreta
        else:
            print("Error, solo puedes ingresar un caractér del abecedario⚠️")
    
        print(" ".join(guiones))#espacios para una mejor visualización de la palabra

        if "_" not in guiones:
            print("Felicidades, completaste la palabra, ganaste!🥳")
            break
    #si no hay más guiones en la palabra a adivinar, se asume que ganó el juego.
    if intentos == 0:
        print("Te quedaste sin intentos, perdiste. 🥹")
    #caso contrario, donde no se completan los guiones antes de acabar los intentos
    while True:
    #bucle para la función de "volver a jugar"

        jugar_otra=input("Quieres jugar de nuevo? si/no: ")
        if jugar_otra =="si":
            jugar_otra= True
            break
        elif jugar_otra =="no":
            jugar_otra= False
            break
        else:
            print("Error, respuesta inválida, solo puedes ingresar si o no⚠️")
    if not jugar_otra:
        print("Gracias por jugar🫂")
        break
    #rompe el bucle si no se desea jugar de nuevo