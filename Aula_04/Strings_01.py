import os
os.system('cls')

#Função len() - conta o tamanho da string

texto= "Olá Mundo"
tamanho = len(texto)

print(f"O tamanho da string '{tamanho}")

#Texto todo em letra maiuscula 
texto_maiusculo = texto.upper()
print(f"o Texto em letra minuscula '{texto_maiusculo}'")

#Texto com letra minuscula 
texto_minusculo = texto_maiusculo.lower()
print(f"O texto em letra minuscula'{texto_minusculo}'")

#invertendo a posição da string 
texto_invertido =texto[::-1]
print(f"string invertida '{texto_invertido}'")