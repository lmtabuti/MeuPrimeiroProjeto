# Recebe os dois números
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))
nome = input("Digite seu nome: ")

# Calcula as operações
soma = num1 + num2
diferenca = num1 - num2
produto = num1 * num2
quociente = num1 / num2

# Exibe os resultados em linhas separadas
print(f"\nCálculos realizados por {nome}")
print(f"Soma: {soma}")
print(f"Diferença: {diferenca}")
print(f"Produto: {produto}")
print(f"Quociente: {quociente}")
