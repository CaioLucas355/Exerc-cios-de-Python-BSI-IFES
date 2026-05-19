# -----------------------------------------
# Recursão
# -----------------------------------------
#Fatorial recursivo:
def fatRec(n):
    if n == 0:  #caso base
        return 1;
    else:
        return n * fatRec(n-1); #autochamada + progresso para o caso base
# -----------------------------------------
#Soma recursiva dos elementos de uma lista:
def somaRec(l,p = 0):
    if p == len(l):
        return 0;
    else:
        return l[p] + somaRec(l, p + 1);
# -----------------------------------------
#Fibonacci recursivo:
def fiboIt(k):
    a = 1;
    b = 1;
    for i in range(k-2):
        c = a + b
        a = b
        b = c
    return b;

def fiboRec(k):
    if k == 1 or k == 2:
        return 1;
    else:
        return fiboRec(k-1) + fiboRec(k-2)

#Existe uma diferênça exorbitante entre as duas, mais amostra quando realizasse com o k para valores cada vez maiores, isso porque enquanto a iterativa apenas relaiza uma simples soma
#a Recursiva divide uma operação em duas e essas duas em duas, sendo um crescimento exponencial realizando um trabalho repetitivo e e complicando os cálculos

# -----------------------------------------
#Exponenciacao recursiva:
def exp(x,y):
    if y == 1:
        return x;
    else:
        return x * exp(x,y-1);
    
# -----------------------------------------
#Maior elemento de uma lista recursivo:
def mElemRec(l):
    if len(l) == 0:
#-----------------------------------------
#Maximo Divisor Comum recursivo
def mdcRec(x,y):
    
# -----------------------------------------
#Inversao

# -----------------------------------------
#Torre de Hanoi

# -----------------------------------------
#Permuta¸c˜oes - Impress˜ao

# -----------------------------------------
#Permuta¸c˜oes:

# -----------------------------------------
