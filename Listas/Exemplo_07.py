import os
os.system('cls')

pessoa = {
    "nome:":"João"
    "idade":30
    "cidade":"São paulo"
}

pessoa["nome"]="paulo"
print(pessoa)

pessoa.update({"estado":"SP"})
print(pessoa)
pessoa.update({"endereço": "Rua Java Ali , 74","CEP":"98933-500"})
print(pessoa)

pessoa.pop("email")
print(pessoa)

pessoa.popitem()
print(pessoa)

del pessoa("endereço")
print(pessoa)

pessoa.clean()
print(pessoa)

pessoa(len{pessoa})