#Anselmo Antunes Ribeiro
#Ex. 15
# Faça um programa que solicite ao usuário os dados necessários para calcular a área de um quadrado.
# Mostrar em seguida o valor correspondente ao dobro da área calculada caso todos os dados fornecidos sejam maiores que zero.

lado = float(input("Insira a medida de um dos lados:"))
area =  lado * 2
print("Área do quadrado=", area)
if(lado > 0):
    dobro = area * 2
print("Área do quadrado dobrada=", dobro)
quit