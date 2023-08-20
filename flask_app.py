from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/example")
def example():
    return render_template("example.html")

@app.route("/example/abc")
def abc():
    return render_template("abc.html")

@app.route("/example/one")
def one():
    return render_template("one.html")

@app.route("/list")
def list():
    return render_template("list.html")

@app.route("/example/scherzo")
def scherzo():
    return render_template("scherzo.html")

@app.route("/pyscript")
def pyscript():
    return render_template("pyscript.html")

@app.route("/navegadorag1")
def navegadorag1():
    return render_template("navegadorag1.html")

@app.route("/notexistent")
def notexistent():
    return render_template("archivo_no_disponible.html")

@app.route("/listag1")
def listag1():
    return render_template("listag1.html")

@app.route("/curiosities")
def curiosities():
    return render_template("curiosities.html")

@app.route("/wiki")
def wikilist():
    return render_template("wikilist.html")

@app.route("/wiki/quemadin_blue")
def quemadinblue():
    return render_template("wiki_quemadin_blue.html")

@app.route("/wiki/internet_explorer")
def internetexplorer():
    return render_template("wiki_Internet_Explorer.html")

@app.route("/wiki/spyglass")
def spyglass():
    return render_template("wiki_spyglass.html")

@app.route("/wiki/anexo_comparativa_de_navegadores_web")
def anexocomparativadenavegadoresweb():
    return render_template("wiki_Anexo_Comparativa_de_navegadores_web1.html")

@app.route("/wiki/diagrama_de_fase")
def diagramadefase():
    return render_template("wiki_Diagrama_de_fase.html")

@app.route("/calculadora")
def calculadora():
    return render_template("calculadora.html")

@app.route("/calculadora1")
def calculadora1():
    return render_template("calculadora1.html")

@app.route("/lineanavegador")
def lineadetiempodenavegadores():
    return render_template("linea de tiempo de navegadores.html")

@app.route("/lineasdetiempo")
def lineasdetiempo():
    return render_template("lineas de tiempo.html")

@app.route("/linea1")
def linea1():
    return render_template("build002.html")

@app.route("/snakegame")
def snakegame():
    return render_template("snakegame.html")

#@app.route("/lapaltadorada")
#def lapaltadorada():
    #return render_template("lapaltadorada.html")

@app.route("/versiones")
def versiones():
    return render_template("versiones.html")

if __name__ == "__main__":
    app.run(debug=True)