# =========================================
# Q3 - Bolão
# =========================================
def limparTela():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

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
import pickle
import os

def bolao():
    open("bolao.py", "w").close()
    if(os.path.exists("jogadores")):
        with open(jogadores, "wb") as f:
            jogadores = pickle.load(f)
        if(os.path.exists("apostas")):
            with open(apostas, "wb") as f1:
                apostas = pickle.load(f1)
    else:
        jogadores = {}  # <- dicionário agora
        apostas = []
    print("Bem vindo ao Bolão!")

    opcoes = {
        "1": lambda: cadastrarJogador(jogadores),
        "2": lambda: visualizarJogadores(jogadores),
        "3": lambda: cadastrarAposta(jogadores, apostas),
        "4": lambda: visualizarApostas(jogadores, apostas),
        "5": lambda: sorteio(jogadores, apostas),
    }
    ordem = input(menu())
    while ordem != "0":
        limparTela()
        if ordem in opcoes:
            opcoes[ordem]()
        else:
            print("Opção inválida. Tente novamente.")
        ordem = input(menu())
    print("Bolão do Pésão desativado - Obrigado por Jogar!")

# - Cadastrar jogador
def salvarJogadores(jogadores):
    with open("jogadores", "wb") as f:
        pickle.dump(jogadores, f);

def JaExiste(cpf, jogadores):
    return cpf in jogadores  # <- busca direta no dicionário

def cadastrarJogador(jogadores):
    nome = input("Digite o nome: ")
    cpf = input("Digite o CPF: ")
    if JaExiste(cpf, jogadores):
        print("Indivíduo já cadastrado! Cadastro não realizado.")
    else:
        jogadores[cpf] = nome  # <- chave: CPF, valor: nome
    salvarJogadores(jogadores);

# - Visualizar jogadores

def visualizarJogadores(jogadores):
    if not jogadores:
        print("Nenhum jogador foi cadastrado.")
    else:
        print("#--Lista de Jogadores--#")
        for i, (cpf, nome) in enumerate(jogadores.items(), start=1):  # <- .items() do dicionário
            print(f"Jogador Nº{i}: {nome} - {cpf}")


#  - Cadastrar aposta
def salvarAposta(apostas):
    with open("apostas", "wb") as f:
        pickle.dump(apostas, f);

def cadastrarAposta(jogadores, apostas):
    apostadores = lerCPFs(jogadores)
    numeroAposta = lerNumerosAposta()
    apostas.append((apostadores, numeroAposta))
    salvarAposta(apostas);

# Sub-rotina: ler CPFs dos jogadores
def lerCPFs(jogadores):
    apostadores = []
    num = int(input("Quantos jogadores estão na Aposta?\n"))
    while num < 1 or num > len(jogadores):
        num = int(input("Número Inaceitável. Por favor tente novamente:\n"))
    while len(apostadores) != num:
        visualizarJogadores(jogadores)
        cpf = input("Por Favor, Digite um CPF:\n")
        if JaExiste(cpf, jogadores) and cpf not in apostadores:
            apostadores.append(cpf)
        else:
            print("CPF Recusado, Tente novamente mais Tarde!")
    return apostadores

# Sub-rotina: ler números da aposta
def lerNumerosAposta():
    qnt = int(input("Digite quantos números deseja colocar na Aposta:\n"))
    seq = []
    while qnt < 6 or qnt > 15:
        qnt = int(input("Número Inaceitável. Por favor tente novamente:\n"))
    while len(seq) < qnt:
        n = int(input("Digite um número para ser apostado neste cartão:\n"))
        if n >= 1 and n <= 60 and n not in seq:
            seq.append(n)
        else:
            print("Número Recusado, Tente novamente mais Tarde!")
    return seq

#  - Visualizar apostas

def visualizarApostas(jogadores, apostas):
    if len(apostas) == 0:
        print("Nenhuma aposta foi cadastrada, Por Favor, Tente novamente mais tarde!")
    else:
        print("#--Lista de Apostas--#")
        n = 1
        for (id, num) in apostas:
            print(f"Aposta Nº{n}\n")
            print("Números da Aposta: ", end=" ")
            for i in num:
                print(f'[{i}]', end="-")
            print()
            print("Jogadores Participantes:")
            for cpfs in id:
                nome = identificarNome(cpfs, jogadores)
                print(f"{nome} - (CPF: {cpfs})")
            n += 1
            line = "-" * 8
            print(line)

def identificarNome(cpf, jogadores):
    return jogadores.get(cpf)  # <- .get() do dicionário, já retorna None se não existir

# - Resultado e vencedores

def sorteio(jogadores, apostas):
    n_sorteados = numerosSorteados()
    valor_total_premio = float(input("Digite o valor total do prêmio do bolão:\n"))
    vencedores = contWinners(apostas, n_sorteados)
    premio_bilhete = valor_total_premio / len(vencedores)
    n = 1
    print("#--Lista de Vencedores--#")
    for aposta in vencedores:
        premio_individual = premio_bilhete / len(aposta)
        print(f'Aposta Nº{n}:\n')
        for cpf in aposta:
            nome = jogadores.get(cpf)  # <- busca direta no dicionário, sem chamar JaExiste
            print(f"{nome} - (CPF: {cpf}) - Ganhou: R${premio_individual:.2f}")
        n += 1

# Ler números sorteados
def numerosSorteados():
    seq = []
    while len(seq) < 6:
        n = int(input("Digite o número sorteado:"))
        if n >= 1 and n <= 60 and n not in seq:
            seq.append(n)
        else:
            print("Número Inaceitável, Tente Novamente.")
    return seq

# Verificar se lista está contida em outra
def verificationList(l1, l2):
    for ele in l1:
        if ele not in l2:
            return False
    return True

# Contar apostas vencedoras
def contWinners(apostas, n_sorteados):
    vencedores = []
    for (ids, numeros) in apostas:
        if verificationList(n_sorteados, numeros):
            vencedores.append(ids)
    return vencedores