import sqlite3 as sql

# Conecta(ou cria) o banco de dados
conn = sql.connect("contatos.db")

# Cria um cursor
cursor = conn.cursor()

# Criação da tabela
cursor.execute('''
CREATE TABLE IF NOT EXISTS contatos(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    telefone TEXT,
    email TEXT)
''')

# Salva as alterações e fecha a conexão

conn.commit()
conn.close()
print("Tabela criada com sucesso!")