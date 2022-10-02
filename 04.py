'''
4. Escreva um algoritmo para ler o nome e a idade de uma pessoa, e exibir quantos dias de vida
ela possui. Considere sempre anos completos, e que um ano possui 365 dias. Ex: uma pessoa
com 19 anos possui 6935 dias de vida; veja um exemplo de saída: MARIA, VOCÊ JÁ VIVEU 6935
DIAS
'''
Nome=input("Insira aqui o seu nome: ")
Idade=int(input("Insira aqui o numero de anos completos vividos: "))
Dias=Idade*365
print(Nome,"você ja viveu",Dias,"dias.")