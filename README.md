# SOFTWARE---JUEGO-DEL-AHORCADO
En este repositorio se encuentran diagramas de arquitectura, caso de uso y flujo entorno al software del Juego del Ahorcado, avance de código y su código final, así mismo un video explicativo del avance y una breve presentación donde se explican las funcionalidades del juego.

Funcionalidades del código:

Este código es del juego del ahorcado, con lenguaje de programación Python, que se ejecuta de manera continua mientras el jugador quiera seguir jugando. Al iniciar el código, se muestra un menú para seleccionar la dificultad, donde según que seleccione el jugador, se le darán una "x" cantidad de intentos, y en este caso disponemos de 3 dificultades: Díficil(4 intentos), Normal(6 intentos) y Fácil(8 intentos). El código también se encarga de que, en caso de que el jugador seleccione otra dificultad o ingrese algo que no tenga que ver con la dificultad, se seleccione la dificultad predeterminada: Normal (6 intentos).

Después, el programa selecciona al azar una palabra al azar desde un banco de palabras, donde importamos previamente el módulo random. En función de la longitud de la palabra, se generaran guiones que ocultarán las letras de la palabra, y que posteriormente nos indicarán nuestro progreso en el juego.

Durante el desarrollo del juego, el jugador ingresa letras para poder adivinar la palabra secreta. El código se encarga de que la entrada de caractéres sea una sola letra y que sea parte del alfabeto. Si la letra cumple estas dos condiciones, el código analiza si la letra es correcta o no, si lo es, se reemplazan los guiones por la letra según corresponda en donde aparezca. Si es incorrecta, se le quita 1 intento al jugador y se le muestra un mensaje para su conocimiento. El estado del juego se muestra después de cada intento.

Para que el juego finalice tenemos que cumplir una de las dos condiciones, ganar o perder. Para ganar, el código no debe detectar guiones en la palabra secreta, en su defecto, que el jugador haya adivinado todas las palabras antes de quedarse sin intentos, mostrando un mensaje de que ha ganado. Si se queda sin intentos antes de que se acaben los guiones, se le muestra que ha perdido. En cualquiera de estos dos casos, se muestra la opción de volver a jugar, y dependiendo de la respuesta del jugador, el juego se reiniciará o en su defecto, finalizara, mostrando un aviso de "Gracias por Jugar".

Objetivo del programa:

Desarrollar un juego del ahorcado que permita al jugador adivinar palabras de forma interactiva, reforzando el vocabulario y aplicando conceptos básicos de programación.

Fecha: 21 de Diciembre del 2025
