def main():
    
    #variáveis
    contNimparePositivo = int(0);
    contNpositivo = int(0);
    contNpareNegativo = int(0);
    somaNparesNegativos = int(0.0);
    contNnegativo = int(0);
    qtd_Cadastro = int(0);
    primeiroNumero = bool();
    flag = int(0);
    maiorNum = int(0);
    menorNum = int(0);
    totalN = int(0);
    porcentagemNpositivo = float(0.0);
    medNparNegativo  = float(0.0);
    
    
    #processamento
    contNimparePositivo = 0;
    contNpositivo = 0;
    contNpareNegativo = 0;
    somaNparesNegativos = 0;
    contNnegativo = 0;
    qtd_Cadastro = 0;
    primeiroNumero = True;
    flag = 1
    while(flag!=0): #CP
        num = int(input());
        #----------
        qtd_Cadastro += 1; # qnt de pessoas cadastradas
        #----------
        if(primeiroNumero == True):
            maiorNum = num;
            menorNum = num;
            primeiroNumero = False;
        elif(num > maiorNum):
            maiorNum = num;
        elif(num < menorNum):
            menorNum = num;
        #---------------------------
        if(num < 0):
            contNnegativo +=1;
            if((num % 2) == 0):
                somaNparesNegativos += num
                contNpareNegativo +=1;
        elif(num > 0):
            contNpositivo +=1;
            if((num % 2) != 0):
                contNimparePositivo += 1;
        #----------
        
        flag = num;#AVC
    
    #processamento
    totalN = contNnegativo + contNpositivo;
    porcentagemNpositivo = (contNpositivo / totalN) * 100;
    
    medNparNegativo = somaNparesNegativos / contNpareNegativo; #média média dos números pares negativos.
    
    
    # saída
    print(f'Maior número: {maiorNum}\nMenor número: {menorNum}\nMédia dos pares negativos: {medNparNegativo:.1f}\nQuantidade de ímpares positivos:  {contNimparePositivo}\nPorcentagem de positivos: {porcentagemNpositivo:.1f}%');



if __name__ == "__main__":
    main()