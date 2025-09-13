from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def index():
    return "Hola mundo"

@app.route("/suma_numeros")
def sumar():
    return """
                <form action='/operar' method='post'>
                    Numero 1: <input name='n1'  id='n1' type='text'> Numero 2: <input name='n2' id='n2' type='text'>
                    <button type='submit'>Sumar</button>
                </form>
        """

@app.route("/operar", methods=["POST"])
def operar():
    n1 = request.form["n1"]
    n2= request.form["n2"]

    return f"Resultado: {int(n1) + int(n2)}"

app.run()