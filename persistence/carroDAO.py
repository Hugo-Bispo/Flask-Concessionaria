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


def select_carro(placa):
    cursor.execute(f'''SELECT PLACA, MODELO, MARCA, COR, VALOR, SITUACAO, AR_CONDICIONADO, 
                    AR_QUENTE, DIRECAO, VIDROS_ELETRICOS, TRAVAS_ELETRICAS FROM CARRO
                    WHERE PLACA = "{placa}"''')
    result = cursor.fetchone()
    result ={"placa": result[0],
			"modelo": result[1],
			"marca": result[2],
			"cor": result[3],
			"valor" : result[4],
            "situacao" : result[5],
			"ar_condicionado" : result[6],
			"ar_quente" : result[7],
			"direcao" : result[8],
			"vidros_eletricos" : result[9],
			"travas_eletricas" : result[10],
	        }
    

    print(result)
    return result
