contatos = []

def adicionar_contato(contato):
    favorito = "Sim" if contato["favorito"] else "Não"

    contatos.append(contato)
    
    print("Contato adicionado com sucesso! Nome: %s, Telefone: %s, Email: %s, Favorito: %s" % (contato["nome"], formatar_numero_telefone(contato["telefone"]), contato["email"], favorito))
    return

def visualizar_contatos():
    print("\n Lista de contatos:")
    for i, contato in enumerate(contatos, start=1):
        favorito = "Sim" if contato["favorito"] else "Não"
        nome = contato["nome"]
        email = contato["email"]
        telefone = formatar_numero_telefone(contato["telefone"])

        print(f"{i}. Nome: {nome}, Telefone: {telefone}, E-mail: {email}, Favorito: {favorito}")
    return

def editar_contato(indice, contato_atualizado):
    indice_contato_ajustado = int(indice) - 1
    if indice_contato_ajustado >= 0 and indice_contato_ajustado < len(contatos):
        contatos[indice_contato_ajustado] = contato_atualizado
        favorito = "Sim" if contatos[indice_contato_ajustado]["favorito"] else "Não"
        nome = contatos[indice_contato_ajustado]["nome"]
        email = contatos[indice_contato_ajustado]["email"]
        telefone = formatar_numero_telefone(contatos[indice_contato_ajustado]["telefone"])

        print(f"Contato atualizado para Nome: {nome}, Telefone: {telefone}, E-mail: {email}, Favorito: {favorito}")
    else:
        print("Indice de tarefa inválido.")
    return

def buscar_contato_indice(indice):
    indice_contato_ajustado = int(indice) - 1
    contato = contatos[indice_contato_ajustado]

    return contato

def marcar_desmarcar_favorito(indice, status):
    indice_contato_ajustado = int(indice) - 1

    contatos[indice_contato_ajustado]["favorito"] = status

    mensagem = ""

    if(status):
        mensagem = f"Contato {indice} alterado para favorito!"
    else:
        mensagem = f"Contato {indice} alterado para não favorito!"

    print(f"\n{mensagem}")
    return

def buscar_contatos_favoritos():
    contatos_favoritos = []
    for indice,contato in enumerate(contatos, start=1):
        if(contato["favorito"]):
            contato_adicionar = {
                "indice_original": indice,
                "nome": contato["nome"],
                "telefone": contato["telefone"],
                "email": contato["email"],
                "favorito": contato["favorito"]
            }
            contatos_favoritos.append(contato_adicionar)
    
    print("\n Lista de contatos favoritados:")

    for contato in contatos_favoritos:
        indice_original = contato["indice_original"]
        favorito = "Sim" if contato["favorito"] else "Não"
        nome = contato["nome"]
        email = contato["email"]
        telefone = formatar_numero_telefone(contato["telefone"])

        print(f"{indice_original}. Nome: {nome}, Telefone: {telefone}, E-mail: {email}, Favorito: {favorito}")
    
    return

def apagar_contato(indice):
    contato = buscar_contato_indice(indice)

    contatos.remove(contato)

    print("\n Contato removido com sucesso!")
    return

def formatar_numero_telefone(numero):
    return "({}){}-{}{}".format(numero[:2], numero[2:7], numero[7:9], numero[9:])
