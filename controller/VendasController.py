from persistence import vendasDAO
import locale, datetime

locale.setlocale(locale.LC_MONETARY, 'pt_BR.UTF-8')

def search_all():
    result = vendasDAO.select_all()
    new_result = []
    for venda in result:
        new_result.append(dao_to_view(venda))
    return new_result

def view_to_dao(registros):
    if "-" in registros["placa"]:
        placa = str(registros["placa"])
        placa = placa.replace("-", "")
        registros["placa"] = placa
    vendasDAO.insert_venda(registros)


def dao_to_view(result):
    placa = f"{result[0][0:3]}-{result[0][3:7]}"
    modelo = result[1]
    valor = locale.currency(result[2], grouping=True)
    data = result[3].strftime("%d/%m/%Y")
    new_result = [placa, modelo, valor, data]
    return new_result

