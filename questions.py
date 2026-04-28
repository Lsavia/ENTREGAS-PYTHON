
import random
words = [
"python",
"programa",
"variable",
"funcion",
"bucle",
"cadena",
"entero",
"lista",
]

##diccionario de categorias con listas dentro

categorias ={"conceptos de programacion" : ["variable","funcion","bucle"],
              "tipos de datos" : ["entero","cadena","lista"], "lenguajes" : ["python","programa"]}




print("¡Bienvenido al Ahorcado!")
print()
puntaje = 0
jugar_denuevo =True


while jugar_denuevo == True :
    guessed = []
    attempts = 6

    print("elije una de estas categorias:","  conceptos de programacion;"," tipos de datos;",
            " lenguajes;")
    cat = input("ingrese el nombre de la categoria: ")
    while True :
        if cat not in categorias :
            print (" la categoria seleccionada no pertenece a una existente, elija denuevo")
            cat = input("ingrese el nombre de la categoria: ")
            continue
        elif len(categorias[cat]) ==0 :
            print(" en la categoria seleccionada ya no quedan mas palabras")
            cat = input("ingrese el nombre de otra categoria: ")
            continue
        break

    print(" has seleccionado la categoria ",cat)

    word = random.sample(categorias[cat],1)[0]
    categorias[cat].remove(word)

    while attempts > 0:
        
        # Mostrar progreso: letras adivinadas y guiones para las que faltan
        progress = ""
        for letter in word:
            if letter in guessed:
                progress += letter + " "
            else:
                progress += "_ "
        print(progress)
    # Verificar si el jugador ya adivinó la palabra completa
        if "_" not in progress:
            puntaje += 6
            print("¡Ganaste!", " has sumado 6 puntos")
            break
        print(f"Intentos restantes: {attempts}")
        print(f"Letras usadas: {', '.join(guessed)}")
        letter = input("Ingresá una letra: ")
        if len(letter)>1:
            print(" entrada no valida")
            continue
        if letter in guessed:
            print("Ya usaste esa letra.")
        elif letter in word:
            guessed.append(letter)
            print("¡Bien! Esa letra está en la palabra.")
        else:
            guessed.append(letter)
            attempts -= 1
            puntaje -=1
            print("Esa letra no está en la palabra."," se te resto un punto")
        print()
    else:
        print(f"¡Perdiste! La palabra era: {word}")
        puntaje = 0
    nueva_partida =input("queres jugar denuevo?, responda con SI, o con NO")
    if nueva_partida =="NO":
        jugar_denuevo ==False
        break

    if all(not lista for lista in categorias.values()):
      ##checkea si no hay mas valores en el diccionario de categorias
      print("No quedan palabras en ninguna categoría.")
      jugar_denuevo ==False
      break

print("Has finalizado la partida !!. Tu puntaje final es: ", puntaje, " !!")
