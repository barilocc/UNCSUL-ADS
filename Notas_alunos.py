# Trabalho de Igor Strauss - RGM 5947848251
from metodos import validar_inscricao, calcular_media
def main():
    while True:
        nome = input("Digite o nome do aluno: (ou 'sair' para finalizar) ")
        if nome.lower() == 'sair':
            break
        notas = []
        for _ in range(4):
            nota = float(input("Digite a nota do aluno: "))
            while nota < 0 or nota > 10:
                print("Nota inválida. Digite uma nota entre 0 e 10.")
                nota = float(input("Digite a nota do aluno: "))
            notas.append(nota)
        categoria = validar_inscricao(notas)
        relatorio(categoria, notas, nome)

def relatorio(categoria, notas, nome):
    print(f"O aluno é um {categoria}.")
    print(f"Média do aluno: {calcular_media(notas):.2f}")
    print(f"O aluno {nome} foi classificado como {categoria}.")
if __name__ == "__main__":
    main()