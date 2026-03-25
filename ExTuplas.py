# =========================================
# EXERCÍCIOS - PARTE 1 (TUPLAS)
# =========================================

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

# -----------------------------------------
# QUESTÃO 1 - Menu principal
# -----------------------------------------

# -----------------------------------------
# FUNÇÃO AUXILIAR - Limpar tela
# -----------------------------------------

# -----------------------------------------
# QUESTÃO 2 - Cadastrar jogador
# -----------------------------------------
# Inserir (nome, CPF) se não existir

# -----------------------------------------
# QUESTÃO 3 - Visualizar jogadores
# -----------------------------------------

# -----------------------------------------
# QUESTÃO 4 - Cadastrar aposta
# -----------------------------------------

# Sub-rotina: ler CPFs dos jogadores

# Sub-rotina: ler números da aposta

# -----------------------------------------
# QUESTÃO 5 - Visualizar apostas
# -----------------------------------------

# -----------------------------------------
# QUESTÃO 6/7 - Resultado e vencedores
# -----------------------------------------

# Ler números sorteados

# Verificar se lista está contida em outra

# Contar apostas vencedoras

# Listar vencedores e prêmios

# -----------------------------------------
# QUESTÃO 8 - Jogo Genius
# -----------------------------------------
# Simular sequência de números aleatórios
# e o usuário deve repetir corretamente