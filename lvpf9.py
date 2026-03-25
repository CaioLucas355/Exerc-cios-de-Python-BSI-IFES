#LVP FUNÇÃO 9 - Conversão BIN e HEX
def f_bin(n): #definir função para conversão em binário
    v = str("") #a variável de retorno é uma string
    while (n > 0): #enquanto n for maior que zero, a repetição ocorre
        resto = n % 2 #pega o valor do resto de n por 2
        v = str(resto) + v #adiciona o valor do resto na string
        n = n // 2 #fatia o valor n por 2 até chegar em zero
    return v #retorna o valor binário
    
def f_hex(n): #definir função para conversão em hexadecimal
    v = str("") #a variável de retorno é uma string
    while (n > 0): #enquanto n for maior que zero, a repetição ocorre
        resto = n % 16 #pega o valor do resto de n por 16
        #Testa se o valor do resto é maior que 9, para atribuição das letras
        if (resto == 10):
            resto = "A"
        elif (resto == 11):
            resto = "B"
        elif (resto == 12):
            resto = "C"
        elif (resto == 13):
            resto = "D"
        elif (resto == 14):
            resto = "E"
        elif (resto == 15):
            resto = "F"
            
        v = str(resto) + v #adiciona o valor do resto na string
        n = n // 16 #fatia o valor n por 16 até chegar em zero
    return v #retorna o valor hexadecimal

def main():
    #declaração de variáveis
    n = int(0)
    binario = int(0)
    hexadecimal = str("")
    
    #entrada
    n = int(input())
    
    #processamento
    binario = f_bin(n)
    hexadecimal = f_hex(n)
    
    #saida
    print(f'DEC={n} BIN={binario} HEX={hexadecimal}')
    
    return 0

if __name__ == "__main__":
    main()
#---------------------------------------   
#LVP FUNÇÃO 9 - Conversão BIN e HEX
def f_bin(n): #definir função para conversão em binário
    v = str("") #a variável de retorno é uma string
    while (n > 0): #enquanto n for maior que zero, a repetição ocorre
        resto = n % 2 #pega o valor do resto de n por 2
        v = str(resto) + v #adiciona o valor do resto na string
        n = n // 2 #fatia o valor n por 2 até chegar em zero
    return v #retorna o valor binário

def f_hex_letra(valor):
    if (valor == 10):
        valor = "A"
    elif (valor == 11):
        valor = "B"
    elif (valor == 12):
        valor = "C"
    elif (valor == 13):
        valor = "D"
    elif (valor == 14):
        valor = "E"
    elif (valor == 15):
        valor = "F"    
    return valor
    
def f_hex(n): #definir função para conversão em hexadecimal
    v = str("") #a variável de retorno é uma string
    while (n > 0): #enquanto n for maior que zero, a repetição ocorre
        resto = n % 16 #pega o valor do resto de n por 16
        #Testa se o valor do resto é maior que 9, para atribuição das letras
        if (resto > 9):
            resto = f_hex_letra(resto)
            
        v = str(resto) + v #adiciona o valor do resto na string
        n = n // 16 #fatia o valor n por 16 até chegar em zero
    return v #retorna o valor hexadecimal

def main():
    #declaração de variáveis
    n = int(0)
    binario = int(0)
    hexadecimal = str("")
    
    #entrada
    n = int(input())
    
    #processamento
    binario = f_bin(n)
    hexadecimal = f_hex(n)
    
    #saida
    print(f'DEC={n} BIN={binario} HEX={hexadecimal}')
    
    return 0

if __name__ == "__main__":
    main() 
#---------------------------------------  
#LVP FUNÇÃO 9 - Conversão BIN e HEX
def f_bin(n): #definir função para conversão em binário
    v = str("") #a variável de retorno é uma string
    while (n > 0): #enquanto n for maior que zero, a repetição ocorre
        resto = n % 2 #pega o valor do resto de n por 2
        v = str(resto) + v #adiciona o valor do resto na string
        n = n // 2 #fatia o valor n por 2 até chegar em zero
    return v #retorna o valor binário

def f_hex_letra(valor):
    h = "ABCDEF"
    #    012345
    return h[valor-10]

    
def f_hex(n): #definir função para conversão em hexadecimal
    v = str("") #a variável de retorno é uma string
    while (n > 0): #enquanto n for maior que zero, a repetição ocorre
        resto = n % 16 #pega o valor do resto de n por 16
        #Testa se o valor do resto é maior que 9, para atribuição das letras
        if (resto > 9):
            resto = f_hex_letra(resto)
            
        v = str(resto) + v #adiciona o valor do resto na string
        n = n // 16 #fatia o valor n por 16 até chegar em zero
    return v #retorna o valor hexadecimal

def main():
    #declaração de variáveis
    n = int(0)
    binario = int(0)
    hexadecimal = str("")
    
    #entrada
    n = int(input()) #IVC
    while (n >= 0): #CP
        #processamento
        binario = f_bin(n)
        hexadecimal = f_hex(n)
        
        #saida
        print(f'DEC={n} BIN={binario} HEX={hexadecimal}')
        n = int(input()) #AVC
        
    return 0

if __name__ == "__main__":
    main()