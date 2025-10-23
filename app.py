"""Tenemos que tener en cuenta que 'flask' es un modulo para utilizar las herramientas de flask y luego tenemos 'Flask' ya que este es una clase"""

from flask import Flask, render_template

app = Flask(__name__) #__name__ les esta diciendo a Flask en donde debe encontrar archivos (templates, static, etc)

"""Ahora con este codigo estaremos creando la primera ruta den flask, ya que esta nos dice @app.route('/') cuando el usuario ingrese a la URL raiz (http://localhost:5000/), tienes que ejecutar esta función"""

@app.route('/')
@app.route('/Inicio')
def inicio():
    # Ahora retornamos HTML completo
    # Fíjate cómo puedo usar comillas triples para escribir múltiples líneas
   return render_template('index.html' )

app.route('/saludo')
def saludo(nombre):
    return f"hola {nombre} Bienvenido a nuestra app"



if __name__ == '__main__':
    app.run(debug=True)
