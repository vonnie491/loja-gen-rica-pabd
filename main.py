import eel
import psycopg2

bancoDeDados = psycopg2.connect(dbname='lolja',user='postgres',password='pabd',host='localhost',port=5432)
cursor = bancoDeDados.cursor()

@eel.expose
def login(nome,senha):
    cursor.execute('SELECT * FROM usuarios')
    listaUsuarios = cursor.fetchall()

    for usuario in listaUsuarios:
        if usuario.nome == nome and usuario.senha == senha:
            return 'loja.html'
    return '#'
    
def conta(nome, senha):
	cursor.execute('SELECT * FROM usuarios')
    listaUsuarios = cursor.fetchall()

    for usuario in listaUsuarios:
        if usuario.nome == nome and usuario.senha == senha:
        	return '#'
        else:
        	cursor.execute("INSERT INTO conta (nome, senha) VALUES (%s, %s)"(usuario.nome, usuario.senha))

eel.init('frontend')

eel.start('index.html')