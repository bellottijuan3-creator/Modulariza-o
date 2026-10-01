def fatorial(num):
    fator = 1
    for i in range(1, num+1, 1):
        fator = fator * i  

    return fator

def main():
    numero = int(input("Digite um numero: "))
    print(f"o fatorial de {numero} é {fatorial(numero)}")
main()
                                 