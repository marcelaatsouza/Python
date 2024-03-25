import math

# 4- Escreva um programa em Python para calcular o valor de uma prestação em atraso(prestacao). Para isso, obtenha o valor da prestação (valorPrestacao), a porcentagem de multa pelo atraso (multa) e a quantidade de dias de atraso (qtdeDias). Calcular e mostrar o valor da prestação atualizado, sabendo que: prestacao=valorPrestacao+(valorPrestacao*(multa/100)*qtdeDias)

valorPrestacao = float(input("Digite o valor da prestação: "))
multa = float(input("Digite o valor da multa pelo atraso: "))
qtdeDias = float(input("Digite o valor da quantidade de dias de atraso: "))

prestacaoAtualizada = valorPrestacao + (valorPrestacao * (multa/100) * qtdeDias)

print("O valor da prestação atualizado é: ", prestacaoAtualizada)

# 5- Faça um programa em Python que peça do usuário um valor em graus para um ângulo. Converta-o para radianos e, usando funções da biblioteca math, imprima o seno,cosseno e tangente deste ângulo.

angulo = float(input("Digite o valor do ângulo em graus: "))
radiano = math.radians(angulo)
seno = math.sin(radiano)
cosseno = math.cos(radiano)
tangente = math.tan(radiano)

print("O valor do seno é: ", seno, "\nO valor do cosseno: ", cosseno, "\nO valor da tangente é: ", tangente)