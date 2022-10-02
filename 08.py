'''
8. Faça um algoritmo para ler três notas de um aluno em uma disciplina e imprimir a sua média
ponderada (as notas tem pesos respectivos de 1, 2 e 3).
'''

av1=float(input("Insira a nota da primeira avaliação: "))
av2=float(input("Insira a nota da segunda avaliação: "))
av3=float(input("Insira a nota da terceira avaliação: "))

media=((av1*1)+(av2*2)+(av3*3))/6

print("Media do aluno: ",media)