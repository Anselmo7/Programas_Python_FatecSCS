import sqlite3 #Biblioteca do sqlite

conn = sqlite3.connect("../SQLite/Santa Luzia.db")
cursor = conn.cursor()

vcodigo = input("Código:")
cursor.execute("select count(*), nmcurso, vlmensalidade from curso where codigo = " + vcodigo)
rs = cursor.fetchone()
if rs[0] > 0:
    print ("Curso:", rs[1])
    print ("Mensalidade:", rs[2])
    vconfirma = input("Confirma a exclusão deste curso? S/N)")
    print ("Código já cadastrado")
else:
    vnmcurso = input("Curso:")
    vvlmensalidade = input("Valor mensal:")
    vconfirma = input("Deseja cadastrar? (S/N)")

    if vconfirma == "S":
        #Enviar instruções SQL para ser executada
        conn.execute("insert into curso values(?, ?, ? )", (vcodigo, vnmcurso, vvlmensalidade))
        conn.commit()

    vcondicao = input("Deseja inserir mais informações?(S/N)):")
    if vcondicao.upper() != 'S':
        print("Informações cadastradas com sucesso")  
     
#Fechar conexão
conn.close
quit()

