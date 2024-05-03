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