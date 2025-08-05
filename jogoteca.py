from flask import Flask, render_template, request, redirect


class Jogo:
    def __init__(self, nome, categoria, console):
        self.nome = nome
        self.categoria = categoria
        self.console = console

jogo1 = Jogo('Tetris', 'Puzzle', 'Atari')
jogo2 = Jogo('God of War', 'Rack n Slash', 'PS2')
jogo3 = Jogo('Mortal Kombat', 'Luta', 'PS2')
jogo4 = Jogo('Pokémon', 'RPG', 'Nintendo DS')

listaJogos = [jogo1, jogo2, jogo3, jogo4]


app = Flask(__name__)


@app.route("/")
def index():
    return render_template('lista.html', titulo='Jogos', jogos=listaJogos)


@app.route("/novo")
def novo():
    return render_template('novo.html', titulo='Novo Jogo')


@app.route("/criar", methods=['GET', 'POST'])
def criar():
    nome = request.form['nome']
    categoria = request.form['categoria']
    console = request.form['console']
    jogo = Jogo(nome, categoria, console)

    listaJogos.append(jogo)

    # Redireciona para a página em questão
    return redirect('/')


app.run(debug=True)
#if __name__ == "__main__":
#    app.run(debug=True)
