#trabalho de igor strauss - RGM 5947848251
tentativa = 1
from random import randint

print ('\nACERTE O NÚMERO!!\n')

n_maquina = randint (1, 100) #gera um número de 1 a 100
n_usuario = int(input('escolha um número de 1 a 100: '))

while n_usuario != n_maquina:
    if n_usuario < n_maquina:
        print('O número é maior. Tente novamente\n ')
    else:
        print('O número é menor. Tente novamente\n')
    tentativa += 1
    n_usuario = int(input('escolha um número de 1 a 100: \n'))
    
else:
    print('='*30)
    print (f" ACERTOU!!!! em {tentativa} tentativas 🎉")
    print('='*30)


