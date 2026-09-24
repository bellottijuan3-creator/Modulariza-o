v1 = 0
v2 = 0
def Mostrar_Crescente():
    if v1 > v2:
        print(f"{v2}, {v1}")
    else:
        print(f"{v1}, {v2}")

def main():
    global v1, v2
    v1 = int(input("Digite o primeiro valor: "))
    v2= int(input("Digite o segundo valor: "))
    Mostrar_Crescente()

main()