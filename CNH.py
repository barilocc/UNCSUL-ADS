# Trabalho de Igor Strauss - RGM 5947848251

nome = input('Digite seu nome: ')
idade = int(input('Digite sua idade: '))
país = input('Digite seu país: ')

while país.lower() not in ['brasil', 'estados unidos']:
    print('País inválido! Por favor, digite "Brasil" ou "Estados Unidos".')
    país = input('Digite seu país: ')

if país.lower() == 'brasil' and idade >= 18:
    print(f'{nome}, você pode tirar a CNH no Brasil.')
if país.lower() == 'estados unidos' and idade >= 16:
    print(f'{nome}, você pode tirar a CNH nos Estados Unidos.')
else:
    print(f'{nome}, você ainda não pode tirar a CNH.')