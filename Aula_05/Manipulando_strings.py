import os
os.system('cls')

#Função para tirar os espaços em branco 
texto= "      Olá Mundo com python"
print(texto.strip())

#Função replace substitui uma string por outra
texto= "O python é incrivel!!"
novo_texto = texto.replace("python", "Java")
print(novo_texto)

#Função split()divide a string em uma lista com base em um delimitador
texto ="Python, Java, C#"
linguangens = texto.split(", ")
print(linguangens)

#Função  starswitch
texto = "Python é incrivel!!"
print(texto.startswith("Python"))
print(texto.startswith("Java"))
