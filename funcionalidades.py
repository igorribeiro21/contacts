from funcoes import adicionar_contato,visualizar_contatos,editar_contato,buscar_contato_indice,marcar_desmarcar_favorito,buscar_contatos_favoritos,apagar_contato, formatar_numero_telefone

def func_adicionar_contato():
    nome_contato = input("Digite o nome do contato: ")
    email_contato = input("Digite o e-mail do contato: ")
    telefone_contato = input("Digite o telefone do contato no formato 11999998888: ")
    favoritar_contato = input("Este contato deve ser adicionado as favoritos? (S/N): ")
    favorito = False

    if(favoritar_contato == "S"):
        favorito = True
    else:
        favorito = False
    
    contato = { "nome": nome_contato, "telefone": telefone_contato, "email": email_contato, "favorito": favorito }
    adicionar_contato(contato)
    return

def func_visualizar_contatos():
    visualizar_contatos()
    return

def func_editar_contato():
    visualizar_contatos()
    indice = int(input("\n Digite o contato que deseja atualizar: "))
        
    contato = buscar_contato_indice(indice)

    nome = contato["nome"]
    email = contato["email"]
    telefone = contato["telefone"]
    favorito = "Sim" if contato["favorito"] else "Não"
    nome_atualizado = input(f"Digite o nome para ser atualizado atualmente está '{nome}':")
    email_atualizado = input(f"Digite o e-mail para ser atualizado atualmente está '{email}':")
    telefone_atualizado = input(f"Digite o telefone para ser atualizado atualmente está '{formatar_numero_telefone(telefone)}', digite no formato DDNumero juntos por ex: 11999998888:")
    favorito_atualizado = input(f"Este contato atualmente {favorito} é favorito, ele deve ficar como Sim ou Não? (S/N):")

    favorito = False

    if(favorito_atualizado == "S"):
        favorito = True
    else:
        favorito = False

    contato = { "nome": nome_atualizado, "telefone": telefone_atualizado, "email": email_atualizado, "favorito": favorito }
    editar_contato(indice,contato)
    return

def func_marcar_desmarcar_favorito():
    status = False
    visualizar_contatos()
    indice = input("\n Digite o número do contato que deseja alterar o status de favorito: ")

    contato = buscar_contato_indice(indice)
    mensagem = ""

    if(contato["favorito"]):
        mensagem = "Deseja alterar esse contato para não favorito? (S/N)"
    else:
        mensagem = "Deseja alterar esse contato para favorito? (S/N)"

    resposta_marcar_desmarcar = input(mensagem)

    marcar_desmarcar = True if resposta_marcar_desmarcar == "S" else False

    if(marcar_desmarcar):
        status =  False if contato["favorito"] else True
    else:
        status = contato["favorito"]
        
    marcar_desmarcar_favorito(indice, status)
    return

def func_buscar_contatos_favoritos():
    buscar_contatos_favoritos()
    return

def func_apagar_contato():
    visualizar_contatos()
    indice = input("\n Digite o número do contato que deseja apagar: ")
    apagar_contato(indice)
    return