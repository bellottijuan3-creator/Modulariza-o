n1 = 0
n2 = 0
n3 = 0
n4 = 0
def calcular_nota():
    media = (n1 + n2 + n3 + n4)/4
    print(f"Sua nota foi de {media}")
    if media >= 6.0:
        print("APROVADO")
    elif media >= 3 and media < 6:
        print("EXAME")
    elif media < 3:
        print("RETIDO")

def main():
    global n1, n2, n3, n4
    n1 = float(input("Digite sua primeira nota: "))
    n2 = float(input("Digite sua segunda nota: "))
    n3 = float(input("Digite sua terceira nota: "))
    n4 = float(input("Digite sua quarta nota: "))
    calcular_nota()


main()