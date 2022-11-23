from flask import Flask, render_template, request, url_for
from persistence import carroDAO, database
from controller import CarroController

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
		#print(registros)
		CarroController.view_to_dao(registros)
	return render_template("cadastrar.html")

@app.route("/pesquisar", methods=["POST"])
def pesquisar():
	if request.method == "POST":
		CarroController.dao_to_view()
	return render_template("pesquisar.html")

@app.route("/relatorio_vendas")
def relatorio_vendas():
	return render_template("relatorio_vendas.html", registros=None)

@app.route("/relatorio_carros")
def relatorio_carros():
	return render_template("relatorio_carros.html", registros=None)



database.create_modelo()
app.run(debug=True)


#http://127.0.0.1:5000