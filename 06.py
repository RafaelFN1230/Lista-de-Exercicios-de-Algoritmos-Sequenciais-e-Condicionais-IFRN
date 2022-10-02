'''
6. O restaurante a quilo Bem-Bão cobra R$12,00 por cada quilo de refeição. Escreva um algoritmo
que leia o peso do prato montado pelo cliente (em quilos) e imprima o valor a pagar. Assuma que a
balança já desconte o peso do prato.
'''

print("Olá, bem vindo ao restaurante Bem-Bão")
Valor_quilo=12.00
Peso_prato=float(input("Insira aqui o peso do prato: "))
Total=Peso_prato*Valor_quilo
print("O valor total a se pagar é de: R$",Total)