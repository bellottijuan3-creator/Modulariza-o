num1 = 0
num2 = 0

def verificar_multiplo():
    if num1 > num2:
        maior = num1
        menor = num2
    else:
        maior = num2
        menor = num1

    if menor == 0:
        print("Nao e possivel dividir por zero")
    elif maior % menor == 0:
        print(f"{maior} e multiplo de {menor}")
    else:
        print(f"{maior} nao e multiplo de {menor}")

def main():
    global num1, num2
    num1 = int(input("Digite o primeiro numero: "))
    num2 = int(input("Digite o segundo numero: "))
    verificar_multiplo()

main()
