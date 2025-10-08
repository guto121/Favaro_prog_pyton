#Importando a Biblioteca matematica

import math
import os
os.system('cls')

# Funções Basicas


#raiz quadrada
#sqrt = funções raiz quadrada 
valor_01 = 9
valor_02 = 3

print(math.sqrt(valor_01))
print(math.sqrt(valor_02))

#Potência ou exponenciação

#pow= operações de potenciação 
print(math.pow(2,3))

#fazendo a mesma coisa,mas puxando as variáveis
print(math.pow(valor_01,valor_02))

semMatch=2**3
print(semMatch)

#Arredondar para cima
print(math.ceil(3.2))
print(math.ceil(-1.8))

#Arrendondando para baixo
print(math.floor(3.2))
print(math.floor(-1.8))

#Valor absoluto
print(math.fabs(-10))
print(math.fabs(7.5))

