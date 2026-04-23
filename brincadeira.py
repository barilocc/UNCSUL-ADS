# Trabalho de Igor Strauss - RGM 5947848251
# JOGO DE ADIVINHAÇÃO DE NÚMEROS

from random import randint

def jogar():
    tentativa = 1
    
    print('\n' + '='*40)
    print('       BEM-VINDO AO JOGO DE ADIVINHAÇÃO')
    print('='*40 + '\n')
    
    # Escolher dificuldade
    while True:
        try:
            dificuldade = int(input('Escolha a dificuldade do jogo:\n1 - Fácil (1-100)\n2 - Médio (1-500)\n3 - Difícil (1-1000)\n\nOpção: '))
            
            if dificuldade not in [1, 2, 3]:
                print('⚠️  Resposta inválida! Digite 1, 2 ou 3.\n')
                continue
            break
        except ValueError:
            print('⚠️  Digite um número válido!\n')
    
    # Definir intervalo conforme dificuldade
    if dificuldade == 1:
        max_numero = 100
        print('\n🎮 Modo: Fácil - Escolha um número entre 1 e 100')
    elif dificuldade == 2:
        max_numero = 500
        print('\n🎮 Modo: Médio - Escolha um número entre 1 e 500')
    else:
        max_numero = 1000
        print('\n🎮 Modo: Difícil - Escolha um número entre 1 e 1000')
    
    # Máquina escolhe o número
    n_maquina = randint(1, max_numero)
    print(f'A máquina escolheu um número... Adivinhe qual é!\n')
    
    # Loop do jogo
    while True:
        try:
            n_usuario = int(input(f'Tentativa {tentativa} - Digite um número (1-{max_numero}): '))
            
            if n_usuario < 1 or n_usuario > max_numero:
                print(f'⚠️  Digite um número entre 1 e {max_numero}!\n')
                continue
            
            if n_usuario == n_maquina:
                break
            elif n_usuario < n_maquina:
                print(f'📈 O número é MAIOR que {n_usuario}. Tente novamente!\n')
            else:
                print(f'📉 O número é MENOR que {n_usuario}. Tente novamente!\n')
            
            tentativa += 1
        except ValueError:
            print('⚠️  Digite um número válido!\n')
    
    # Fim do jogo
    print('\n' + '='*40)
    print(f'🎉 PARABÉNS! Você acertou em {tentativa} tentativa(s)!')
    print(f'O número era: {n_maquina}')
    print('='*40 + '\n')
    
    return tentativa

# Programa principal
if __name__ == '__main__':
    while True:
        pontos = jogar()
        
        while True:
            jogar_novamente = input('Deseja jogar novamente? (S/N): ').strip().upper()
            if jogar_novamente in ['S', 'SIM', 'YES', 'Y']:
                break
            elif jogar_novamente in ['N', 'NÃO', 'NAO', 'NO']:
                print('\n👋 Obrigado por jogar! Até logo!\n')
                exit()
            else:
                print('⚠️  Digite S para Sim ou N para Não.\n')

