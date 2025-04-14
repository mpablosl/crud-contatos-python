import sqlite3 as sql

# Função para adicionar um contato
def adicionar_contato(nome, telefone, email):
    conn = sql.connect("contatos.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO contatos (nome, telefone, email) VALUES (?,?,?)", (nome,telefone,email))
    conn.commit()
    conn.close()

# Função para listar todos os contatos
def listar_contatos():
    conn = sql.connect("contatos.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM contatos")
    contatos = cursor.fetchall()
    conn.close()
    return contatos

# Função para atualizar um contato existente
def atualizar_contatos(id, nome, telefone, email):
    conn = sql.connect("contatos.db")
    cursor = conn.cursor()
    cursor.execute("UPDATE contatos SET nome = ?, telefone = ?, email = ? WHERE id = ?",(nome, telefone, email, id))
    conn.commit()
    conn.close()

# Função para deletar um contato
def deletar_contato(id):
    conn = sql.connect("contatos.db")
    cursor = conn.cursor()
    cursor.execute("DELETE FROM contatos where id = ?",(id,))    
    conn.commit()
    conn.close()

def obter_contato(id):
    conn = sql.connect('contatos.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM contatos WHERE id = ?",(id,))
    contato = cursor.fetchone()
    conn.close()
    return contato

def editar_contato(id, nome, telefone, email):
    conn = sql.connect('contatos.db')
    cursor = conn.cursor()
    cursor.execute('UPDATE contatos SET nome = ?, telefone = ?, email = ? WHERE id = ?', (nome, telefone, email, id))
    conn.commit()
    conn.close()