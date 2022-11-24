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
