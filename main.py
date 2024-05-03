from funcoes import adicionar_contato,visualizar_contatos,editar_contato,buscar_contato_indice,marcar_desmarcar_favorito,buscar_contatos_favoritos,apagar_contato, formatar_numero_telefone
from funcionalidades import func_adicionar_contato,func_visualizar_contatos

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
        func_adicionar_contato()
    elif escolha == 2:
        func_visualizar_contatos()
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
        telefone_atualizado = input(f"Digite o telefone para ser atualizado atualmente está '{formatar_numero_telefone(telefone)}', digite no formato DDNumero juntos por ex: 11999998888:")
        favorito_atualizado = input(f"Este contato atualmente {favorito} é favorito, ele deve ficar como Sim ou Não? (S/N):")

        favorito = False

        if(favorito_atualizado == "S"):
            favorito = True
        else:
            favorito = False

        contato = { "nome": nome_atualizado, "telefone": telefone_atualizado, "email": email_atualizado, "favorito": favorito }
        editar_contato(indice,contato)
    elif escolha == 4:
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
    elif escolha == 5:
        buscar_contatos_favoritos()
    elif escolha == 6:
        visualizar_contatos()
        indice = input("\n Digite o número do contato que deseja apagar: ")
        apagar_contato(indice)
    elif escolha == 7:
        break

print("Programa finalizado")