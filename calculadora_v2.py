saida = ''
def adicao(a, b):
    return a + b
def subtracao(a, b):
    return a - b
def multiplicacao(a, b):
    return a * b
def divisao(a, b):
    if b == 0:
        return "Não foi possível realizar a divisão por 0"
    return a / b
def calculadora(num1, num2, operacao):
    if operacao == '+' or operacao == 'adicao':
        resultado = adicao(num1, num2)
    elif operacao == '-' or operacao == 'subtracao':
        resultado = subtracao(num1, num2)
    elif operacao == '*' or operacao == 'multiplicacao':
        resultado = multiplicacao(num1, num2)
    elif operacao == '/' or operacao == 'divisao':
        resultado = divisao(num1, num2)
    else:
        resultado = "Operação inválida"
    return resultado
while saida.lower() != 'n':
    try:
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))
        operacao = input("Digite a operação matemática (+, -, *, / ou adicao, subtracao, multiplicacao, divisao): ")
        resultado = calculadora(num1, num2, operacao)
        print('Resultado da operação: ', resultado)
    except ValueError:
        print("Por favor, digite um número válido.")
    
    saida = input("Deseja continuar? (S/N): ").lower()
    if saida not in ['s', 'n']:
        print("Entrada inválida. Por favor, digite 'S' para sim ou 'N' para não.")
        saida = input("Deseja continuar? (S/N): ").lower()

print("Programa encerrado.")