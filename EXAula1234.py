#Exercícios (Parte I: Listas e Matrizes)
#Aula 1 
################################## Regressiva:
def listapar():
    l =[] ;
    i = 100;
    while(i > 0):
        l.append(i);
        i -= 2;
    return l;
################################## Metade: 
def meia():
    l = [];
    for i in range(10):
        n1 = int(input());
        n2 = n1/2;
        l.append(n2);
    print(l);
################################## Leitura: 
def ler(x):
    i = 0;
    l = [];
    while(i < x):
        n = int(input());
        l.append(n);
        i+= 1;
    return l;
##################################  Ocorrências: 
def ocorre(l,x):
    def ocorre(l,x):
        return l.count(x)
################################## Máximo: 
def max(l):
    l.sort();
    return l[len(l)-1]

################################## Posição do Máximo:
def pMax(l):
    i = 0;
    maior = max(l);
    while(i < len(l)):
        if(l[i] == maior):
            return i;
        i += 1;
        
################################## Inverter:
def invert(l):
    l.reverse()
    return l
#Aula 2 
################################## Fibonacci:
def fibo(n):
    seq = [];
    a = 1;
    b = 1;
    for i in range(n):
        seq.append(a);
        aux = a;
        a = b;
        b = aux + b;
    return seq;
################################## Ordenadas e abscissas:
def cord(obi,ord):
    ContPar = 0;
    ContImp = 0;
    for elem in obi:
        if(elem % 2 == 0):
            ContPar +=1;
    for item in ord:
        if(item % 2 != 0):
            ContImp += 1;
    aux = 0;
    if(ContPar >= ContImp):
        for num in obi:
            aux += num;
    else: 
        aux = 1;
        for ber in ord:
            aux  *= ber;
    print(aux);
################################## k Múltiplos: 
def multiplos(k,n):
    multi = [];
    for i in range(1,k+1):
        n2 = n * i;
        multi.append(n2);
    return multi;
#Aula 3 
################################## Média: 
def med():
    notas = [];
    media = 0;
    n = int(input());
    for i in range(n):
        nota = int(input());
        notas.append(nota);
        media += nota;
    media = media / n;
    acima = 0;
    for i in notas:
        if( i > 60):
            acima += 1;
    print(media);
    print(acima);       
################################## Temperaturas: 
def temp():
    tempDias = [];
    media = 0;
    n = int(input());
    for i in range(n):
        grau = int(input());
        tempDias.append(grau);
        media += grau;
    media = media / n;
    baixo = 0;
    for i in tempDias:
        if( i < media):
            baixo += 1;
    print(baixo);
            
################################## Iguais: 
def iguais(l1,l2):
    aux = 0;
    i = 0;
    while i < len(l1):
        if l1[i] == l2[i]:
            aux += 1;
        i += 1
    print(aux);
################################## Salários: 
def salary(n):
    aux = [];
    med = 0;
    nomes = [];
    Salarios = [];
    for i in range(n):
        nome = input();
        salario = float(input());
        nomes.append(nome);
        Salarios.append(salario);
        med += salario;
    med = med / n;
    for sal in range(len(Salarios)):
        if Salarios[sal] > med:
            aux.append(sal);
    j = 0;
    while j < len(aux):
        h = aux[j];
        print(nomes[h]);
        j += 1;        
################################## Sublista: 
def sublist(l,x,y):
    sub = [];
    for i in l:
        if i > x and i < y:
            sub.append(i);
    return sub;
################################## Troca de Cartas:
def presente(x,z):
    for elem in x:
        if(elem == z):
            return True;

def depurar(lista):
    l2 = [];
    for x in lista:
        if not presente(x,l2):
            l2.append(x);
    return l2;

def MaxtradeCards(Alice, Beatriz):
    #retirar as repetidas de cada um
    alice = depurar(Alice);
    bia = depurar(Beatriz);
    
    so_alice = [];
    so_bia = [];
    
    for i in alice:
        if not presente(i, bia):
            so_alice.append(i);

    for j in bia:
        if not presente(j, alice):
            so_bia.append(j);

    if len(so_alice) < len(so_bia):
        return len(so_alice);
    else:
        return len(so_bia);


#Aula 4 (Matrizes)
################################## Criar Matriz:
def criarMatrizNula(m,n):
    x = [];
    for i in range(m):
        y = [];
        for j in range(n):
            y.append(0);
        x.append(y);
    return x;
################################## Imprimir Matriz:
def imprimematriz(m):
    for i in m:
        for j in i:
            print(f'', end = '\t');
        print();
