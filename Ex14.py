def fatorial(num):
    fator = 1

    for i in range(1, num + 1, 1):
        fator = fator * i

    return fator


def dividir(num1, num2):
    return num1 / num2


def main():
    numero = int(input("Digite o valor de N: "))

    resultado = 0

    for i in range(0, numero + 1, 1):
        resultado = resultado + dividir(1, fatorial(i))

    print(f"Resultado: {resultado}")


main()