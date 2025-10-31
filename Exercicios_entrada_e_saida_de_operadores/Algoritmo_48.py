import os
os.system('cls')
import math

salario=(float(input("Digite o seu salario: ")))
quilowatts=(float(input("Digite a quantidade de quilowatts: ")))
valor_por_quilowatts= (salario/7)/100
valor_a_pagar=quilowatts*valor_por_quilowatts
valor_com_desconto=valor_a_pagar-(valor_a_pagar*0.10)

print(f"O valor por quilowatts: {quilowatts}")
print(f"o valor a ser pago: R$ {valor_a_pagar} ")
print(f"O valor com desconto: R$ {valor_com_desconto}")


