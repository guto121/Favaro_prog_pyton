import os
os.system('cls')

#criando as listas
frutas =["maça ","banana","laranja","uva"]
numeros =[1,2,3,4,5,6]
mista =[1,"texto",3.14,True]

#imprimindo os elementos da lista 
print(frutas[0])
print(frutas[-1])
print(frutas[1:4])

#adicionando elemento na lista
frutas.append("abacaxi")
print(frutas)
print(frutas[-1])

#adicionando elementos em uma posição especifica 
frutas.insert(2,"kiwi")
print(frutas)

numeros.append(7)
print(numeros)

numeros.insert(0,0)
print(numeros)