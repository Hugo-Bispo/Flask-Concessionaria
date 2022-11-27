from flask import Flask, render_template, request, url_for
from persistence import carroDAO, vendasDAO, database
from controller import CarroController, VendasController

app = Flask(__name__)


@app.route('/')
def principal():
	return render_template("index.html")


@app.route('/cadastrar', methods=["GET", "POST"])
def cadastrar():
	#notas = {"Fulano":5.0, "Beltrano":6.0, "Aluno": 7.0, "Sicrano":8.5, "Rodrigo":9.5}
	if request.method == "POST":
		if request.form.get("placa") and request.form.get("modelo") and request.form.get("marca") and request.form.get("valor") and request.form.get("cor"):
			registros = (
				{"placa": request.form.get("placa"),
				"modelo": request.form.get("modelo"),
				"marca": request.form.get("marca"),
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