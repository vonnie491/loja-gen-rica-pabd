import eel

@eel.expose
def login(usuario,senha):
    print(usuario)
    print(senha)

eel.init('frontend')

eel.start('index.html')