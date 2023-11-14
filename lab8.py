from flask import Flask
from flask import render_template
from flask import request
from flask import redirect,url_for

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("lab8.html")


@app.route("/sumbit", methods=["POST"])
def sumbit():
    if len(request.form["prenom"]) < 1:
        return redirect(url_for("erreur"))
    with open("log.txt", "w") as fichier:
        fichier.write(
            "Prenom : " + request.form["prenom"] +
            "\nGenre : " + request.form["genre"] +
            "\nContinent : " + request.form["pays"]
        )
    return redirect(url_for("merci"))


@app.route("/erreur")
def erreur():
    # Dans un projet, nous devons return une page html
    return "<h1 style='color:red'>Attention! Merci de remplir tous les champs du formulaire."


@app.route("/merci")
def merci():
    # Dans un projet, nous devons return une page html
    return "<h1 style='color:green'> Merci, formulaire envoyé!</h1>"