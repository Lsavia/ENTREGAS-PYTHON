
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

categorias ={"conceptos de programacion" : ["variable","funcion","bucle"],
              "tipos de datos" : ["entero","cadena","lista"], "lenguaje" : ["python","programa"]}

print("elije una de estas categorias:","  conceptos de programacion;"," tipos de datos;",
            " lenguajes;")
cat = input("ingrese el nombre de la categoria: ")
while cat not in categorias :
    print (" la categoria seleccionada no pertenece a una existente, elija denuevo")
    cat = input("ingrese el nombre de la categoria: ")
dato = categorias [cat]

print(cat)

word = random.choice(categorias[cat])
guessed = []
attempts = 6
print("¡Bienvenido al Ahorcado!")
print()
puntaje = 0




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

print(" tu puntaje final es: ", puntaje)