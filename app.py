from flask import Flask, render_template
# Render_template sera utilizado para tomar las paginas HTML y renderilarlo esas vistas en las ruatas que creemos con flask

app = Flask(__name__) 
#__name__ les esta diciendo a Flask en donde debe encontrar archivos (templates, static, etc)

@app.route('/')
@app.route('/index')
# Mediante la funcion de app.route, flask creara ciertas rutas para que el usuario pueda moverse libremente cada vez que ingresa a distintos apartados de la app web APIfood

# Primera ruta creada
def inicio():
    # Ahora retornamos HTML completo
   return render_template('index.html' )

# Segunda ruta creada
@app.route('/ingreso') 
def ingreso():
    return render_template('ingreso.html')

# Plantilla base de HTML
@app.route("/base")
def base():
    return render_template("base.html", name="Hanks")


if __name__ == '__main__':
    app.run(debug=True)

