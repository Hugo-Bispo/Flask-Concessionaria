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
            PLACA CHAR(7),
            DATA_VENDA DATE,
            FOREIGN KEY(PLACA) REFERENCES CARRO(PLACA),
            CONSTRAINT PK_VENDAS PRIMARY KEY (PLACA, DATA_VENDA)
        )''')


    
    cursor.execute('''
        DROP PROCEDURE IF EXISTS VENDER_CARRO;
        ''')

    cursor.execute('''
                   
        CREATE PROCEDURE VENDER_CARRO (PLACA CHAR(7), DATA_VENDA DATE)
        BEGIN
        INSERT INTO VENDAS (PLACA, DATA_VENDA) VALUES (PLACA, DATA_VENDA);
        UPDATE CARRO C SET C.SITUACAO = 0 WHERE C.PLACA = PLACA;
        END;
        ''')