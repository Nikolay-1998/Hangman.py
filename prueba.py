def draw_lines(palabra,letras):
    print("Letras a adivinar: ", end='')
    for letra in palabra:
        if letra in letras:
            print(letra, end='')
        else:
            print(" _ ", end='')