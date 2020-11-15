import mysql.connector

conexao = mysql.connector.connect(host='localhost',database='University',user='root',password='root2020')

if conexao.is_connected():
    db_info = conexao.get_server_info()
    print("conectado ao servidor mysql", db_info)
    cursor = conexao.cursor()
    cursor.execute("select database();")
    linha = cursor.fetchone()
    print("Conectado ao ", linha)

if conexao.is_connected():
    cursor.close()
    conexao.close()
    print("Conexão Encerrada")