import os
import time

def move_word(word, height):

    while True:
        for i in range(height):
            os.system('cls' if os.name == 'nt' else 'clear')
            print(' ' * i + word)
            time.sleep(0.001)

        for i in range(height - 1, -1, -1):
            os.system('cls' if os.name == 'nt' else 'clear')
            print(' ' * i + word)
            time.sleep(0.001)

if __name__ == "__main__":
    while True:
        palavra = input("Digite a palavra que deseja mover (ou 'sair' para encerrar): ")
        if palavra.lower() == 'sair':
            break
        altura = 100
        move_word(palavra, altura)
