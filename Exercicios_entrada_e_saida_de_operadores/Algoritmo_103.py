import os
os.system('cls')

ano = int(input("Digite o ano do seu nascimento: "))
anoAtual = int(input("Digite o ano atual: "))


if(anoAtual - ano !=0 and anoAtual-ano <=100):
    idade =anoAtual - ano
    print(f"Idade {idade}")
else:
    print("Data invalida ")