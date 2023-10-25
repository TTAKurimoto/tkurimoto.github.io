#EXERCÍCIOS PRÁTICOS:

#1. Complete o código para solicitar ao usuário que insira seu nome e, em seguida, imprimir "Olá, [nome]!".
nome = input("Digite seu nome: ")
# Complete o código aqui
print("Olá, " + nome + "!")



#2.Complete o código para verificar se a variável idade é maior ou igual a 13 e menor ou igual a 16.
idade = int(input("Digite sua idade: "))
if idade >= 13 and idade <= 16:
    print("Você está na faixa etária correta.")
else:
    print("Você não está na faixa etária correta.")



#3.Complete o código para calcular a soma de dois números e imprimir o resultado.
# Solicitar ao usuário que insira o primeiro número
num1 = float(input("Digite o primeiro número: "))
# Solicitar ao usuário que insira o segundo número
num2 = float(input("Digite o segundo número: "))

# Complete o código aqui para calcular a soma e imprimir o resultado
soma = num1 + num2
print("A soma é:", soma)



#4.Faça um Programa que peça um número e então mostre a mensagem O número informado foi [número].
# Declaração de variável
numero = int(input("Digite um número: "))
# Impressão do número informado
print(f"O número informado foi {numero}")



#5.Faça um Programa que peça dois números e imprima a soma.
# Declaração de variáveis
numero1 = int(input("Digite o primeiro número: "))
numero2 = int(input("Digite o segundo número: "))
# Cálculo da soma
soma = numero1 + numero2
# Impressão da soma
print(f"A soma dos números é {soma}")



#6.Faça um Programa que peça as 4 notas bimestrais e mostre a média.
# Declaração de variáveis
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))
nota4 = float(input("Digite a quarta nota: "))
# Cálculo da média
media = (nota1 + nota2 + nota3 + nota4) / 4
# Impressão da média
print(f"A média é {media}")



#7.Faça um Programa que converta metros para centímetros.
# Declaração de variável
metros = float(input("Digite a medida em metros: "))
# Conversão para centímetros
centimetros = metros * 100
# Impressão do resultado
print(f"A medida em centímetros é {centimetros}")
print(f"A medida em centímetros é {centimetros:.2f}")



#8.Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês.
# Declaração de variáveis
salario_hora = float(input("Quanto você ganha por hora? "))
horas_trabalhadas = float(input("Quantas horas você trabalhou no mês? "))
# Cálculo do salário
salario = salario_hora * horas_trabalhadas
# Impressão do salário
print(f"Seu salário no mês é de R$ {salario:.2f}")



#9.Faça um Programa que peça dois números e imprima o maior deles.
# Declaração de variáveis
numero1 = float(input("Digite o primeiro número: "))
numero2 = float(input("Digite o segundo número: "))
# Comparação dos números
if numero1 > numero2:
    maior_numero = numero1
else:
    maior_numero = numero2

# Impressão do resultado
print(f"O maior número é {maior_numero}")



#10.Faça um programa para a leitura de duas notas parciais de um aluno. O programa deve calcular a média alcançada por aluno e apresentar:
#•	A mensagem "Aprovado", se a média alcançada for maior ou igual a sete;
#•	A mensagem "Reprovado", se a média for menor do que sete;
#•	A mensagem "Aprovado com Distinção", se a média for igual a dez.
# Declaração de variáveis
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
# Cálculo da média
media = (nota1 + nota2) / 2
# Verificação da situação do aluno
if media >= 7:
    print("Aprovado")
elif media == 10:
    print("Aprovado com Distinção")
else:
    print("Reprovado")
