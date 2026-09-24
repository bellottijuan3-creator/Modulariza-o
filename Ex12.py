def calcular_rendimento(tipo, valor):
    if tipo == 1:
        valor_corrigido = valor * 1.03
        print(f"Valor corrigido na poupanca: {valor_corrigido}")
    elif tipo == 2:
        valor_corrigido = valor * 1.05
        print(f"Valor corrigido na renda fixa: {valor_corrigido}")
    else:
        print("Tipo de investimento invalido")

def main():
    tipo = int(input("Digite o tipo (1=poupanca, 2=renda fixa): "))
    valor = float(input("Digite o valor do investimento: "))
    calcular_rendimento(tipo, valor)

main()
