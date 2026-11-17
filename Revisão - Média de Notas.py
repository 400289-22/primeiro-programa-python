print("\n----------- MÉDIA DE NOTAS -----------\n")

soma = 0

for i in range(1, 5):
    nota = float(input(f"Digite a {i}ª nota do aluno: "))

    soma = soma + nota
    nota_final = soma / 4

print(f"A média do aluno é igual a:  {nota_final:.2}\n")

if nota_final >= 7:
    print("O aluno foi aprovado!\n")
else:
    print("O aluno foi reprovado.\n")
