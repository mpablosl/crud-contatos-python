from flask import Flask, render_template, request, redirect
from crud import adicionar_contato, listar_contatos, deletar_contato, editar_contato, obter_contato, atualizar_contatos

app = Flask(__name__)

# Página inicial - lista os contatos
@app.route('/')
def index():
    contatos = listar_contatos()
    return render_template('index.html', contatos=contatos)

# Rota para adicioanr novo contato
@app.route('/adicionar', methods=['POST'])
def adicionar():
    nome = request.form['nome']
    telefone = request.form['telefone']
    email = request.form['email']
    adicionar_contato(nome,telefone,email)
    return redirect('/')

# Rota para deletar um contato
@app.route('/deletar/<int:id>')
def deletar(id):
    deletar_contato(id)
    return redirect('/')


# Rota para editar um contato
@app.route('/editar/<int:id>', methods=['GET', 'POST'])
def editar(id):
    if request.method == 'POST':
        nome = request.form['nome']
        telefone = request.form['telefone']
        email = request.form['email']
        editar_contato(id, nome, telefone, email)
        return redirect('/')
    else:
        contato = obter_contato(id)
        return render_template('editar.html', contato=contato)

if __name__ == '__main__':
    app.run(debug=True)