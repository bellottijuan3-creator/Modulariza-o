def calcular_velocidade(v, e, t):
    distancia_total_metros = v * e
    distancia_km = distancia_total_metros / 1000
    tempo_horas = t / 60
    
    velocidade_media = distancia_km / tempo_horas
    print(f"Velocidade media: {velocidade_media} km/h")

def main():
    voltas = int(input("Digite o numero de voltas: "))
    extensao = float(input("Digite a extensao do circuito em metros: "))
    tempo = float(input("Digite o tempo de duracao em minutos: "))
    
    # Passando as variaveis locais como parametros para o procedimento
    calcular_velocidade(voltas, extensao, tempo)

main()
