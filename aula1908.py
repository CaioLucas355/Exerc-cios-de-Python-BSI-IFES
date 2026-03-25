def main(): #função principal do programa
    a = int(input()) #entrada de dados via teclado com conversão para inteiro
    print(f'{a/3:.4f}') #saída de dados com f-string decimal com 4 casas

    return 0 #toda função tem retorno

if __name__ == "__main__": #prepara a invocação da função
    main() #invocação da função

#------------------------------------------------------------------
'''
Faça um programa em python que calcule a média aritmética 
entre quatro notas quaisquer fornecidas pelo usuário.
'''
def main(): #função principal do programa
    #declaração de variáveis
    n1 = float(0.0) #atribuição direta para simular uma declaração de variável
    n2 = float(0.0)
    n3 = float(0.0)
    n4 = float(0.0)
    media = float(0.0)

    #entrada de dados
    n1 = float(input("Digite a Nota 1: ")) #atribuição por input
    n2 = float(input("Digite a Nota 2: "))
    n3 = float(input("Digite a Nota 3: "))
    n4 = float(input("Digite a Nota 4 :"))

    #processamento de dados
    media = (n1 + n2 + n3 + n4) / 4 #atribuição por expressão aritmética

    #saída de dados
    print(f'{media:.2f}')

    return 0 #toda função tem retorno

if __name__ == "__main__": #prepara a invocação da função
    main() #invocação da função
	