#Anselmo Antunes Ribeiro
#Ex. 12
# Em um jogo de Fazenda existe a opção de compras de frutas para o jogador manter em sua despensa.
#No empório virtual as frutas são vendidas pelos seguintes preços: Maçã: R$ 2,30 por Kg, Melancia: R$ 4,00 a unidade e Laranja R$ 0,30 a unidade.
#Escreva um programa para ler a quantidade de maças, laranjas e melancias compradas, calcular e mostrar na tela o valor a pagar.

#Preço por Kg ou unid.

maca = 2.30
melancia = 4.00
laranja = 0.30

kgmaca = float(input("insira o peso das maçãs em kg:"))
precomaca = kgmaca * maca
print("Valor =", precomaca)

unidmelancia = float(input("insira a quantidade de melancias:"))
precomelancia = unidmelancia * 4.00
print("Valor =", precomelancia)

unidlaranja = float(input("insira a quantidade de laranjas:"))
precolaranja = unidlaranja * 0.30
print("Valor =", precolaranja)

total = precomaca + precomelancia + precolaranja
print("Valor total=", total)
quit