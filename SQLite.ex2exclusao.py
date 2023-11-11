#Código para exclusão de cursos na tabela do SQLite.

import sqlite3 #Biblioteca do sqlite

conn = sqlite3.connect("../SQLite/Santa Luzia.db")
cursor = conn.cursor()

vcodigo = input("Código:")
cursor.execute("select count(*), nmcurso, vlmensalidade from curso where codigo = " + vcodigo)
rs = cursor.fetchone()
if rs[0] > 0:
    print ("Código já cadastrado")
    print ("Curso:", rs[1])
    print ("Mensalidade:", rs[2])
    vconfirma = input("Confirma a exclusão deste curso? S/N)")
    if vconfirma.upper():

    #Enviar instruções SQL para ser executada
        conn.execute("Delete from curso Where codigo = " + vcodigo)
        conn.commit()

    vcondicao = input("Deseja inserir mais informações?(S/N)):")
    if vcondicao.upper() != 'S':
        print("Informações cadastradas com sucesso")  
     
#Fechar conexão
conn.close
quit() 