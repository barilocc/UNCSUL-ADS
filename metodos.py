# Trabalho de Igor Strauss - RGM 5947848251
def calcular_media(notas):
    if len(notas) == 0:
        return 0
    return sum(notas) / len(notas)

def validar_inscricao(notas):
    idade = int(input("Digite a idade do aluno: "))
    renda = float(input("Digite a renda familiar do aluno: "))
    if calcular_media(notas) >= 7:
        if idade >= 18:
            if renda <= 2000:                
                categoria = "candidato bolsa"
                return categoria
            else:
                categoria = "candidato regular"
                return categoria
        else:
            categoria = "candidato menor de idade"
            return categoria
    else:
        categoria = "candidato reprovado"
        return categoria