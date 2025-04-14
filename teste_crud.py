import crud

# Teste: adicionando um contato
crud.adicionar_contato("Pablo Soares Lopes","21995369134","mpablosl@gmail.com")

# Teste: LIstando os contatos
contatos = crud.listar_contatos()

for c in contatos:
    print(c)