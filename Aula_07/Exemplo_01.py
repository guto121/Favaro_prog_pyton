import os
os.system('cls')
import time

cont = 10

while(cont >0):
    print("Volta: ",cont)
    time.sleep(0.50)
    cont -=1 #cont = cont -1

    cont = 0

    while(cont <=10):
        print("Volta: ",cont)
        time.sleep(0.50)
        cont +=1 #cont = cont+1
