import eel
import psycopg2

bancoDeDados = psycopg2.connect(dbname='loja',user='postgres',password='pabd',host='localhost',port=5432)
bancoDeDados.autocommit = True
cursor = bancoDeDados.cursor()

@eel.expose
def login(nome,senha):
    cursor.execute('SELECT * FROM usuarios')
    listaUsuarios = cursor.fetchall()

    for usuario in listaUsuarios:
        if usuario[0] == nome and usuario[1] == senha:
            return 'loja.html'
    
@eel.expose
def criarConta(nome,senha):
    if nome == '' or senha == '':
        return 'Nome ou Senha vazios'
    if len(nome) < 5 or len(senha) < 5:
        return 'Nome ou Senha muito curtos'
    
    cursor.execute('SELECT * FROM usuarios')
    listaUsuarios = cursor.fetchall()

    for usuario in listaUsuarios:#Não deixa criar usuários com mesmo nome
        if usuario[0] == nome:
            return 'Usuário já existente'
    
    cursor.execute(f"INSERT INTO usuarios (nome, senha, saldo) VALUES ('{nome}', '{senha}', 0)")

eel.init('frontend')
eel.start('index.html')