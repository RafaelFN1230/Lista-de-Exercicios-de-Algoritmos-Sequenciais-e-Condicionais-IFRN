'''
9. Uma fábrica de camisetas produz os tamanhos pequeno, médio e grande, cada uma sendo
vendida respectivamente por 10, 12 e 15 reais. Construa um algoritmo em que o usuário forneça a
quantidade de camisetas pequenas, médias e grandes referentes a uma venda, e a máquina
informe quanto será o valor arrecadado.
'''
print("Temos tamanhos pequeno, médio e grande")
print("Valor respectivamente: 10, 12 e 15 reais.")
p=int(input("Insira o numeor de camisa P: "))
m=int(input("Insira o numeor de camisa M: "))
g=int(input("Insira o numeor de camisa G: "))

val_p=p*10
val_m=m*12
val_g=g*15
total=val_p+val_m+val_g

print("Total: ",total)