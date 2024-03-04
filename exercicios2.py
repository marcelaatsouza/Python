# 1. Desenvolva um programa em Python que solicite ao usuário os valores dos lados de um retângulo e calcule e mostre seu perímetro e sua área.
a = float(input("Digite o primeiro lado do retângulo: "))
b = float(input("Digite o segundo lado do retângulo: "))
area = a * b
perimetro = 2 * (a + b)
print("A área do retângulo é:", area)
print("O perímetro do retângulo é:", perimetro)

# 2. Escreva um programa em Python que solicite ao usuário o salário atual e mostre o salário acrescido de 5% de comissão.
salario_atual = float(input("Digite o seu salário atual: "))
comissao = salario_atual * 0.05
novo_salario = salario_atual + comissao
print("O valor do novo salário é:", novo_salario)

# 3. Escreva um programa em Python que solicite ao usuário a distância entre duas cidades e o tempo de viagem. O programa deverá calcular e exibir a velocidade média de um carro que vai de uma cidade para outra.
distancia = float(input("Digite a distância entre as cidades: "))
tempo= float(input("Digite o tempo de viagem: "))
vm = distancia / tempo
print("A velocidade média de um carro que viaja de uma cidade para a outra é de " , vm)

# 4. Escreva um programa em Python que calcule as duas raízes de uma equação de 2º grau ax²+bx+c, conhecendo os valores dos coeficientes da mesma (a, b, c). Suponha que as raízes são reais.
a = float(input("Digite o valor de a: "))
b = float(input("Digite o valor de b: "))
c = float(input("Digite o valor de c: "))
discriminante = b**2 - 4*a*c
if(discriminante < 0):
    print("Não possui raízes reais.")
else:
    raiz1 = (-b + discriminante**0.5) / (2*a)
    raiz2 = (-b - discriminante**0.5) / (2*a)
    print("As raízes da equação são:", raiz1, "e", raiz2)

# 5. Escreva um programa em Python que leia a cotação dodólar (taxa de conversão), leia um valor em dólares e converta e mostre o valor equivalente em Reais.
cotacao = float(input("Digite a cotação atual do dólar: "))
valor_dolar = float(input("Digite o valor a ser convertido: "))
valor_real = valor_dolar * cotacao
print(valor_dolar, "dólares equivalem a", valor_real, "reais.")

# 6. Escreva um programa em Python que leia um valor representando o gasto realizado por um cliente do restaurante ComaBem e visualize o valor total a ser pago, considerandoos 10% do garçom.
gasto_cliente = float(input("Digite o valor gasto no restaurante: "))
comissao_garcom = gasto_cliente * 0.1
total = gasto_cliente + comissao_garcom
print("O valor total da conta é de:", total)

# 7. Escreva um programa em Python que obtenha uma temperatura em graus Celsius, calcule e mostre a respectiva temperatura nas escalas Fahrenheit e Kelvin.
celsius = float(input("Digite a temperatura em graus celsius: "))
fahrenheit = (celsius * 1.8) + 32
kelvin = celsius + 273
print("O valor de", celsius, "graus celsius é de", fahrenheit, "graus fahrenheit e", kelvin, "graus kelvin.")