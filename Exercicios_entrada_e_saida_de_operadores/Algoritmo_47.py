import os
os.system('cls')

numero = "123"
numero_invertido =numero[::-1]


print(f"O numero invertido '{numero_invertido}'")


#explicação

num=int(input("digite um numero: "))
print(num)
centena=num// 100
dezena=(num&100)// 10
unidade=num%10
num_invertido=unidade*100+dezena*10+centena
print(num_invertido)