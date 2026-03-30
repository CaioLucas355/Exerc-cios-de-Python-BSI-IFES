import random
# =========================================
# EXERCÍCIOS - PARTE 1 (TUPLAS)
# =========================================
import os
# -----------------------------------------
# QUESTÃO 1 - Funcionário mais antigo
# -----------------------------------------
# Dada uma lista de tuplas com (nome, tempo de casa, salário),
# identificar o(s) funcionário(s) com maior tempo de empresa
# e aplicar bônus de 10%.

def bonus(funcs):
    maisV = 0;
    for (_ , tempo , _) in funcs:
        if tempo > maisV:
            maisV = tempo;
    for (nome , time , sal) in funcs:
        if time == maisV:
            print(f'{nome} - R${(sal * 1.1):.0f}');

# -----------------------------------------
# QUESTÃO 2 - Lucro de produtos
# -----------------------------------------
# Recebe lista de tuplas (preço_custo, preço_venda)
# e imprime:
# - quantidade com lucro 25%

def lucro(l):
    menos20 = 0;
    mais25 = 0;
    for (custo, venda) in l:
        if venda == (1.25*custo):
            mais25 += 1;
    print(f"Quantidade com lucro 25%: {(mais25 / len(l))*100}%");

# -----------------------------------------
# QUESTÃO 3 - Pontos alinhados
# -----------------------------------------
# Dadas três tuplas representando pontos (x, y),
# verificar se estão alinhados

def alinhados(a, b, c):
    x1, y1 = a;
    x2, y2 = b;
    x3, y3 = c;

    fator = (x1*(y2 - y3) + x2*(y3 - y1) + x3*(y1 - y2));
    if(fator != 0):
        return False
    return True;

# -----------------------------------------
# QUESTÃO 4 - Agência de turismo
# -----------------------------------------
# Cada voo: (numero, companhia, lista de escalas)
# (a) Voos que começam em A e terminam em B

def q4a (voos,a,b):
    for (id,com,escala) in voos:
        if(escala[0] == a and escala[-1] == b):
            print(f'{id} - {com}');

# (b) Quantos voos começam em A e passam por B

def q4b (voos,a,b):
    qnt_voos = 0;
    for (id, com , escala) in voos:
        for city in escala:
            if(escala[0] == a and b in escala):
                qnt_voos += 1;
    print(f"{qnt_voos}");

# (c) Verificar se existe voo direto entre A e B

def q4c (voos,a,b):
    for( _ , _ , escala) in voos:
        for i in range (len(escala) -1):
            if(escala[i] == a and escala[i+1] == b):
                return True;
    return False;

# -----------------------------------------
# QUESTÃO 5 - Copa do Mundo
# -----------------------------------------
# Determinar quantos jogos terminaram empatados
# com base nos pontos dos times

def bowser(n_jogos,classificacao):
    # 3 * n_jogos é o número máximo de pontos possíveis com todos os casos de vitória, mas a realidade é diferente por conta dos empates
    #cada empate diminui 1 ponto do total pois ele gera apenas 1 ponto para cada time, ou seja 2 ao invés de 3
    #com base nisso, se eu pego o número máximo de possível e subtráio ele pela quantidade total real de pontos posso saber o número de empates
    pontos_totais = 0;
    for ( _ ,pontos) in classificacao:
        pontos_totais += pontos;
    qnt_empate = 3 * n_jogos - pontos_totais;
    return qnt_empate;

# =========================================
# EXERCÍCIOS - PARTE 2 (SISTEMA DE BOLÃO)
# =========================================
def bolao():
    jogadores = [];
    apostas = [];
    print("Bem vindo ao Bolão!");
    ordem = input(menu());
    
    while ordem != "0":
        limparTela();
        if ordem == "1":
            cadastrarJogador(jogadores);
        elif ordem == "2":
            visualizarJogadores(jogadores);
        elif ordem == "3":
            cadastrarAposta(jogadores, apostas);
        elif ordem == "4":
            visualizarApostas(jogadores, apostas);
        elif ordem == "5":
            sorteio(jogadores, apostas);
        else:
            print("Opção inválida. Tente novamente.");
        ordem = input(menu)
    print("Bolão do Pésão desativado - Obrigado por Jogar!");
# -----------------------------------------
# QUESTÃO 1 - Menu principal
# -----------------------------------------
def menu():
    print('''
Bolão do Pésão - Escolha uma opção:

1) Cadastrar usuário
2) Visualizar usuários
3) Cadastrar aposta
4) Visualizar apostas
5) Inserir sorteio e ver vencedores
0) Sair 
Digite o Número!
''')
# -----------------------------------------
# FUNÇÃO AUXILIAR - Limpar tela
# -----------------------------------------
def limparTela():
    if os.name == "nt":
        os.system("cls");
    else:
        os.system("clear");
# -----------------------------------------
# QUESTÃO 2 - Cadastrar jogador
# -----------------------------------------
# Inserir (nome, CPF) se não existir    
def JaExiste(cpf, jogadores):
    for (id,_) in jogadores:
        if (id == cpf):
            return True;
    return False;

