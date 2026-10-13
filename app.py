from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = 'tu_clave_secreta_para_flask'

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/contacto', methods=['POST'])
def contacto():
    nombre = request.form.get('nombre')
    email = request.form.get('email')
    mensaje = request.form.get('mensaje')
    
    print(f"Nuevo mensaje de {nombre} ({email}): {mensaje}")
    
    flash('¡Mensaje enviado con éxito! Nos pondremos en contacto pronto.', 'success')
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True, port=5000)