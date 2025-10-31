import os
os.system('cls')

def somar(a,b):
    total = a+b
    print(total)

def substrair(a,b):
    total=a-b
    print(total)

def multiplicar(a,b):
    total=a*b
    print(multiplicar)

def dividir(a,b):
    total=a/b
    print(total)

numero_01=int(input("digite um numero: "))
numero_02=int(input("Digite um numero: "))
op=input("Digite a operação: ")

if(op =='+'):
    somar(numero_01,numero_02)
elif(op =="-"):
    substrair(numero_01,numero_02)
elif(op == "*"):
    multiplicar(numero_01,numero_02)
elif(op == "/"):
    dividir(numero_01,numero_02)
else:
    print("operação invalida!!")