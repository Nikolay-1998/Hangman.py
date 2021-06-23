import prueba
import random
import os
def read_words(words_file):
    """ (file open for reading) -> list of str
    Return a list of all words (with newlines removed) from open file
    words_file.
    Precondition: Each line of the file contains a word in uppercase characters
    from the standard English alphabet.
    """
    lists = []
    for line in words_file:
        word = ''

        for character in line:

            if character != '\n':
                word = word + character

        lists.append(word)

    return lists

def pintar_estado_del_juego():
    clear()
    print()
    prueba.draw_lines(palabra_a_adivinar, letras_adivinadas)
    print()
    print("letras_adivinadas",letras_adivinadas)
    print("letras_erroneas",letras_erroneas)
    print("numero_de_intentos",total_de_intentos)


def clear():
    os.system('cls' if os.name in ('nt', 'dos') else 'clear')

archivo_palabras = open('words.txt',mode = 'r')
words = read_words(archivo_palabras)
archivo_palabras.close()

letras_erroneas =[]

letras_adivinadas =[]

total_de_intentos =0

gano = False

letra_ingresada =''

cicloqueimprime = 0

encontro_letra = False

yaesta = False

palabra_al_azar=''

palabra_a_adivinar=random.choice(words)

while total_de_intentos < 10 and gano == False:

    pintar_estado_del_juego()

    letra_ingresada = input("Ingrese una letra: ")

    yaesta = (letra_ingresada in letras_adivinadas) or (letra_ingresada in letras_erroneas)

    if yaesta is True:
        pintar_estado_del_juego()

    else:

        encontro_letra = False

        if letra_ingresada in palabra_a_adivinar:
            encontro_letra = True
            for i in range(palabra_a_adivinar.count(letra_ingresada)):
                letras_adivinadas.append(letra_ingresada)
        else:
            letras_erroneas.append(letra_ingresada)

        clear()

        pintar_estado_del_juego()

        pintar_estado_del_juego()

    if len(letras_adivinadas) == len(palabra_a_adivinar):
        gano = True

    total_de_intentos += 1

if gano == True:

    print("Felicidades! Ganaste el juego!""La palabra era", palabra_a_adivinar)

else:

    print("Concentrate un poco más en la próxima""La palabra era", palabra_a_adivinar)

