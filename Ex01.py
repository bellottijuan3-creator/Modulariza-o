num1 = 0
num = 0
def MaiorMenor():
    if num1 > num2:
        d = num1 - num2
        print(f"{num1} é maior que {num2} a diferença entre eles é {d}")
    else:
        d = num2 - num1
        print(f"{num2} é maior que {num1} a diferença entre eles é {d}")
    
     
def main():
    global num1, num2
    num1 = int(input("Digite o primeiro numero: "))
    num2 = int(input("Digite o segundo numero: "))
    MaiorMenor()

main()