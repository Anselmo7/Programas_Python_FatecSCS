from hashlib import sha256
senOK = '78ffc2e25bc4e2ef60c0532acd15ece8c7a66e8ef2ad5a3b09227e98887e7cf6'       
nro = 0 
while nro < 3: 
        nro = nro + 1 
        login = (input('login: ')) 
        senha = (input('senha: '))
        
        senha_hash = sha256(senha.encode()).hexdigest()

        if login == 'ABC' and senha_hash == senOK:
            print ('Acesso permitido') 
            break 
        else: 
              print ('Acesso negado')
        if nro == 2:
            print("Atenção! Última tentativa!")
        if nro == 3: 
              print ('Usuário bloqueado') 
quit()   

