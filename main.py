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
            global nomeUsuario
            nomeUsuario = nome
            return 'loja.html'
    
@eel.expose    
def editarUsuario(nome='',senha='',novoNome='',novaSenha='',novoSaldo='',apagar=False):
    if nome == '' or senha == '':
        return 'Nome ou senha vazios'
    if len(nome) < 5 or len(senha) < 5:
        return 'Nome ou senha muito curtos'
    
    cursor.execute('SELECT * FROM usuarios')
    listaUsuarios = cursor.fetchall()

    usuarioEncontrado = None
    for usuario in listaUsuarios:#Não deixa criar usuários com mesmo nome
        if usuario[0] == nome:
            usuarioEncontrado = usuario

    if apagar:
        if usuarioEncontrado == None:
            return 'Usuário não encontrado'
        else:
            cursor.execute(f"DELETE FROM usuarios WHERE nome='{nome}'")
            return
        
    if novoNome or novaSenha or novoSaldo:#Tentando editar
        if usuarioEncontrado:
            novoNome = usuarioEncontrado[0] if novoNome == '' else novoNome
            novaSenha = usuarioEncontrado[1] if novaSenha == '' else novaSenha
            novoSaldo = usuarioEncontrado[2] if novoSaldo == '' else usuarioEncontrado[2] + float(novoSaldo)
            cursor.execute(f"UPDATE usuarios SET nome='{novoNome}', senha='{novaSenha}', saldo='{novoSaldo}' WHERE nome='{usuarioEncontrado[0]}'")
        else:
            return 'Usuário não encontrado'

    elif nome and senha:#Tentando criar usuário
        if usuarioEncontrado == None:
            cursor.execute(f"INSERT INTO usuarios (nome, senha, saldo) VALUES ('{nome}', '{senha}', 0)")
        else:
            return 'Usuário já existente'
        
@eel.expose
def pegarProdutos():
    cursor.execute('SELECT * FROM produtos')
    return cursor.fetchall()

@eel.expose
def adicionarAoCarrinho(produto:list):
    cursor.execute(f"INSERT INTO compras (comprador, produto, efetivada) VALUES ('{nomeUsuario}','{produto[0]}',False)")

@eel.expose
def pegarProdutosDoCarrinho():
    cursor.execute(f"SELECT * FROM compras WHERE comprador='{nomeUsuario}' AND efetivada=False")
    return cursor.fetchall()

''''
tabelas: usuários, produtos e compras
telas: login, loja, editar_usuario, carrinho
create: login
read: loja
update: editar_usuario
delete: editar_usuario
'''


eel.init('frontend')
eel.start('index.html')