class Carro():
    def __init__(self, placa, modelo, marca, cor, valor, situacao=False, ar_condicionado, ar_quente, vidros_eletricos, travas_eletricas):
        self.placa = placa
        self.modelo = modelo
        self.marca = marca
        self.valor = valor
        self.cor = cor
        self.ar_condicionado = ar_condicionado
        self.ar_quente = ar_quente
        self.vidros_eletricos = vidros_eletricos
        self.travas_eletricas = travas_eletricas
    
    # Getter
    @property
    def placa(self):
        return self._preco

    # Setter
    @placa.setter
    def placa(self, placa_carro):
        pass