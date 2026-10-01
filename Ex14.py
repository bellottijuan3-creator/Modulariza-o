
# inicio
Contar = 1
while (Contar <= 4):
    
    if Contar == 1:
        print("--Cadastro do time A--")
        VitoriasA = int(input("Digite o quantas vitorias o time teve: ").strip())
        EmpatesA = int(input("Digite quantos empates o time teve: ").strip())  
        DerrotasA = int(input("Digite quantas derrotas o time teve: ").strip())
        GolsmA = int(input("Digite quantos gols o Time marcou: ").strip()) 
        GolsSA = int(input("Digite quantos gols o time sofreu: ")) 
        saldoDeA = GolsmA - GolsSA
        somaTotalA = VitoriasA + EmpatesA + DerrotasA
        somaPontosA = (VitoriasA * 3) + (EmpatesA * 1)
        
        if somaTotalA != 12:
            print("Soma total ultrapassou ou não chegou a 12")
            
        elif GolsmA < 13 or GolsmA > 20:
            print("Gols marcados fora do critéiro! ")
            
        elif GolsSA < 9 or GolsSA > 11:
            print("Gols sofridos fora do critério! ")
        else:
            print("Tudo dentro do critério")
            Contar = Contar + 1
            percentVA = (somaPontosA/36)*100
            print(f"O porcentual de vitoria é {percentVA:.2f}")
            

        
            
    if Contar == 2:
        
        print("--Cadastro do time B--")
        VitoriasB = int(input("Digite o quantas vitorias o time teve: ").strip())
        EmpatesB = int(input("Digite quantos empates o time teve: ").strip())  
        DerrotasB = int(input("Digite quantas derrotas o time teve: ").strip())
        GolsmB = int(input("Digite quantos gols o Time marcou: ").strip()) 
        GolsSB = int(input("Digite quantos gols o time sofreu: ")) 
        saldoDeB = GolsmB - GolsSB 
        somaTotalB = VitoriasB + EmpatesB + DerrotasB
        somaPontosB = (VitoriasB * 3) + (EmpatesB * 1)
        
        if somaTotalB != 12:
            print("Soma total ultrapassou ou não chegou a 12")
            Contar = 1
        elif GolsmB < 13 or GolsmB > 20:
            print("Gols marcados fora do critéiro! ")
            Contar = 1
        elif GolsSB < 9 or GolsSB > 11:
            print("Gols sofridos fora do critério! ")
            Contar = 1
        else:
            print("Tudo dentro do critério")
            Contar = Contar + 1
            percentVB = (somaPontosB/36)*100
            print(f"O porcentual de vitoria é {percentVB:.2f}")
        
    if Contar == 3:
        
        print("--Cadastro do time C--")
        VitoriasC = int(input("Digite o quantas vitorias o time teve: ").strip())
        EmpatesC = int(input("Digite quantos empates o time teve: ").strip())  
        DerrotasC = int(input("Digite quantas derrotas o time teve: ").strip())
        GolsmC = int(input("Digite quantos gols o Time marcou: ").strip()) 
        GolsSC = int(input("Digite quantos gols o time sofreu: "))
        saldoDeC = GolsmC - GolsSC 
        somaTotalC = VitoriasC + EmpatesC + DerrotasC
        somaPontosC = (VitoriasC * 3) + (EmpatesC * 1)
        
        if somaTotalC != 12:
            print("Soma total ultrapassou ou não chegou a 12")
            Contar = 1
            
        elif GolsmC < 13 or GolsmC > 20:
            print("Gols marcados fora do critéiro! ")
            Contar = 1
        
        elif GolsSC < 9 or GolsSC > 11:
            print("Gols sofridos fora do critério! ")
            Contar = 1
            
        else:
            print("Tudo dentro do critério")
            Contar = Contar + 1
            percentVC = (somaPontosC/36)*100
            print(f"O porcentual de vitoria é {percentVC:.2f}")
        
    if Contar == 4:
        
        print("--Cadastro do time D--")
        VitoriasD = int(input("Digite o quantas vitorias o time teve: ").strip())
        EmpatesD = int(input("Digite quantos empates o time teve: ").strip())  
        DerrotasD = int(input("Digite quantas derrotas o time teve: ").strip())
        GolsmD = int(input("Digite quantos gols o Time marcou: ").strip()) 
        GolsSD = int(input("Digite quantos gols o time sofreu: ")) 
        saldoDeD = GolsmD - GolsSD
        somaTotalD = VitoriasD + EmpatesD + DerrotasD
        somaPontosD = (VitoriasD * 3) + (EmpatesD * 1)
        
        
        if somaTotalD != 12:
            print("Soma total ultrapassou ou não chegou a 12")
            
        elif GolsmD < 13 or GolsmD > 20:
            print("Gols marcados fora do critéiro! ")
        
        elif GolsSD < 9 or GolsSD > 11:
            print("Gols sofridos fora do critério! ")
            
        else:
            print("Tudo dentro do critério")
            Contar = Contar + 1
            percentVD = (somaPontosD/36)*100
            print(f"O porcentual de vitoria é {percentVD:.2f}")
  