def cadastrarJogador(jogadores):
    nome = input("Digite o nome: ");
    cpf = input("Digite o CPF: ");
    
    if(JaExiste(cpf,jogadores)):
        print("Indivíduo já cadastrado! Cadastro não realizado.");
    else:
        jogadores.append(cpf , nome);
# -----------------------------------------
# QUESTÃO 3 - Visualizar jogadores
# -----------------------------------------
def visualizarJogadores(jogadores):
    if (len(jogadores) == 0):
        print("Nenhum jogador foi cadastrado.");
    else:
        i = 1;
        print("#" + "--" + "Lista de Jogadores" + "--" +"#");
        for (cpf, nome) in jogadores:
            print(f'Jogador Nº{i}: {nome} - {cpf}  ');
            i += 1;
# -----------------------------------------
# QUESTÃO 4 - Cadastrar aposta
# -----------------------------------------
def cadastrarAposta(jogadores, apostas):
    apostadores = lerCPFs(jogadores);
    numeroAposta = lerNumerosAposta();
    apostas.append((apostadores , numeroAposta));
# Sub-rotina: ler CPFs dos jogadores
def lerCPFs(jogadores):
    apostadores = [];
    num = int(input("Quantos jogadores estão na Aposta?\n"));
    while num < 1 or n > len(jogadores):
        num = int(input("Número Inaceitável. Por favor tente novamente:\n"));
    while len(apostadores) != num:
        visualizarJogadores(jogadores);
        cpf = input("Por Favor, Digite um CPF:\n");
        if JaExiste(cpf,jogadores) and cpf not in apostadores:
            apostadores.append(cpf);
        else:
            print("CPF Recusado, Tente novamente mais Tarde!");
    return apostadores;
# Sub-rotina: ler números da aposta
def lerNumerosAposta():
    qnt = int(input("Digite quantos números deseja colocar na Aposta:\n"));
    seq = [];
    while (qnt < 6 or qnt > 15):
       qnt = int(input("Número Inaceitável. Por favor tente novamente:\n"));
    while (len(seq) < qnt):
        n = int(input("Digite um número para ser apostado neste cartão:\n"))
        if (n >= 1 and n <= 60 and n not in seq):
            seq.append(n);
        else:
            print("Número Recusado, Tente novamente mais Tarde!");
            
    return seq;
    
# -----------------------------------------
# QUESTÃO 5 - Visualizar apostas
# -----------------------------------------
def visualizarApostas(jogadores, apostas):
    if (len(apostas) == 0):
        print("Nenhuma aposta foi cadastrada, Por Favor, Tente novamente mais tarde!");
    else:
        print("#" + "--" + "Lista de Apostas" + "--" +"#");
        n = 1
        for (id, num) in apostas:
            print(f"Aposta Nº{i}\n");
            print("Números da Aposta: ", end=" ");
            for i in num:
                print(f'[{num}]', end="-");
            print();
            print("Jogadores Participantes:");
            for cpfs in id:
                nome = identificarNome(cpfs,jogadores);
                print(f"{nome} - (CPF: {cpfs})")
            i += 1
            line = "-"*8;
            print(line);
def identificarNome(cpf,jogadores):
    for (id, num) in jogadores:
        if id == cpf: 
            return num;
    return None;
        
# -----------------------------------------
# QUESTÃO 6/7 - Resultado e vencedores
# -----------------------------------------
# Listar vencedores e prêmios
def sorteio(jogadores, apostas): 
    n_sorteados = numerosSorteados();
    valor_total_premio = float(input("Digite o valor total do prêmio do bolão:\n"));
    vencedores = contWinners(apostas,n_sorteados);
    premio_bilhete = valor_total_premio / len(vencedores);
    n = 1;
    print("#" + "--" + "Lista de Vencedores" + "--" +"#");
    for aposta in vencedores:
        premio_individual = premio_bilhete / len(aposta);
        print(f'Aposta Nº{n}:\n');
        for cpf in aposta:
            nome = JaExiste(cpf, jogadores);
            print(f"{nome} - (CPF: {cpf}) - Ganhou: R${premio_individual:.2f}")
        n += 1;  
# Ler números sorteados
def numerosSorteados():
    seq = [];
    while (len(seq) < 6):
        n = int(input("Digite o número sorteado:"));
        if( n >= 1 and n <= 60 and n not in seq):
            seq.append(n);
        else:
            print("Número Inaceitável, Tente Novamente.");
    
    return seq
# Verificar se lista está contida em outra
def verificationList(l1,l2):
    for ele in l1:
        if ele not in l2:
            return False;
    return True;
# Contar apostas vencedoras
def contWinners(apostas, n_sorteados):
    vencedores = [];
    for (ids,numeros) in apostas:
        if (verificationList(n_sorteados, numeros)):
            vencedores.append(ids);
    return vencedores
# -----------------------------------------
# QUESTÃO 8 - Jogo Genius
# -----------------------------------------
# Simular sequência de números aleatórios
# e o usuário deve repetir corretamente
