print("\n----------- PAR OU ÍMPAR ----------\n")

print("Digite 000 para encerrar o programa.\n")

while True:
    num = int(input("Digite um número inteiro: "))
    
    if num == 000:
        print("Programa encerrado.")
        break

    if num % 2 == 0:
        print(f"{num} é um número par.")

    else:
        print(f"{num} é um número ímpar.")
    continue

