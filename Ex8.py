h_ini = 0
m_ini = 0
h_fim = 0
m_fim = 0

def calcular_tempo():
    total_ini = (h_ini * 60) + m_ini
    total_fim = (h_fim * 60) + m_fim
    
    if total_fim >= total_ini:
        duracao_minutos = total_fim - total_ini
    else:
        duracao_minutos = (total_fim + 1440) - total_ini
        
    horas = duracao_minutos // 60
    minutos = duracao_minutos % 60
    
    print(f"O jogo durou {horas} horas e {minutos} minutos")

def main():
    global h_ini, m_ini, h_fim, m_fim
    h_ini = int(input("Digite a hora de inicio: "))
    m_ini = int(input("Digite o minuto de inicio: "))
    h_fim = int(input("Digite a hora de termino: "))
    m_fim = int(input("Digite o minuto de termino: "))
    calcular_tempo()

main()
