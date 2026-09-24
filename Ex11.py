def calcular_novo_preco(preco, venda):
    if venda < 500 and preco < 30:
        novo_preco = preco * 1.10
    elif (venda >= 500 and venda < 1000) and (preco >= 30 and preco < 80):
        novo_preco = preco * 1.15
    elif venda >= 1000 and preco >= 80:
        novo_preco = preco * 0.95
    else:
        novo_preco = preco
        
    print(f"Novo preco: {novo_preco}")

def main():
    preco_atual = float(input("Digite o preco atual: "))
    venda_mensal = float(input("Digite a venda mensal: "))
    calcular_novo_preco(preco_atual, venda_mensal)

main()
