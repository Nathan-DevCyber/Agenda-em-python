
AGENDA = {}

AGENDA["guilherme"] = {
    "telefone" : "99999657",
    "email": "guilherme@email.com",
    "endereco" : "Av. 1",
}
AGENDA["maria"] = {
    "telefone" : "99998437",
    "email": "maria@email.com",
    "endereco" : "Av. 2",
}


def mostrar_contatos():
    for contato in AGENDA:
        buscar_contato(contato)
        print("====================================")




def buscar_contato(contato):
    print("Nome: ", contato)
    print("Telefone: ", AGENDA[contato]["telefone"])
    print("Email: ", AGENDA[contato]["email"])
    print("Endereço: ", AGENDA[contato]["endereco"])


def incluir_contato(contato, telefone, email, endereco):
    AGENDA[contato] = {
        "telefone" : telefone,
        "email": email,
        "endereco": endereco,
    }
    print(">>>>>>>>>>>>> Contato {} adicionado/editado com sucesso".format(contato))


def excluir_contato(contato):
    AGENDA.pop(contato)
    print(">>>>>> Contato {} excluido com sucesso".format(contato))

buscar_contato("maria")
mostrar_contatos()
incluir_contato("joao", "419999999", "joao@gmail.com", "av. 3")
mostrar_contatos()