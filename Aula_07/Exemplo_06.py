import os
os.system('cls')
import time

cont =0

while(True):
    numero = int(input("Digite um numero: "))
    if numero>=0:
        break
    cont+=1

    print(f"Você digitou {cont} numeros negativos ")