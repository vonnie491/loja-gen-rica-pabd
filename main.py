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


eel.init('frontend')

eel.start('index.html')