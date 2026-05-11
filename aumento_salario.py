#Trabalho de Igor Strauss - RGM 5947848251

nome = input('Digite seu nome: ')
salario = float(input('Digite seu salário atual: R$ '))
tempo_trabalho = int(input('Digite o tempo de trabalho em anos: '))
meta_trabalho = int(input('quanto da meta você atingiu em porcentagem: '))

while meta_trabalho < 0 or meta_trabalho > 100:
    print('Valor inválido! Por favor, digite um valor entre 0 e 100.')
    meta_trabalho = int(input('quanto da meta você atingiu em porcentagem: '))

if  tempo_trabalho >= 5 and meta_trabalho >= 80:
    aumento = salario * 0.30
    novo_salario = salario + aumento
    print(f'{nome}, você recebeu um aumento de 20%. Seu novo salário é: R$ {novo_salario:.2f}')
elif tempo_trabalho >= 5 and meta_trabalho < 80:
    aumento = salario * 0.20
    novo_salario = salario + aumento
    print(f'{nome}, você recebeu um aumento de 20%. Seu novo salário é: R$ {novo_salario:.2f}')
elif tempo_trabalho < 5 and meta_trabalho >= 80:
    aumento = salario * 0.10
    novo_salario = salario + aumento
    print(f'{nome}, você recebeu um aumento de 20%. Seu novo salário é: R$ {novo_salario:.2f}')
else:
    print(f'{nome}, você não recebeu um aumento. Seu salário permanece: R$ {salario:.2f}')