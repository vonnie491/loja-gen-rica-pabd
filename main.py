import eel

@eel.expose
def dizerOi():
    print('oi')

eel.init('frontend')

eel.start('index.html')