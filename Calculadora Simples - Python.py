def calcular():
    print("Calculadora")
    print("Operações disponíveis: +, -, *, /")

    try:
        numero1 = float(input("Digite o primeiro número: "))
        operador = input("Digite a operação: ").strip()
        numero2 = float(input("Digite o segundo número: "))

        if operador == "+":
            resultado = numero1 + numero2
        elif operador == "-":
            resultado = numero1 - numero2
        elif operador == "*":
            resultado = numero1 * numero2
        elif operador == "/":
            if numero2 == 0:
                print("Erro: não é possível dividir por zero.")
                return
            resultado = numero1 / numero2
        else:
            print("Operação inválida.")
            return

        print(f"Resultado: {resultado}")
    except ValueError:
        print("Entrada inválida: digite números válidos.")


if __name__ == "__main__":
    calcular()