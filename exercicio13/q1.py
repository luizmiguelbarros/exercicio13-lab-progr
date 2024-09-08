# Lê o número inteiro N
N = int(input("Digite o valor de N: "))

# Loop para ler N números reais
for i in range(1, N + 1):
    numero = float(input(f"Digite o número real {i}: "))
    # Imprime o número arredondado para 1 casa decimal
    print(f"Número {i} arredondado: {round(numero, 1)}")
