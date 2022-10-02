'''
10. Construa um algoritmo para calcular a distância entre dois pontos do plano cartesiano. Cada
ponto é um par ordenado (x,y).
'''

valor={"ponto1":[],"ponto2":[]}   

for a in range (2):
    if (a==0):
        print("Insira a posição do primeiro ponto.")
        x=int(input("Insira o valor de x: "))
        y=int(input("Insira o valor de y: "))
        valor["ponto1"].append(x)
        valor["ponto1"].append(y)
    if (a==1):
        print("Insira a posição do segundo ponto.")
        x=int(input("Insira o valor de x: "))
        y=int(input("Insira o valor de y: "))
        valor["ponto2"].append(x)
        valor["ponto2"].append(y)

dist=((valor["ponto2"][0]-valor["ponto1"][0])**2+(valor["ponto2"][1]-valor["ponto1"][1])**2)**0.5
print("Distancia: ",dist)