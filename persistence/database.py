import mysql.connector

mybd = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    passwd = "12345678",
)
cursor = mybd.cursor()

def create_modelo():
    __create_database()
    __create_tables()

def __create_database():
    cursor.execute("CREATE DATABASE IF NOT EXISTS CONCESSIONARIA")
    cursor.execute("USE CONCESSIONARIA")

def __create_tables():
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS CARRO(
	        PLACA CHAR(7) PRIMARY KEY,
            MODELO VARCHAR(20) NOT NULL,
            MARCA VARCHAR(15) NOT NULL,
            COR VARCHAR(30) NOT NULL,
            VALOR DECIMAL(10,2) NOT NULL,
            SITUACAO BOOLEAN DEFAULT 1,
            AR_CONDICIONADO BOOLEAN,
            AR_QUENTE BOOLEAN,
            DIRECAO CHAR(1) NOT NULL,
            VIDROS_ELETRICOS BOOLEAN,
            TRAVAS_ELETRICAS BOOLEAN
        )''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS VENDAS(
            ID_VENDA INT4 PRIMARY KEY AUTO_INCREMENT,
            PLACA CHAR(7) NOT NULL,
            DATA_VENDA DATE NOT NULL,
            FOREIGN KEY(PLACA) REFERENCES CARRO(PLACA)
        )''')