from persistence import carroDAO

def view_to_dao(registros):
    if "-" in registros["placa"]:
        placa = str(registros["placa"])
        placa = placa.replace("-", "")
        registros["placa"] = placa

    if registros["ar_condicionado"] == "on":
        registros["ar_condicionado"] = True
    else:
       registros["ar_condicionado"] = False

    if registros["ar_quente"] == "on":
        registros["ar_quente"] = True
    else:
       registros["ar_quente"] = False

    if registros["vidros_eletricos"] == "on":
        registros["vidros_eletricos"] = True
    else:
       registros["vidros_eletricos"] = False

    if registros["travas_eletricas"] == "on":
        registros["travas_eletricas"] = True
    else:
       registros["travas_eletricas"] = False
    print(registros)
    carroDAO.insert_carro(registros)


def dao_to_view():
    print(carroDAO.select_carro())
