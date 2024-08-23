def adicionar_contato(contatos):
    nome = input("\nDigite o nome do contato: ")
    telefone = input("\nDigite o telefone do contato: ")
    email = input("\nDigite o email do contato: ")
    favorito = False
    contatos.append([nome, telefone, email, favorito])
    print("\nContato adicionado com sucesso!")

def listar_contatos(contatos):
    print("\nLista de contatos")
    for indice, contato in enumerate(contatos, start=1):
        print(f"{indice} - Nome: {contato[0]}, Telefone: {contato[1]}, Email: {contato[2]}")
        if contato[3]:
            print("\nFavorito: Sim")
        else:
            print("\nFavorito: Não")

def editar_contato(contatos):
    listar_contatos(contatos)
    indice_contato = int(input("\nDigite o número do contato que deseja editar: ")) - 1
    contato = contatos[indice_contato]
    print("\n1 - Editar nome")
    print("\n2 - Editar telefone")
    print("\n3 - Editar email")
    print("\n4 - Sair da edição")
    escolha = input("\nDigite a opção desejada: ")
    if escolha == "1":
        novo_nome = input("\nDigite o novo nome: ")
        contato[0] = novo_nome
    elif escolha == "2":
        novo_telefone = input("\nDigite o novo telefone: ")
        contato[1] = novo_telefone
    elif escolha == "3":
        novo_email = input("\nDigite o novo email: ")
        contato[2] = novo_email
    elif escolha == "4":
        print("\nSaindo da edição...")

def marcar_desmarcar_favorito(contatos):
    listar_contatos(contatos)
    indice_contato = int(input("\nDigite o número do contato que deseja marcar/desmarcar como favorito: ")) - 1
    contato = contatos[indice_contato]
    if contato[3]:
        contato[3] = False
        print("\nContato desmarcado como favorito!")
    else:
        contato[3] = True
        print("\nContato marcado como favorito!")

def listar_contatos_favoritos(contatos):
    print("\nLista de contatos favoritos")
    for indice, contato in enumerate(contatos, start=1):
        if contato[3]:
            print(f"{indice} - Nome: {contato[0]}, Telefone: {contato[1]}, Email: {contato[2]}")

def excluir_contato(contatos):
    listar_contatos(contatos)
    indice_contato = int(input("\nDigite o número do contato que deseja excluir: ")) - 1
    contato = contatos[indice_contato]
    contatos.remove(contato)
    print("\nContato excluído com sucesso!")

contatos = []
while True:
    print("\nAgenda de contatos")
    print("\n1 - Adicionar contato")
    print("\n2 - Listar contatos")
    print("\n3 - Editar contato")
    print("\n4 - Marcar/Desmarcar contato dos favoritos")
    print("\n5 - Ver lista de contatos favoritos")
    print("\n6 - Excluir contato")
    print("\n7 - Sair da agenda")

    escolha = input("\nDigite a opção desejada: ")

    if escolha == "1":
        adicionar_contato(contatos)

    elif escolha == "2":
        listar_contatos(contatos)

    elif escolha == "3":
        editar_contato(contatos)

    elif escolha == "4":
        marcar_desmarcar_favorito(contatos)

    elif escolha == "5":
        listar_contatos_favoritos(contatos)
    
    elif escolha == "6":
        excluir_contato(contatos)

    elif escolha == "7":
        print("\nSaindo da agenda...")
        break