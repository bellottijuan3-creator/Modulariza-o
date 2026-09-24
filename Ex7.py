v1 = 0

def calculo_se_e_divisivel():
    if v1 % 2 == 0:
        print(f"O numero {v1} é divisível por 2")
    elif v1 % 3 == 0:
        print(f"O numero {v1} é divisível por 3")
    else:
        print("Este numero não é divisivel nem por 2 e nem por 3")

def main():
    global v1
    v1 = int(input("digite um valor: "))
    calculo_se_e_divisivel()

main()