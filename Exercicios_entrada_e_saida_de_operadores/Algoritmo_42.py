import math
import os
os.system('cls')

angulo = float(input("Digite o angulo: "))

rad=math.radians(angulo)

print("seno")
print(math.sin(rad))


print("cosseno")
print(math.cos(rad))


print("Tangente")
print(math.tan(rad))


print("Secante")
print(1/math.cos(rad))


print("Co-secante")
print(1/math.sin(rad))


print("Co-Tangente")
print(1/math.tan(rad))



