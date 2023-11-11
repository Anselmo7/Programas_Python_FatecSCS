# Dados para validação do Login/Senha
loginok ="afteste"
senhaok ="@123"
#
vlogin = input("Login:")
vsenha = input("Senha:")
if (vlogin == loginok and vsenha == senhaok):
    print("Login Correto")   
    print("Senha Correta")
else:    
    (vlogin == loginok and vsenha != senhaok)
    print("Acesso Negado")   
quit()
