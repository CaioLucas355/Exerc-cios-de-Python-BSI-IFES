

#Tabuleiro (variáveis)
A1, A2, A3 = ' ', ' ', ' '
B1, B2, B3 = ' ', ' ', ' '
C1, C2, C3 = ' ', ' ', ' '

#Jogador atual (X começa)
jogador = 'X'

#Função para mostrar o tabuleiro
def mostrar_tabuleiro():
    print(f"{A1}|{A2}|{A3}")
    print("-+-+-")
    print(f"{B1}|{B2}|{B3}")
    print("-+-+-")
    print(f"{C1}|{C2}|{C3}")

#Função para verificar se há um vencedor
def verificar_vitoria():
    # Linhas
    if A1 == A2 == A3 and A1 != ' ': return True
    if B1 == B2 == B3 and B1 != ' ': return True
    if C1 == C2 == C3 and C1 != ' ': return True
    # Colunas
    if A1 == B1 == C1 and A1 != ' ': return True
    if A2 == B2 == C2 and A2 != ' ': return True
    if A3 == B3 == C3 and A3 != ' ': return True
    # Diagonais
    if A1 == B2 == C3 and A1 != ' ': return True
    if A3 == B2 == C1 and A3 != ' ': return True
    return False

#Função para verificar empate
def verificar_empate():
    if A1 != ' ' and A2 != ' ' and A3 != ' ' and \
       B1 != ' ' and B2 != ' ' and B3 != ' ' and \
       C1 != ' ' and C2 != ' ' and C3 != ' ':
        return True
    return False
def main():
#Começo da bomba
    while True:
        mostrar_tabuleiro()

        # Solicitar a jogada
        print(f"Jogador {jogador}, faça sua jogada (digite a linha e a coluna):")
        jogada = input().upper()

        if jogada == 'A1' and A1 == ' ':
            A1 = jogador
        elif jogada == 'A2' and A2 == ' ':
            A2 = jogador
        elif jogada == 'A3' and A3 == ' ':
            A3 = jogador
        elif jogada == 'B1' and B1 == ' ':
            B1 = jogador
        elif jogada == 'B2' and B2 == ' ':
            B2 = jogador
        elif jogada == 'B3' and B3 == ' ':
            B3 = jogador
        elif jogada == 'C1' and C1 == ' ':
            C1 = jogador
        elif jogada == 'C2' and C2 == ' ':
            C2 = jogador
        elif jogada == 'C3' and C3 == ' ':
            C3 = jogador
        else:
            print("Jogada inválida ou posição já ocupada. Tente novamente.")
            continue

        #Verificar vitória ou empate
        if verificar_vitoria():
            mostrar_tabuleiro()
            print(f"Parabéns, jogador {jogador}! Você ganhou!")
            break
        elif verificar_empate():
            mostrar_tabuleiro()
            print("Empate!")
            break

        #Alternar o jogador
        jogador = 'O' if jogador == 'X' else 'X'
if __name__ == "__main__":
    main()


#Viver é muito perigoso, Caio. Lembre-se disso; 