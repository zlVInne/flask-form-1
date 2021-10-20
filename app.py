from flask import Flask, render_template, url_for, redirect, request
app = Flask(__name__)

lista = ['Tarefa 1', 'Tarefa 2', 'Tarefa 3']
# Como realizar o deploy no Heroku
# Como conectar com o banco de dados.

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html', tarefas=lista)

@app.route('/create', methods=['GET'])
def create():
    return render_template('create.html')

@app.route('/save', methods=['POST'])
def save():
    lista.append(request.form['tarefa'])
    return redirect('https://5000-rose-antlion-6a1ppvyr.ws-us17.gitpod.io/')

if __name__ == '__main__':
    app.run(debug=True)
