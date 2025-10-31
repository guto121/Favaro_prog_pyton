import math
import os
os.system('cls')

def somar(a,b):
    total =a+b
    return total

def raizQuadrada(a):
    raiz=math.sqrt(a)
    print(raiz)

print("Função somar sem parametros ")

print("Função somar com parametros ")
num_01=int(input("Digite um numero: "))
num_02=int(input("Digite um numero: "))

print("Função somar recebendo os parametros")
raiz2= somar(num_01,num_02)

print("Função raizQuadrada recebendo o returno da função somar")
raizQuadrada(raiz2)