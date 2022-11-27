import mysql.connector

mybd = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    passwd="12345678",
    database="CONCESSIONARIA"
)
cursor = mybd.cursor()


def insert_venda(registros):
    placa = registros["placa"]
    data_venda = registros["data_venda"]

    cursor.execute(f'''
        CALL VENDER_CARRO('{placa}', '{data_venda}')
        ''')

    mybd.commit()

def select_all():
    result = None
    cursor.execute(f'''SELECT V.PLACA, C.MODELO, C.VALOR, V.DATA_VENDA FROM VENDAS V
                        INNER JOIN CARRO C ON V.PLACA = C.PLACA
                    ''')
    result = cursor.fetchall()
    print(result)
    return result