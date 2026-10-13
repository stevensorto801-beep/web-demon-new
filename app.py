from flask import Flask, render_template, request, redirect, url_for, flash
import os

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
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
