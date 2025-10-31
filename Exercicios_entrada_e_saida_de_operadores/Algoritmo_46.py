import math
import os
os.system('cls')

#Forma 1

saldo = float(input("Digite o seu saldo: "))
novo_saldo = saldo+(saldo*0.01)
print(novo_saldo)

#Forma 2

saldo1 =(saldo/100)*1
novo_saldo=saldo+saldo1
print(novo_saldo)
