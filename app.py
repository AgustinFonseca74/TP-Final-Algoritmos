from flask import Flask, render_template

app = Flask(__name__)



@app.route('/')
def pantalla_inicio():
       return render_template('base.html')

    

@app.route('/turnos_disponibles')
def turnos_disponibles():
       return render_template("turnos_disponibles.html")

@app.route('/registrar_turnos')
def registrar_turnos():
       return render_template("registrar_turnos.html")

@app.route('/calendario')
def calendario():
       return render_template("calendario.html")

if __name__ == '__main__':
    app.run(debug=True)