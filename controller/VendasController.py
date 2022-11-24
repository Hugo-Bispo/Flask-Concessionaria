from persistence import vendasDAO


def view_to_dao(registros):
    if "-" in registros["placa"]:
        placa = str(registros["placa"])
        placa = placa.replace("-", "")
        registros["placa"] = placa

    print(registros)
    vendasDAO.insert_venda(registros)


def dao_to_view(placa):
    pass
