import mysql.connector

###########################################################################################
#create
def Create():
    
    conexao = mysql.connector.connect(
        host='localhost',
        user='root_ikeda',
        password='123456',
        database='bdyoutube'
    )
    cursor = conexao.cursor()
    nomeproduto = "coca"
    valor = 2
    comando = f'INSERT INTO vendas( Produto, Valor) VALUES ( "{nomeproduto}" , {valor});'
    cursor.execute(comando)

    conexao.commit()

    cursor.close()
    conexao.close()
    return comando
###########################################################################################
#read
def Read():
    
    conexao = mysql.connector.connect(
        host='localhost',
        user='root_ikeda',
        password='123456',
        database='bdyoutube'
    )
    cursor = conexao.cursor()
    
    comando = f'SELECT * FROM vendas;'
    cursor.execute(comando)
    resultado = cursor.fetchall()
    print(resultado)
    cursor.close()
    conexao.close()
    return resultado
###########################################################################################
#update
def Update():
   
    conexao = mysql.connector.connect(
        host='localhost',
        user='root_ikeda',
        password='123456',
        database='bdyoutube'
    )
    cursor = conexao.cursor()
    nomeproduto = "coockies"
    valor = 2315
    comando = f'UPDATE bdyoutube.vendas SET Valor={valor} WHERE produto="{nomeproduto}";'
    cursor.execute(comando)

    conexao.commit()

    cursor.close()
    conexao.close()

###########################################################################################
#delete
def Delete():
    
    conexao = mysql.connector.connect(
        host='localhost',
        user='root_ikeda',
        password='123456',
        database='bdyoutube'
    )
    cursor = conexao.cursor()
    nomeproduto = "coockies"
    comando = f'delete from vendas WHERE produto="{nomeproduto}";'
    cursor.execute(comando)
    conexao.commit()
    cursor.close()
    conexao.close()

print(Create())
print(Read())