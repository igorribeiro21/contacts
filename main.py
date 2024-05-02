from funcoes import adicionar_contato,visualizar_contatos,editar_contato,buscar_contato_indice

while True:
    print("\n Menu da lista de opções:")
    print("1. Adicionar contato")
    print("2. Visualizar contatos")
    print("3. Editar contato")
    print("4. Marcar/desmarcar contato como favorito")
    print("5. Ver lista de favoritos")
    print("6. Apagar contato")
    print("7. Sair")

    escolha = int(input("Digite a opção que deseja escolher: "))

    if escolha == 1:
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
    elif escolha == 2:
        visualizar_contatos()
    elif escolha == 3:
        visualizar_contatos()
        indice = int(input("\n Digite o contato que deseja atualizar: "))
        
        contato = buscar_contato_indice(indice)

        nome = contato["nome"]
        email = contato["email"]
        telefone = contato["telefone"]
        favorito = "Sim" if contato["favorito"] else "Não"
        nome_atualizado = input(f"Digite o nome para ser atualizado atualmente está '{nome}':")
        email_atualizado = input(f"Digite o e-mail para ser atualizado atualmente está '{email}':")
        telefone_atualizado = input(f"Digite o telefone para ser atualizado atualmente está '{telefone}', digite no formato 11999998888:")
        favorito_atualizado = input(f"Este contato atualmente {favorito} é favorito, ele deve ficar como Sim ou Não? (S/N):")

        favorito = False

        if(favorito_atualizado == "S"):
            favorito = True
        else:
            favorito = False

        contato = { "nome": nome_atualizado, "telefone": telefone_atualizado, "email": email_atualizado, "favorito": favorito }
        editar_contato(indice,contato)
    elif escolha == 6:
        break

print("Programa finalizado")