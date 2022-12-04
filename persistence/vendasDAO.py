import mysql.connector
from controller.database_connection import mysql_execute_command, mysql_execute_select, mysql_execute_select_all


def insert_venda(registros):
    placa = registros["placa"]
    data_venda = registros["data_venda"]
    command = (f" CALL VENDER_CARRO('{placa}', '{data_venda}')")
    print(command)
    mysql_execute_command(command)



def select_all():
    result = None
    command = (f'''SELECT V.PLACA, C.MODELO, C.VALOR, V.DATA_VENDA 
                FROM VENDAS V INNER JOIN CARRO C ON V.PLACA = C.PLACA''')
    result = mysql_execute_select_all(command)
    return result