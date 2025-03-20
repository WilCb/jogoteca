from flask import Flask, render_template

class Jogo:
    def __init__(self, nome, categoria, console):
        self.nome = nome
        self.categoria = categoria
        self.console = console

app = Flask(__name__)

@app.route("/inicio")
def ola():
    jogo1 = Jogo('Tetris', 'Puzze', 'Atari')
    jogo2 = Jogo('God of war', 'Rack n Slash', 'PS2')
    jogo3 = Jogo('League of Legends', 'MOBA', 'PC')
    lista = [jogo1, jogo2, jogo3]

    return render_template('lista.html', titulo='Jogos', jogos=lista)

@app.route("/cadastrar", methods=["POST"])
def cadastrar():
    pass


if __name__ == '__main__':
    app.run(debug=True)