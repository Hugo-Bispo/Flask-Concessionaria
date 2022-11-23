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


def dao_to_view(placa):
    if "-" in placa:
        placa = placa.replace("-", "")

    result = carroDAO.select_carro(placa)
    placa = f"{result[0][0:3]}-{result[0][3:7]}"
    modelo = result[1]
    marca = result[2]
    cor = result[3]
    valor = result[4]
    situacao = yes_or_no(result[5])
    ar_condicionado = yes_or_no(result[6])
    ar_quente = yes_or_no(result[7])
    vidros_eletricos = yes_or_no(result[9])
    travas_eletricas = yes_or_no(result[10])
    direcao = result[8]
    if "m" in direcao:
        direcao = "Mecânica"
    elif "e" in direcao:
        direcao = "Elétrica"
    else:
        direcao = "Hidráulica" 

    result = {"Placa": placa,
		"Modelo": modelo,
		"Marca": marca,
		"Cor": cor,
		"Valor" : valor,
        "Disponivel" : situacao,
		"Ar-condicionado" : ar_condicionado,
		"Ar-quente" : ar_quente,
		"Direçao" : direcao,
		"Vidros Eletricos" : vidros_eletricos,
		"Travas Eletricas" : travas_eletricas,
	    }

    print(result)
    return result

def yes_or_no(registro):
    if registro == 1:
        registro = "Sim"
    else:
        registro = "Não"
    return registro

