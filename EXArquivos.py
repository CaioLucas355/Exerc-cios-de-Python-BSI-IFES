# -----------------------------------------
# FUNÇÃO AUXILIAR - Limpar tela
# -----------------------------------------
import os
def limparTela():
    if os.name == "nt":
        os.system("cls");
    else:
        os.system("clear");
# =========================================
# Q1 - Genius
# =========================================
import random

def q1():
    #arq = open("recorde.txt","w")
    pontos = 0;
    print("Bem Vindo ao Jogo do Genius!");
    n_sorteado = str(random.randint(1,4));
    seq_sort = n_sorteado;
    print(f"O Primeiro Número é: {n_sorteado}");
    
    g = input();
    while g == n_sorteado:
        pontos += 1;
        limparTela();
        seq_sort = seq_sort + n_sorteado;
        n_sorteado = str(random.randint(1,4));
        print(f"O Próximo Número é: {n_sorteado}\n");
        g = input();
    #------------------------------------------------------------------------
    existe =  os.path.exists("recorde_genius.txt");
    print(f"Você errou, tente novamente mais tarde!");
    if(existe):
        rec = open("recorde_genius.txt", "r");
        recorde = int(rec.read());
        if(recorde < pontos):
            print(f'Você superou o antigo recorde ({recorde}) agora você é o number 1 do jogo com seus incríveis {pontos} pontos')
            with open("recorde_genius.txt", "w") as arq:
                arq.write(str(pontos))
        elif(recorde == pontos):
            print(f"Você atingiu o recorde de pontos ({recorde}) mas não ultrapassou - seus pontos: ({pontos})");
        else:
            print(f"Infelizmente não conseguiu superar o recorde do jogo de {recorde} pontos com seus míseraveis {pontos} pontos")
    else:
        rec = open("recorde_genius.txt", "w");
        print("Você acaba de criar um novo recorde de pontos com seus pontos: ({pontos})")
        rec.write(str(pontos));
# =========================================
# Q2 - Agenda
# =========================================
#def q2():
    
# =========================================
# Q3 - Bolão
# =========================================
#def q3():