'''
3. A padaria Hotpão vende uma certa quantidade de pães franceses e uma quantidade de broas a
cada dia. Cada pãozinho custa R$ 0,12 e a broa custa R$ 1,50. Ao final do dia, o dono quer saber
quanto arrecadou com a venda dos pães e broas (juntos), e quanto deve guardar numa conta de
poupança (10% do total arrecadado). Você foi contratado para fazer os cálculos para o dono. Com
base nestes fatos, faça um algoritmo para ler as quantidades de pães e de broas, e depois calcular
os dados solicitados.
'''

print("Olá, bem vindo(a) a padaria Hotpão.")
print("Por favor insira a quantidade de pães e broas vendidas.")
Pao_frances=int(input("Insira aqui a quantidade de pães franceses: "))
Broa=int(input("Insira aqui a quantidade de broas: "))
Total=Pao_frances*0.12+Broa*1.15
print("Este é o total do dia",round(Total,2))
Poupanca=Total*0.10
print("Esta é a quantia que deve ser guardado na poupança:",round(Poupanca,2))