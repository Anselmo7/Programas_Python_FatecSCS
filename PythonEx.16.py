#Anselmo Antunes Ribeiro
#Ex. 16
# Ler as notas de avaliação de um jogador sobre a 1ª e 2ª. fases de um Game e em seguida escrever uma mensagem informando 
#a média aritmética destas notas e uma mensagem informando “Experiência boa”, caso a média seja maior ou a 8.0 ou a mensagem “Experiência ruim” caso contrário.

Fase1 = float(input("Insira a nota da fase 1:"))
Fase2 = float(input("Insira a nota da fase 2:"))
media = (Fase1 + Fase2) / 2
if(media >= 8):
    print("Experiência Boa")
else:
    print("Experiência Ruim") 
print("Média das fases=", media)    
quit       