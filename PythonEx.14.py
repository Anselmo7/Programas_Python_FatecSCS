#Anselmo Antunes Ribeiro
#Ex. 14
# Faça um programa para ler uma medida em metros. Mostrar o equivalente em centímetros somente caso a medida seja menor que 100

medida = float(input("Insira a medida:"))
if(medida < 100):
    conversao = medida * 100
    print("Medida em cm =", conversao)
quit    

