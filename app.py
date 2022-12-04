from flask import Flask, render_template, request, url_for
from persistence import carroDAO, vendasDAO, database
from controller import CarroController, VendasController

app = Flask(__name__)


@app.route('/')
def principal():
	return render_template("index.html")


@app.route('/cadastrar', methods=["GET", "POST"])
def cadastrar():
	if request.method == "POST":
		if request.form.get("placa") and request.form.get("modelo") and request.form.get("marca") and request.form.get("valor") and request.form.get("cor"):
			registros = (
				{"placa": request.form.get("placa"),
				"modelo": request.form.get("modelo"),
				"marca": request.form.get("marca"),
				"ano" : request.form.get("ano"),
				"valor": request.form.get("valor"),
				"cor" : request.form.get("cor"),
				"ar_condicionado" : request.form.get("ar_condicionado"),
				"ar_quente" : request.form.get("ar_quente"),
				"direcao" : request.form.get("direcao"),
				"vidros_eletricos" : request.form.get("vidros_eletricos"),
				"travas_eletricas" : request.form.get("travas_eletricas"),
				}
				)
		print(registros)
		CarroController.view_to_dao(registros)
	return render_template("cadastrar.html")

@app.route("/editar", methods=["GET", "POST"])
def editar():
	registro = {}
	if request.method == "POST":
		button_delete = request.form.get("delete")
		button_update = request.form.get("update")
		button_search = request.form.get("search")

		if button_delete != None:
			registros = ({"placa": request.form.get("Placa")})
			print(registros)
			CarroController.delete(registros)
		if button_update != None:
			registros = ({"placa": request.form.get("Placa"),
				"modelo": request.form.get("Modelo"),
				"marca": request.form.get("Marca"),
				"valor": request.form.get("Valor"),
				"ano" : request.form.get("Ano"),
				"cor" : request.form.get("Cor"),
				"ar_condicionado" : request.form.get("Ar-condicionado"),
				"ar_quente" : request.form.get("Ar-quente"),
				"direcao" : request.form.get("Direçao"),
				"vidros_eletricos" : request.form.get("Vidros Eletricos"),
				"travas_eletricas" : request.form.get("Travas Eletricas")
				})
				
			#print(registros)
			CarroController.update(registros)

		if button_search != None:
			print("search")
			if request.form.get("placa"):
				placa = request.form.get("placa")
				registro = CarroController.search_carro(placa)

	return render_template("editar.html", registro = registro)

@app.route("/pesquisar", methods=["GET", "POST"])
def pesquisar():
	registro = {}
	if request.method == "POST":
		
		if request.form.get("placa"):
			placa = request.form.get("placa")
			registro = CarroController.search_carro(placa)
	return render_template("pesquisar.html", registro = registro)

@app.route("/vender", methods=["GET", "POST"])
def vender():
    if request.method == "POST":
        if request.form.get("placa") and request.form.get("data_venda"):
            registros = (
                {"placa": request.form.get("placa"),
                 "data_venda": request.form.get("data_venda")
                 }
            )
        VendasController.view_to_dao(registros)
    return render_template("vender.html")

@app.route("/relatorio_vendas", methods=["GET", "POST"])
def relatorio_vendas():
	registros = VendasController.search_all()
	return render_template("relatorio_vendas.html", registros = registros)

@app.route("/relatorio_carros", methods=["GET", "POST"])
def relatorio_carros():
	registros = CarroController.search_all()
	return render_template("relatorio_carros.html", registros= registros)

database.create_modelo()
app.run(debug=True)

#http://127.0.0.1:5000