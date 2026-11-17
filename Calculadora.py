def somar(a, b): return a + b
def subtrair(a, b): return a - b
def multiplicar(a, b): return a * b
def dividir(a, b):
    if b == 0:
        raise ValueError("Não é possível dividir por zero.")
    return a / b

while True:
    op = input("\nOperação: (+, -,*, /): ")
    if op == "0":
        break
    a = float(input("\nDigite o primeiro número: "))
    b = float(input("Digite o segundo número: "))

    result = print(f"Resultado: {somar(a, b) if op == '+' else subtrair(a, b) if op == '-' else multiplicar(a, b) if op == '*' else dividir(a, b):.2f}")