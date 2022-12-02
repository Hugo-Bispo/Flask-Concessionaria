from persistence import carroDAO
import locale

locale.setlocale(locale.LC_MONETARY, 'pt_BR.UTF-8')

# Implementar listas e Dicionario
def search_carro(placa):
    placa = str(placa)
    placa = placa.replace("-", "").upper()
    result = carroDAO.select_carro(placa)
    if result == None:
        return {"Placa": "Não Encontrada"}
    new_result = dao_to_view(result)
    dict_result = {"Placa": new_result[0],
        "Modelo": new_result[1],
        "Marca": new_result[2],
        "Cor": new_result[3],
        "Valor" : new_result[4],
        "Disponivel" : new_result[5],
        "Ar-condicionado" : new_result[6],
        "Ar-quente" : new_result[7],
        "Direçao" : new_result[8],
        "Vidros Eletricos" : new_result[9],
        "Travas Eletricas" : new_result[10],
    }
    return dict_result

def search_all():
    result = carroDAO.select_all()
    new_result = []
    for carro in result:
        new_result.append(dao_to_view(carro))
    print(new_result)
    return new_result

def view_to_dao(registros):
    if "-" in registros["placa"]:
        placa = str(registros["placa"])
        placa = placa.replace("-", "")
        registros["placa"] = placa.upper()

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


def dao_to_view(result):    
    placa = f"{result[0][0:3]}-{result[0][3:7]}"
    modelo = result[1]
    marca = result[2]
    cor = result[3]
    valor = locale.currency(result[4], grouping=True)
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
    elif "h" in direcao:
        direcao = "Hidráulica" 
    new_result = [placa, modelo, marca, cor, valor, situacao, ar_condicionado, ar_quente, direcao, vidros_eletricos, travas_eletricas]

    return new_result

def update(registros):
    
    if "-" in registros["placa"]:
        placa = str(registros["placa"])
        placa = placa.replace("-", "")
        registros["placa"] = placa.upper()

    if "R$" in registros["valor"]:
        valor = str(registros["valor"])
        valor = valor.replace("R$ ","")
        valor = valor.replace(".","")
        valor = valor[:-3]
        registros["valor"] = valor

    if registros["direcao"] == "Elétrica":
        registros["direcao"] = "e"
    elif registros["direcao"] == "Mecânica":
        registros["direcao"] = "m"
    else:
        registros["direcao"] = "h"

    if registros["ar_condicionado"] == "Sim":
        registros["ar_condicionado"] = 1
    else:
       registros["ar_condicionado"] = 0

    if registros["ar_quente"] == "Sim":
        registros["ar_quente"] = 1
    else:
       registros["ar_quente"] = 0

    if registros["vidros_eletricos"] == "Sim":
        registros["vidros_eletricos"] = 1
    else:
       registros["vidros_eletricos"] = 0

    if registros["travas_eletricas"] == "Sim":
        registros["travas_eletricas"] = 1
    else:
       registros["travas_eletricas"] = 0
    print(registros)
    carroDAO.update_carro(registros)

def delete(registros):
    if "-" in registros["placa"]:
        placa = str(registros["placa"])
        placa = placa.replace("-", "")
        registros["placa"] = placa.upper()

    carroDAO.delete_carro(registros)

def yes_or_no(registro):
    if registro == 1:
        registro = "Sim"
    else:
        registro = "Não"
    return registro

