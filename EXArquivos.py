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
            arq = open("recorde_genius.txt", "w")
            arq.write(str(pontos))
            arq.close()
        elif(recorde == pontos):
            print(f"Você atingiu o recorde de pontos ({recorde}) mas não ultrapassou - seus pontos: ({pontos})");
        else:
            print(f"Infelizmente não conseguiu superar o recorde do jogo de {recorde} pontos com seus míseraveis {pontos} pontos")
        rec.close()
    else:
        rec = open("recorde_genius.txt", "w");
        print("Você acaba de criar um novo recorde de pontos com seus pontos: ({pontos})")
        rec.write(str(pontos));
    rec.close()
    
# =========================================
# Q2 - Agenda
# =========================================
def existe(arq_name):
    return os.path.exists(arq_name);

def menu():
    welcome = """
Bem Vindo a sua Agenda Pessoal!
\tO que deseja fazer?
\t\t1) Cadastrar um novo contato
\t\t2) Visualizar todos os contatos
\t\t0) Fechar agenda
Digite o Número da escolha abaixo""";
    print(welcome);


def cadastrarNovoContato():
    contatus = "contatos.txt";
    nome = input("Digite o NOME do Contato\n>:")
    tel = input("Digite o TELEFONE do Contato\n>:")
    if(existe(contatus)):
        arq = open(contatus, "a");
        arq.append(nome + "-" + tel);
        arq.close()
        print("Cadastro Realizado!");
    else:
        arq = open(contatus, "w");
        arq.write(nome + "-" + tel);
        arq.close();
        print("Cadastro Realizado!")
    agenda()

def visualizarContatos():
    print("Lista de Contatos:")
    contatus = "contatos.txt";
    if(existe(contatus)):
        with open(contatus, "r") as contato:
            for contatos in contato.read().splitlines():
                nome , tel = contatos.split("-") ;
                print(f"\tNome: {nome} -\tTel: {tel}");
    else:
        print("Nenhum Contato ainda Cadastrado!")
    agenda()

def agenda():
    ordem = { 1: cadastrarNovoContato(), 2: visualizarContatos()}
    on = True;
    while on:
        menu()
        ord = int(input());
        if ord == 0:
            on = False;
        if ord in ordem:
            ordem[ord]();
        else:
            print("Opção Inválida, tente novamente!\n>:")


# =========================================
# Q3 - Bolão
# =========================================
    #Feita Separadamente
