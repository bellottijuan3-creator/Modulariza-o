v1 = 0
v2 = 0
v3 = 0
v4 = 0

def Mostrar_Ordem():
    if v4 > v3:
        print(f"{v1}, {v2}, {v3}, {v4}")
    elif v4 > v2:
        print(f"{v1}, {v2}, {v4}, {v3}")
    elif v4 > v1:
        print(f"{v1}, {v4}, {v2}, {v3}")
    else:
        print(f"{v4}, {v1}, {v2}, {v3}")

def main():
    global v1, v2, v3, v4
    v1 = float(input("Digite o primeiro valor: "))
    v2 = float(input("Digite o segundo valor: "))
    v3 = float(input("Digite o terceiro valor: "))
    v4 = float(input("Digite o quarto valor: "))
    Mostrar_Ordem()

main()