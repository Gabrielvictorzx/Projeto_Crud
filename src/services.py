from conexão import *

def enviar_dados(nome, email, senha):
    criar_usuario(nome, email, senha)

def criar_usuario(nome, email, senha):
    if conn.is_connected():
        print('Banco conectado com sucesso!')

        cursor = conn.cursor()

        sql = 'INSERT INTO usuario (nome, email, senha) values (%s, %s, %s)'
        values = (nome, email, senha)

        cursor.execute(sql, values)
        conn.commit()
        print('Usuario cadastrado com sucesso!')
        conn.close()
        cursor.close()

    else:
        print('Falha ao conectar com o banco!')

def listar_usuario():
    if conn.is_connected():
        print('Banco de dados conectado com sucesso!!')

        cursor = conn.cursor()

        cursor.execute('select id, nome, email from usuario;')

        usuarios = cursor.fetchall()
        return usuarios
    else:
        print('Falha ao conectar com o banco de dados!')

    if __name__ == '__main__':
        listar_usuario()