#Exercícios da Aula 0: Fundamentos da programação estruturada
################################## Fatorial:
def fat(n):
    res = 1;
    while(n > 0):
        res = res * n;
        n = n -1;
    return res;
################################## Combinação: 
def comb(n,p):
    cima = fat(n);
    baixo = fat(p) * fat(n - p);
    return cima / baixo;
################################## Múltiplos:
def multiplos(k,n):
    for i in range(1,k+1):
        print(f'{n*i}');
################################## Divisor:
def divisor(x,y):
    if(y % x == 0):
        return True;
    else:
        return False;
##################################   Divisores:  
def divisores(k):
    for i in range(1,k):
        if(k % i == 0):
            print(f'{i}');
################################## Máximo Divisor Comum (MDC):
def mdc(m,n):
    mdc = 0;
    maior = 0;
    menor = 0;
    if(m > n):
        menor = n;
        maior = m;
    elif(n > m):
        menor = m;
        maior = n;
    for i in range(1,menor + 1):
        if(maior % i == 0 and menor % i == 0):
            mdc = i;
    print(f'{mdc}');
##################################    Primo: 
def primo(x):
    i = 1;
    cont = 0;
    while(i <= x):
        if(divisor(i,x)):
            cont +=1;
        i += 1;
    if(cont > 2):
        return False
    return True;
################################## Primos:
def primos(k):
    for num in range(1,k+1):
        if(primo(num)):
            print(f'{num}');     
    
##################################   Dama: 
def modulo(a):
    if(a < 0):
        a = a* -1;
    return a;
def dama(x,y,m,n):
    dif2 = 0;
    dif = 0;
    if(x== m and y == n):
        print(f'0');
    elif(x==m or y == n):
        print(f'0');
    else:
        dif = modulo(x-m);
        dif2 = modulo(y - n);
        if(dif == dif2):
            print(f'2');
################################## Acerola: [Maratona de Programação 2008] 
def suco(n,f):
    ml = f * 0.05;
    res = ml/n;
    print(f'{res:.2f}');
################################## Alarme Despertador: [Maratona de Programação 2009] 
def sono(Hatual,Matual,Halar,Malar):
    Tatual = (Hatual * 60) + Matual;
    Talar = (Halar * 60) + Malar;
    if Talar <= Tatual:
        Talar += 1440;
    Tsono = modulo(Talar - Tatual);
    print(f'{Tsono}');
    
def main():
    
    
    
    
    
    return 0
if __name__ == "__main__":
    main()