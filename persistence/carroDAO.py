import mysql.connector
from controller.database_connection import mysql_execute_command, mysql_execute_select, mysql_execute_select_all

def insert_carro(registros):
    print(registros)
    placa = registros["placa"]
    modelo = registros["modelo"]
    marca = registros["marca"]
    valor = registros["valor"]
    cor = registros["cor"]
    ano = registros["ano"]
    ar_condicionado = registros["ar_condicionado"]
    ar_quente = registros["ar_quente"]
    vidros_eletricos = registros["vidros_eletricos"]
    travas_eletricas = registros["travas_eletricas"]
    direcao = registros["direcao"]
    command = f'''INSERT INTO CARRO (PLACA, MODELO, MARCA, VALOR, COR, ANO, AR_CONDICIONADO, AR_QUENTE, VIDROS_ELETRICOS, TRAVAS_ELETRICAS, DIRECAO) VALUES (
            "{placa}", "{modelo}", "{marca}", "{valor}", "{cor}", "{ano}", "{ar_condicionado}", "{ar_quente}", "{vidros_eletricos}", "{travas_eletricas}", "{direcao}")'''
    print(command)
    mysql_execute_command(command)
        

def update_carro(registros):

    placa = registros["placa"]
    modelo = registros["modelo"]
    marca = registros["marca"]
    valor = registros["valor"]
    cor = registros["cor"]
    ano = registros["ano"]
    ar_condicionado = registros["ar_condicionado"]
    ar_quente = registros["ar_quente"]
    vidros_eletricos = registros["vidros_eletricos"]
    travas_eletricas = registros["travas_eletricas"]
    direcao = registros["direcao"]

    command = (f'''
        UPDATE CARRO SET
            MODELO = "{modelo}",
            MARCA = "{marca}",
            VALOR = "{valor}",
            COR = "{cor}",
            ANO = "{ano}",
            AR_CONDICIONADO = "{ar_condicionado}",
            AR_QUENTE = "{ar_quente}",
            VIDROS_ELETRICOS = "{vidros_eletricos}",
            TRAVAS_ELETRICAS = "{travas_eletricas}",
            DIRECAO = "{direcao}"
        WHERE PLACA = "{placa}"
    ''')
    mysql_execute_command(command)

def delete_carro(registros):
    placa = registros["placa"]

    command = f"CALL EXCLUIR_CARRO('{placa}')"
    mysql_execute_command(command)


def select_carro(placa):
    result = None
    command = (f'''SELECT PLACA, MODELO, MARCA, COR, VALOR, ANO, SITUACAO, AR_CONDICIONADO, 
                    AR_QUENTE, DIRECAO, VIDROS_ELETRICOS, TRAVAS_ELETRICAS FROM CARRO
                    WHERE PLACA = "{placa}"''')
    result = mysql_execute_select(command)
    return result


def select_all():

    result = None
    command = (f'''SELECT PLACA, MODELO, MARCA, COR, VALOR, ANO, SITUACAO, AR_CONDICIONADO, 
                    AR_QUENTE, DIRECAO, VIDROS_ELETRICOS, TRAVAS_ELETRICAS FROM CARRO
                    ''')
    result = mysql_execute_select_all(command)
    return result
