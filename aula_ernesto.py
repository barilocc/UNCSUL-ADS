import math

#trabalho de igor strauss

print ('SEJA BEM VINDO. RESPONDA AS QUESTÕES ABAIXO: ')

emprestimo = float(input("qual será o valor do emprestimo? "))
faturamento_mensal = float(input('qual o seu faturamento mensal? '))
score = int(input('qual o seu historico de credito? '))
ano_fund = int(input('A quanto tempo a empresa existe? (coloque apenas o número)'))
setor = str(input('qual o setor da empresa? ')).lower()

valor_parcela = math.ceil (emprestimo / 24)

if ano_fund > 2 or setor == "tecnologia":
    if valor_parcela <= (faturamento_mensal  *0.30):
        if score >= 500:
            if setor == "varejo":
                porcentagem_garantia = 0.50
            else:
                porcentagem_garantia = 0.30
            valor_minimo_garantia = emprestimo * porcentagem_garantia
            print(f"\nPara o setor {setor}, a garantia mínima exigida é R${valor_minimo_garantia:.2f}")
            garantia_ofertada = float(input("Qual o valor da garantia que você oferece? "))
            if garantia_ofertada >= valor_minimo_garantia:
                if faturamento_mensal > 5000:
                    taxa = 0.2
                else:
                    taxa = 0.5
                valor_com_juros = emprestimo * (1 + taxa)

                print("\n" + "="*30)
                print("EMPRESTIMO APROVADO!")
                print(f"Score do cliente: {score}")
                print(f"Taxa aplicada: {taxa:.0%}")
                print(f"Valor total com juros: R${valor_com_juros:.2f}")
                print(f"Valor de cada parcela (24x): R${math.ceil(valor_com_juros/24):.2f}")
                print("="*30)
            else:
                print("PROPOSTA NEGADA: Valor da garantia insuficiente.")
        else:
            print("PROPOSTA NEGADA: Score muito baixo.")
    else:
        print(f"PROPOSTA NEGADA: Parcela de R${valor_parcela} compromete mais de 30% do faturamento.")
else:
    print("PROPOSTA NEGADA: A empresa não atende aos requisitos de tempo de fundação ou setor.")