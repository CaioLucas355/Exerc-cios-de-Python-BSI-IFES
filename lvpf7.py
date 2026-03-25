#LVP FUNÇÃO 7
def f_mais_proximo(a):
    #declaração de variáveis
    i = int(0)    
    j = int(0)    
    
    #processamento
    i = 1 #IVC
    while (i ** 2 < a): #CP
        i += 1 #AVC
    
    j = i - 1

    if (a - j ** 2 < i ** 2 - a):
        return j
    return i

    
def f_raizNewton(a):
    #declaração de variáveis
    x = int(0)
    x2 = int(0)
    
    x = f_mais_proximo(a)
    x2 = x ** 2
    
    return (a+x2)/(2*x)
    
def main():
    #declaração de variaveis
    n = int(0)
    
    #entrada de dados
    n = int(input()) #1 IVC
    #processamento e saída
    while (n >= 0): #2 CP
        print(f'N={n:.4f} RAIZ={f_raizNewton(n):.6f}')
        n = int(input()) #3 AVC
        
    return 0

if __name__ == "__main__":
    main()