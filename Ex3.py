import math

a = 0
b = 0
c = 0

def calcular_raizes():
    delta = (b ** 2) - (4 * a * c)
    print(f"Delta = {delta}")
    
    if delta < 0:
        print("Nao existem raizes reais")
    elif delta == 0:
        x = -b / (2 * a)
        print(f"Existe uma raiz: {x}")
    else:
        x1 = (-b + math.sqrt(delta)) / (2 * a)
        x2 = (-b - math.sqrt(delta)) / (2 * a)
        print(f"X1 = {x1}")
        print(f"X2 = {x2}")

def main():
    global a, b, c
    a = float(input("Digite o coeficiente A: "))
    b = float(input("Digite o coeficiente B: "))
    c = float(input("Digite o coeficiente C: "))
    calcular_raizes()

main()