if percentVA > percentVB and percentVA > percentVC and percentVA > percentVD:
    print("TIME A CAMPEÃO!")

elif percentVA == percentVB:
    if saldoDeA > saldoDeB:
        print("TIME A CAMPEÃO PELO SALDO DE GOLS!")
    else:
        print("TIME B CAMPEÃO PELO SALDO DE GOLS!")

elif percentVA == percentVC:
    if saldoDeA > saldoDeC:
        print("TIME A CAMPEÃO PELO SALDO DE GOLS!")
    else:
        print("TIME C CAMPEÃO PELO SALDO DE GOLS!")

elif percentVA == percentVD:
    if saldoDeA > saldoDeD:
        print("TIME A CAMPEÃO PELO SALDO DE GOLS!")
    else:
        print("TIME D CAMPEÃO PELO SALDO DE GOLS!")


# -------- TIME B --------

elif percentVB > percentVA and percentVB > percentVC and percentVB > percentVD:
    print("TIME B CAMPEÃO!")

elif percentVB == percentVA:
    if saldoDeB > saldoDeA:
        print("TIME B CAMPEÃO PELO SALDO DE GOLS!")
    else:
        print("TIME A CAMPEÃO PELO SALDO DE GOLS!")

elif percentVB == percentVC:
    if saldoDeB > saldoDeC:
        print("TIME B CAMPEÃO PELO SALDO DE GOLS!")
    else:
        print("TIME C CAMPEÃO PELO SALDO DE GOLS!")

elif percentVB == percentVD:
    if saldoDeB > saldoDeD:
        print("TIME B CAMPEÃO PELO SALDO DE GOLS!")
    else:
        print("TIME D CAMPEÃO PELO SALDO DE GOLS!")


# -------- TIME C --------

elif percentVC > percentVA and percentVC > percentVB and percentVC > percentVD:
    print("TIME C CAMPEÃO!")

elif percentVC == percentVA:
    if saldoDeC > saldoDeA:
        print("TIME C CAMPEÃO PELO SALDO DE GOLS!")
    else:
        print("TIME A CAMPEÃO PELO SALDO DE GOLS!")

elif percentVC == percentVB:
    if saldoDeC > saldoDeB:
        print("TIME C CAMPEÃO PELO SALDO DE GOLS!")
    else:
        print("TIME B CAMPEÃO PELO SALDO DE GOLS!")

elif percentVC == percentVD:
    if saldoDeC > saldoDeD:
        print("TIME C CAMPEÃO PELO SALDO DE GOLS!")
    else:
        print("TIME D CAMPEÃO PELO SALDO DE GOLS!")


# -------- TIME D --------

elif percentVD > percentVA and percentVD > percentVB and percentVD > percentVC:
    print("TIME D CAMPEÃO!")

elif percentVD == percentVA:
    if saldoDeD > saldoDeA:
        print("TIME D CAMPEÃO PELO SALDO DE GOLS!")
    else:
        print("TIME A CAMPEÃO PELO SALDO DE GOLS!")

elif percentVD == percentVB:
    if saldoDeD > saldoDeB:
        print("TIME D CAMPEÃO PELO SALDO DE GOLS!")
    else:
        print("TIME B CAMPEÃO PELO SALDO DE GOLS!")

elif percentVD == percentVC:
    if saldoDeD > saldoDeC:
        print("TIME D CAMPEÃO PELO SALDO DE GOLS!")
    else:
        print("TIME C CAMPEÃO PELO SALDO DE GOLS!")
    

    
