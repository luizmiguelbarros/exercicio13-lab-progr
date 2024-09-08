while True:
    nome = input("Digite um nome (ou 'fim' para encerrar): ")
    if nome.lower() == "fim":
        break
    
    # Imprime o nome em caixa alta (maiúsculas)
    print(nome.upper())