################################## Somar Matrizes: 
def somaMatriz(a,b):
    x = [];
    for any in range(len(a[0])): # erro anterior: len(any)
        y = [];
        for thing in range(len(any)):
            y.append(0);
        x.append(y);
    i = 0;
    while i < len(a):
        num = 0;
        j = 0;
        while j < len(a[i]): #erro anterior: len(i)
            num = a[i][j] + b[i][j] #erro anterior: i[j] + b[i][j];
            x[i][j] = num
            j += 1;
        i += 1;
    return x;
            
################################## Notas: 
def notas():
    m = int(input("Digite o número de alunos")); # número de linhas
    n = int(input("Digite o número de notas")); # numero de colunas
    Neo = [];
    
    mediaTurma = 0;
    somaDasMedias = 0;
    
    for i in range(m):
        trinity = [];
        for j in range(len(n)):
            note = int(input());
            trinity.append(note);    
        Neo.append(trinity);
    for aluno in range(len(Neo)):
        media = 0;
        for pontos in range(len(aluno)):
            media += aluno[pontos];
        media = media / n;
        print(f'Aluno{aluno + 1}: {media:.1f}');
        somaDasMedias += media;
    mediaTurma = somaDasMedias / m;
    print(f'Média da turma: {mediaTurma:.1f}');
################################## Matriz identidade:
def ma_Identidade(m):
    aux = 0;
    cont = 0;
    limit = len(m);
    for i in range(limit):
        if(m[i][i] == 1):
            aux += 1;
        else:
            return False
    for j in range(limit):
        for k in range(len(m[i])):
            if(m[j][k] == 1):
                cont += 1; 
    if(aux == limit and aux == cont):
        return True;
    else:
        return False;
################################## Determinante: 
def ma_Determinante_m3x3(m):
    a = m[0][0];
    b = m[0][1];
    c = m[0][2];
    d = m[1][0];
    e = m[1][1];
    f = m[1][2];
    g = m[2][0];
    h = m[2][1];
    i = m[2][2];
    determinante = (a*e*i) + (b*f*g) + (c*d*h) - (a*f*h) - (b*d*i) - (c*e*g);
    return determinante;
################################## Triangular inferior da transposta de uma matriz: 
#não fui capaz de solucionar esse problema sozinho, necessitei de ajuda para compreendê-lo, quando vi a relação dos indices opostos já era tarde demais.
def ma_triangulo(m):
    for i in range(len(m)):
        for j in range(i + 1, len(m)): # como os números da diagonal da matriz não se alteram precio apenas alterar os que estão fora dela, então para acessá-los preciso ir +1 no indice
            aux = m[i][j]; # guarda o valor dentro do indíce acima da diagonal 
            m[i][j] = m[j][i]; # troca com seu oposto abaixo da diagonal
            m[j][i] = aux; # e o abaixo da diagonal recebe o valor do seu oposto acima
    
    for i in range(len(m)):
        for j in range(i+1,len(m)): # isolando somente os que estão acima da diagonal
            m[i][j] = 0; # subistituindo seus valores por zero paratransformar a matriz em triangular inferior
    
    for line in m:
        print(line);         
################################## Cavalo:
def horse(m):
    movPossivel = 0;
    coor = [(-2, -1),(-2, +1),(-1, -2),(-1, +2),(+1, -2),(+1, +2),(+2, -1),(+2, +1)]; # todas as coordenadas de i e j possíveis para o cavalo
    x , y = 0, 0;
    for i in range(len(m)):
        for j in range(len(i)):
            if(m[i][j] == 1):
                x = i;
                y = j;
    for (cx , cy) in coor:
        novoX = x + cx;
        novoY = y + cy;
        if( (novoX >= 0 and novoX < len(m) and novoY >= 0 and novoY < len(m))): # caso algum ponto esteja fora do tabuleiro é retirado da conta aqui
           movPossivel += 1; 
    print(movPossivel);
################################## Robô Colecionador:
def roboColecionador(arena,toDos):
#temos a arena na qual (. = nada; * = figura; # = pilastra)
#‘N’, ‘S’, ‘L’, ‘O’ - orienta¸c˜ao inicial do robˆo (Norte, Sul, Leste e Oeste)
#‘D’ - “gire 90 graus para a direita”
#‘E’ - “gire 90 graus para a esquerda”
#‘F’ - “ande uma célula para a frente”
    pontos = 0;
    xRobo, yRobo = 0, 0;
    sentido = "";
    for linha in len(arena):
        for casa in len(arena[linha]):
            if (arena[linha][casa] == 'N' or arena[linha][casa] == 'S' or arena[linha][casa] == 'L' or arena[linha][casa] == 'O') :
                xRobo = linha;
                yRobo = casa;
                sentido = arena[linha][casa];

    m = len(arena);
    for fazeres in toDos:
        for i in range(m):
            for j in range(len(arena[i])):
                if sentido
        
    
    
    
    
    
    
    
    
    
    
    
    