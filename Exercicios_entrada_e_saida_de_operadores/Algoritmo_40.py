import os
os.system('cls')

dividendo = float(input("Digite o dividendo: "))
divisor = float(input("Digite o divisor: "))

quociente = divisor/ dividendo

resto = dividendo%divisor

print(f"\nDividendo é: {dividendo} \nO divisor é: {divisor} \nO quociente é: {quociente} \nE por fim, o resto é: {resto}")
