import mysql.connector

###########################################################################################
#create
def Create():
    
    conexao, cursor = Connection_DB()

    
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
    
    conexao, cursor = Connection_DB()
    
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
   
    conexao, cursor = Connection_DB()
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
    
    conexao, cursor = Connection_DB()
    nomeproduto = "coockies"
    comando = f'delete from vendas WHERE produto="{nomeproduto}";'
    cursor.execute(comando)
    conexao.commit()
    cursor.close()
    conexao.close()

def Connection_DB():
    conexao = mysql.connector.connect(
        host='localhost',
        user='root_ikeda',
        password='123456',
        database='bdyoutube'
    )
    cursor = conexao.cursor()
    return conexao,cursor

print(Delete())
print(Update())
print(Create())
print(Read())