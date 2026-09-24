num1 = 0
num = 0

def MaiorMenor():
    if num1 > num2:
        print(f"{num1} é maior que {num2}")
    else:
        print(f"{num2} é maior que {num1}")
    
    
def main():
    global num1, num2
    num1 = int(input("Digite o primeiro numero: "))
    num2 = int(input("Digite o segundo numero: "))
    MaiorMenor()



main()