#LVP FUNÇÃO 6
def f_fatorial(x):
    #declaração de variáveis
    f = int(0)
    
    #inicialização de variável
    f = 1
    #processamento
    for i in range(1,x+1):
        f = f * i  #f *= i
    
    return f
    
def main():
    #declaração de variáveis
    n = int(0)
    
    #entrada de dados
    n = int(input()) #IVC
   
    #processamento e saída
    while(n >= 0): #CP
        print(f'Fatorial({n})={f_fatorial(n)}')
        n = int(input()) #AVC
    
    return 0
    
if __name__ == "__main__":
    main()