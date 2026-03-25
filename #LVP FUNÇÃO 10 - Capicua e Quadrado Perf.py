#LVP FUNÇÃO 10 - Capicua e Quadrado Perfeito
# Título/comentário do programa. O código busca números no intervalo [1, 5000] que são Capicua e/ou Quadrados Perfeitos.
def f_tam(n):
    # Define a função 'f_tam' para calcular o número de dígitos (tamanho) de um número inteiro 'n'.
    #declaração de variáveis
    # Comentário sobre a declaração.
    cont = 0
    # Inicializa o contador de dígitos.
    while (n > 0):
        # Inicia um loop que continua enquanto 'n' for positivo.
        n = n // 10
        # Divide 'n' por 10 usando divisão inteira (remove o último dígito).
        cont += 1
        # Incrementa o contador de dígitos.
    return cont
    # Retorna o número total de dígitos.

def f_inverte(n):
    # Define a função 'f_inverte' para inverter a ordem dos dígitos de um número 'n'.
    #declaração de variáveis
    # Comentário sobre a declaração.
    tam = int(0)
    # Variável para armazenar o número de dígitos.
    invertido = int(0)
    # Variável para armazenar o número invertido.
    
    tam = f_tam(n)
    # Chama a função 'f_tam' para obter o número de dígitos de 'n'.
    
    pot = tam - 1
    # Inicializa a variável 'pot' (potência de 10) com o índice do dígito mais significativo (ex: para 123, tam=3, pot=2).
    while (n > 0):
        # Inicia um loop que processa os dígitos, do menos significativo para o mais significativo.
        resto = n % 10
        # Obtém o último dígito de 'n' (o resto da divisão por 10).
        invertido += resto*10**pot
        # Adiciona o dígito extraído ('resto') ao número 'invertido', multiplicando-o pela potência correta de 10.
        pot = pot - 1
        # Decrementa a potência para o próximo dígito.
        n = n // 10
        # Remove o último dígito de 'n' (divisão inteira por 10).

    return invertido
    # Retorna o número com os dígitos invertidos.
        

def f_capicua(n):
    # Define a função 'f_capicua' para verificar se um número 'n' é Capicua (palíndromo numérico).
    # Capicua é um número que é lido da mesma forma da esquerda para a direita ou vice-versa.
    #declaração de variáveis
    # Comentário sobre a declaração.
    invertido = int(0)
    # Variável para armazenar o número invertido.
    
    invertido = f_inverte(n)
    # Chama a função 'f_inverte' para obter o número invertido.
    
    if (n == invertido and n > 9):
    # Condição para ser Capicua: o número original deve ser igual ao seu inverso E deve ter mais de um dígito (n > 9).
        return True
    # Se for Capicua, retorna True.
    
    return False
    # Se não for Capicua, retorna False.

def f_quadradoPerfeito(n):
    # Define a função 'f_quadradoPerfeito' para verificar se 'n' é um quadrado perfeito (raiz quadrada inteira).
    metade = (n // 2)
    # Calcula a metade de 'n' (divisão inteira). O maior possível fator quadrado a ser testado é n/2 (para n=4, 2*2=4).
    if (n == 1):
    # Trata o caso especial: 1 é um quadrado perfeito (1*1=1).
        return True
    
    for i in range(metade,0,-1):
    # Inicia um loop que itera de 'metade' (n // 2) até 1, decrementando de 1 em 1.
    # A iteração de trás para frente visa otimizar, buscando o fator mais provável primeiro.
        if (i ** 2 == n):
    # Condição: Se o quadrado do número atual 'i' for igual a 'n'.
            return True
    # Se encontrar um fator, 'n' é quadrado perfeito e retorna True.
    return False
    # Se o loop terminar sem encontrar um fator, 'n' não é quadrado perfeito e retorna False.

def main():
    # Define a função principal 'main', que executa a lógica de busca e impressão.
    
    for i in range(1,5001):
    # Inicia um loop que itera por todos os números inteiros 'i' de 1 até 5000 (inclusive).
        if (f_capicua(i) and f_quadradoPerfeito(i)):
        # Verifica a condição mais restritiva primeiro: se 'i' é Capicua E Quadrado Perfeito.
            print(f'{i} É CAPICUA E QUADRADO PERFEITO')
            # Imprime o resultado para o número 'i'.
        elif (f_capicua(i)):
        # Se não for ambas, verifica se é Capicua.
            print(f'{i} É CAPICUA')
            # Imprime o resultado para Capicua.
        elif (f_quadradoPerfeito(i)):
        # Se não for Capicua, verifica se é Quadrado Perfeito.
            print(f'{i} É QUADRADO PERFEITO')
            # Imprime o resultado para Quadrado Perfeito.

    return 0
    # Retorna 0, indicando o fim da execução do programa.
    
if __name__ == "__main__":
    # Esta estrutura garante que a função 'main' só será executada quando o script for rodado diretamente.
    main()
    # Chama a função 'main' para iniciar o programa.