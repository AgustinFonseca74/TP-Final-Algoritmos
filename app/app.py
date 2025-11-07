from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def inicio():
      return render_template('pantalla_inicio.html')

@app.route('/pantalla_inicio')
def pantalla_inicio():
       return render_template('pantalla_inicio.html')

    

@app.route('/turnos_disponibles')
def turnos_disponibles():
       return render_template("turnos_disponibles.html")

@app.route('/registrar_turnos')
def registrar_turnos():
       return render_template("registrar_turnos.html")

@app.route('/base')
def calendario():
       return render_template("base.html")

@app.route('/oaa')
def oaa():
       return render_template("oaa.js")

if __name__ == '__main__':
    app.run(debug=True, port=5000)