import os
os.system('cls')

sigla=input("Digite a sicla da sua cidade: ")
uf = sigla.upper()

if(uf =="SP"):
    print("Paulista")
elif(uf == "MG"):
    print("mineiro")
elif(uf == "RJ"):
    print("Carioca")
else:
    print("Outros estados ")