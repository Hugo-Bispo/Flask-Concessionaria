import mysql.connector

mybd = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    passwd = "12345678",
    database = "CONCESSIONARIA"
)
cursor = mybd.cursor()

def insert_carro(registros):
    placa = registros["placa"]
    modelo = registros["modelo"]
    marca = registros["marca"]
    valor = registros["valor"]
    cor = registros["cor"]
    ar_condicionado = registros["ar_condicionado"]
    ar_quente = registros["ar_quente"]
    vidros_eletricos = registros["vidros_eletricos"]
    travas_eletricas = registros["travas_eletricas"]
    direcao = registros["direcao"]

    cursor.execute(f'''
        INSERT INTO CARRO (PLACA, MODELO, MARCA, VALOR, COR, AR_CONDICIONADO, AR_QUENTE, VIDROS_ELETRICOS, TRAVAS_ELETRICAS, DIRECAO) VALUES (
            "{placa}", "{modelo}", "{marca}", "{valor}", "{cor}", {ar_condicionado}, {ar_quente}, {vidros_eletricos}, {travas_eletricas}, "{direcao}"
        )''')
    mybd.commit()

def update_carro(registros):
    placa = registros["placa"]
    modelo = registros["modelo"]
    marca = registros["marca"]
    valor = registros["valor"]
    cor = registros["cor"]
    ar_condicionado = registros["ar_condicionado"]
    ar_quente = registros["ar_quente"]
    vidros_eletricos = registros["vidros_eletricos"]
    travas_eletricas = registros["travas_eletricas"]
    direcao = registros["direcao"]

    cursor.execute(f'''
        UPDATE CARRO SET
            MODELO = "{modelo}",
            MARCA = "{marca}",
            VALOR = "{valor}",
            COR = "{cor}",
            AR_CONDICIONADO = "{ar_condicionado}",
            AR_QUENTE = "{ar_quente}",
            VIDROS_ELETRICOS = "{vidros_eletricos}",
            TRAVAS_ELETRICAS = "{travas_eletricas}",
            DIRECAO = "{direcao}"
        WHERE PLACA = "{placa}"
    ''')
    mybd.commit()

def delete_carro(registros):
    placa = registros["placa"]

    cursor.execute(f'''
        DELETE FROM VENDAS WHERE PLACA = "{placa}"
    ''')

    cursor.execute(f'''
        DELETE FROM CARRO WHERE PLACA = "{placa}"
    ''')
    mybd.commit()

def select_carro(placa):
    result = None
    cursor.execute(f'''SELECT PLACA, MODELO, MARCA, COR, VALOR, SITUACAO, AR_CONDICIONADO, 
                    AR_QUENTE, DIRECAO, VIDROS_ELETRICOS, TRAVAS_ELETRICAS FROM CARRO
                    WHERE PLACA = "{placa}"''')
    result = cursor.fetchone()
    return result


def select_all():
    result = None
    cursor.execute(f'''SELECT PLACA, MODELO, MARCA, COR, VALOR, SITUACAO, AR_CONDICIONADO, 
                    AR_QUENTE, DIRECAO, VIDROS_ELETRICOS, TRAVAS_ELETRICAS FROM CARRO
                    ''')
    result = cursor.fetchall()
    return result
