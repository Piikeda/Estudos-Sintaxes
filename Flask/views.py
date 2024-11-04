from main import app
from flask import render_template

#rotas
@app.route("/")
def homepage():
    return render_template("homepage.html")

#rotas
@app.route("/blog")
def blog():
    return "Meu blog no flask"