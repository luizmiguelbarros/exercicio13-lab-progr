import math

# Lê o número inteiro N
N = int(input("Digite o valor de N: "))

# Verifica se o número é par ou ímpar
if N % 2 == 0:
    # Se N for par, lê N/2 números reais
    qtd_numeros = N // 2
    print(f"Lendo {qtd_numeros} números para calcular as raízes quadradas:")
    
    for i in range(1, qtd_numeros + 1):
        numero = float(input(f"Digite o número real {i}: "))
        # Calcula e imprime a raiz quadrada do número
        print(f"Raiz quadrada de {numero}: {math.sqrt(numero):.2f}")
else:
    # Se N for ímpar, lê N*2 números reais
    qtd_numeros = N * 2
    print(f"Lendo {qtd_numeros} números para calcular as raízes cúbicas:")
    
    for i in range(1, qtd_numeros + 1):
        numero = float(input(f"Digite o número real {i}: "))
        # Calcula e imprime a raiz cúbica do número
        print(f"Raiz cúbica de {numero}: {numero**(1/3):.2f}")
