import os
import time

def animar_palavra(palavra):
    espaco = 0
    direcao = 1
    largura_terminal = os.get_terminal_size().columns
    
    while True:
        print(' ' * espaco + palavra)
        espaco += direcao
        
        if espaco > largura_terminal - len(palavra):
            direcao = -1
        elif espaco < 0:
            direcao = 1
        
        time.sleep(0.05)

def main():
    palavra = input("Digite a palavra: ")
    animar_palavra(palavra)

if __name__ == "__main__":
    main()
