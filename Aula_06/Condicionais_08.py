import os
os.system('cls')

nota_01=7
nota_02=8
nota_03=5
nota_04=6

media=(nota_01+nota_02+nota_03+nota_04)/4

if(media >=7):
    print(f"media: {media}\nAluno Aprovado! ")
elif (media >=5 and media <=7):
    print(f"media: {media}\nAluno de recuperação! ")
else:
    print(f"media: {media}\nReprovado! ")
