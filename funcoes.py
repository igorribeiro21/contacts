contatos = []

def adicionar_contato(contato):
    favorito = "Sim" if contato["favorito"] else "Não"

    contatos.append(contato)
    
    print("Contato adicionado com sucesso! Nome: %s, Telefone: %s, Email: %s, Favorito: %s" % (contato["nome"], contato["telefone"], contato["email"], favorito))
    return

def visualizar_contatos():
    print("\n Lista de contatos:")
    for i, contato in enumerate(contatos, start=1):
        favorito = "Sim" if contato["favorito"] else "Não"
        nome = contato["nome"]
        email = contato["email"]
        telefone = contato["telefone"]

        print(f"{i}. Nome: {nome}, Telefone: {telefone}, E-mail: {email}, Favorito: {favorito}")
    return

def editar_contato(indice, contato_atualizado):
    indice_tarefa_ajustado = int(indice) - 1
    if indice_tarefa_ajustado >= 0 and indice_tarefa_ajustado < len(contatos):
        contatos[indice_tarefa_ajustado] = contato_atualizado
        favorito = "Sim" if contatos[indice_tarefa_ajustado]["favorito"] else "Não"
        nome = contatos[indice_tarefa_ajustado]["nome"]
        email = contatos[indice_tarefa_ajustado]["email"]
        telefone = contatos[indice_tarefa_ajustado]["telefone"]

        print(f"Contato atualizado para Nome: {nome}, Telefone: {telefone}, E-mail: {email}, Favorito: {favorito}")
    else:
        print("Indice de tarefa inválido.")
    return

def buscar_contato_indice(indice):
    indice_tarefa_ajustado = int(indice) - 1
    contato = contatos[indice_tarefa_ajustado]

    return contato