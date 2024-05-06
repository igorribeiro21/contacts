from funcionalidades import func_adicionar_contato,func_visualizar_contatos,func_editar_contato,func_marcar_desmarcar_favorito,func_buscar_contatos_favoritos,func_apagar_contato

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
        func_editar_contato()
    elif escolha == 4:
        func_marcar_desmarcar_favorito()
    elif escolha == 5:
        func_buscar_contatos_favoritos()
    elif escolha == 6:
        func_apagar_contato()
    elif escolha == 7:
        break

print("Programa finalizado")