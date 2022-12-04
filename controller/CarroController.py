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
        "Ano" :new_result[6],
        "Disponivel" : new_result[5],
        "Ar-condicionado" : new_result[7],
        "Ar-quente" : new_result[8],
        "Direçao" : new_result[9],
        "Vidros Eletricos" : new_result[10],
        "Travas Eletricas" : new_result[11],
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
    
    registros["ar_condicionado"] = one_or_zero(registros["ar_condicionado"])
    registros["ar_quente"] = one_or_zero(registros["ar_quente"])
    registros["vidros_eletricos"] = one_or_zero(registros["vidros_eletricos"])
    registros["travas_eletricas"] = one_or_zero(registros["travas_eletricas"])

    print(registros)
    carroDAO.insert_carro(registros)


def dao_to_view(result):
    print("result" + str(result))
    placa = f"{result[0][0:3]}-{result[0][3:7]}"
    modelo = result[1]
    marca = result[2]
    cor = result[3]
    valor = locale.currency(result[4], grouping=True)
    ano = str(result[5])
    situacao = yes_or_no(result[6])
    ar_condicionado = yes_or_no(result[7])
    ar_quente = yes_or_no(result[8])
    vidros_eletricos = yes_or_no(result[10])
    travas_eletricas = yes_or_no(result[11])
    direcao = result[9]
    if "m" in direcao:
        direcao = "Mecânica"
    elif "e" in direcao:
        direcao = "Elétrica"
    elif "h" in direcao:
        direcao = "Hidráulica" 
    new_result = [placa, modelo, marca, cor, valor, situacao, ano, ar_condicionado, ar_quente, direcao, vidros_eletricos, travas_eletricas]

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

def one_or_zero(registro):
    if registro == "on":
        registro = 1
    else:
        registro = 0
    return registro

def yes_or_no(registro):
    if registro == 1:
        registro = "Sim"
    else:
        registro = "Não"
    return registro

