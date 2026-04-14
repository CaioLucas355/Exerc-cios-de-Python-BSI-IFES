# =========================================
# Q1 - Adultos
# =========================================
"""
Crie um dicionário com nome, idade e telefone de 10 pessoas (digitado pelo usuário).
Depois:
01 = {[nome, idade, num]}
- Remova menores de idade
- Imprima nome e telefone dos restantes
"""

def remover_menores(listaTele):
    remover = [];
    for key in listaTele:
        nome, idade, num = listaTele[key];
        if idade < 18:
            remover.append(key);
    
    for key in remover:
        del listaTele[key];
        
def imprimirListaTele(listaTelefonica):
        i = 1;
        for pessoa in listaTelefonica:
            nome, idade, num = listaTelefonica[pessoa];
            print(f'Indivíduo Nº{i}\nNome: {nome}\tTelefone: {num}');
            i += 1;
            
def q1():
    listaTelefonica = {};
    
    for i in range(10):
        nome = input("Digite um Nome: ");
        idade = int(input("Digite a idade do indivíduo: "));
        num = input("Digite o número do indivíduo: ");
        pessoa = (nome , idade , num);
        key = i + 1;
        listaTelefonica[key] = pessoa;
    
    remover_menores(listaTelefonica);
    imprimirListaTele(listaTelefonica);
         
        
        
# =========================================
# Q2 - Agenda
"""
Sistema de agenda com menu:
1 - Cadastrar contato (nome + telefone)
2 - Visualizar contatos

Regras:
- Armazenar em dicionário
- Salvar em arquivo texto
"""
# =========================================
def q2():
    agenda();

def agenda():
    ordem = { 1: cadastrarNovoContato(contatos), 2: visualizarContatos(contatos)}
    on = True;
    contatos = {}
    
    while on:
        menu()
        ord = int(input());
        if ord == 0:
            on = False;
        if ord in ordem:
            ordem[ord]();
        else:
            print("Opção Inválida, tente novamente!\n>:")
                  
def cadastrarNovoContato(contatos):
    nome = input("Digite o NOME do Contato\n>:")
    tel = input("Digite o TELEFONE do Contato\n>:")
    contatos[nome] = tel;
    print("Cadastro Realizado!")

def visualizarContatos(contatos):
    if not contatos:
        print("Nenhum contato cadastrado.")
        return
    print("\nLista de Contatos:")
    for nome in contatos:
        print(f"Nome: {nome} - Número: {contatos[nome]}");
    
def menu():
    welcome = """
Bem Vindo a sua Agenda Pessoal!
\tO que deseja fazer?
\t\t1) Cadastrar um novo contato
\t\t2) Visualizar todos os contatos
\t\t0) Fechar agenda
Digite o Número da escolha abaixo
          """;
    print(welcome);
        


# =========================================
# Q3 - Bolão
# =========================================
import os
"""
Adaptar sistema do bolão:
- Usar dicionário ao invés de lista
- Salvar dados em arquivo binário
- Carregar dados ao iniciar
"""
def limparTela():
    if os.name == "nt":
        os.system("cls");
    else:
        os.system("clear");
# -------------------------------

def q3():
    pass


# =========================================
# Q4 - Concurso Público
# =========================================
"""
Funções:
(a) Listar candidatos classificados (nota >= 60)
(b) Mostrar aprovado por área:
    - Maior nota total
    - Desempate: mais velho
"""

def q4_a(candidatos, areas, codigo_area):
    seq = [];
    inscritos = areas[codigo_area][1];
    for numInsc in inscritos:
        nota1 = candidatos[numInsc][2];
        if nota1 >= 60:
            seq.append(numInsc);
    return seq;

def q4_b(candidatos, areas):
    print("Lista de Candidatos Aprovados de Cada Área:\n");
    for codArea in areas:
        candi = q1(candidatos,areas,codArea);
        nMaior = 0;
        aprov ="";
        Flag = True;
        for nInsc in candi:
            nome, data, p1, p2 = candidatos[nInsc];
            nFinal = p1 + p2;
            if(Flag):
                Adata = data;
                nMaior = nFinal;
                aprov = nome;
                Flag = False
            elif(nMaior < nFinal):
                Adata = data;
                nMaior = nFinal;
                aprov = nome;
            elif(nMaior == nFinal):
                dia0 , mes0, ano0 = Adata;
                dia1, mes1, ano1 = data;
                if(ano0 > ano1):
                    Adata = data;
                    nMaior = nFinal;
                    aprov = nome;
                elif(mes0 > mes1):
                    Adata = data;
                    nMaior = nFinal;
                    aprov = nome;
                elif(dia0 > dia1):
                    Adata = data;
                    nMaior = nFinal;
                    aprov = nome;
        print(f'\tÁrea - {codArea[0]}\tCandidato Aprovado:\t{aprov}');

# =========================================
# Q5 - Multas (Sistema de trânsito)
# =========================================
"""
(a) Filtrar infrações com menos de 1 ano
(b) Calcular pontos da CNH
(c) Verificar situação do motorista/veículo
"""

def q5_a(infracoes, data_atual):
    pass

def q5_b(cnh, infracoes, naturezas):
    pass

def q5_c(cnh, placa, data_atual, infracoes, motoristas, veiculos):
    pass


# =========================================
# Q6 - Academia
# =========================================
"""
Funções:

- Mostrar treino por grupo
- Mostrar exercícios que aluno NÃO faz
- Autenticação de usuário + exibir treino
"""

def q6_treino(exercicios, alunos, treinos, login, grupo):
    pass

def q6_exercicios_faltantes(exercicios, treinos, login):
    pass

def q6_login(alunos, exercicios, treinos):
    pass


# =========================================
# Q7 - Produtos (Loja)
# =========================================
"""
Funções:

(a) Verificar estoque suficiente
(b) Imprimir pedido
(c) Retornar valor total do pedido
(d) Total gasto por cliente
"""

def q7_a(cod_produto, clientes, produtos, pedidos):
    pass

def q7_b(cod_pedido, clientes, produtos, pedidos):
    pass

def q7_c(cod_pedido, produtos, pedidos):
    pass

def q7_d(clientes, produtos, pedidos):
    pass


# =========================================
# Q8 - Voos
# =========================================
"""
Funções:

(a) Calcular tempo total do voo
(b) Mostrar origem e destino
(c) Buscar voos entre cidades
(d) Encontrar voo mais rápido
"""

def q8_a(numero_voo, voos):
    pass

def q8_b(voos):
    pass

def q8_c(origem, destino, voos):
    pass

def q8_d(origem, destino, voos):
    pass


# =========================================
# Q9 - Séries
# =========================================
"""
Sistema completo com menu:

- Cadastrar série
- Excluir série
- Adicionar temporada
- Marcar episódios
- Salvar estatísticas em arquivo
"""

def q9():
    pass


# =========================================
# Q10 - Perícia Criminal
# =========================================
"""
Funções:

(a) Calcular saldo correto das contas
(b) Identificar contas hackeadas
(c) Mostrar contas negativas hackeadas
(d) Calcular prejuízo total do banco
"""

def q10_a(historico, contas):
    pass

def q10_b(contas, saldos_corretos):
    pass

def q10_c(contas, contas_hackeadas, clientes):
    pass

def q10_d(contas_hackeadas):
    pass
def main():
    
    q2();
    
    
    
    return 0
if __name__ == "__main__":
    main()