'''
5. Um motorista deseja colocar no seu tanque X reais de gasolina. Escreva um algoritmo para ler o
preço do litro da gasolina e o valor do pagamento, e exibir quantos litros ele conseguiu colocar no
tanque.
'''


Valor_gas=float(input("Insira aqui o valor da gasolina: "))
Valor_pag=float(input("insira aqui o valor do pagamento: "))
Litro_gas=Valor_pag/Valor_gas
print("Você consegue comprar",Litro_gas,"litros de gasolina.")