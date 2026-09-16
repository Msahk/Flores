import os
from flask import Flask, render_template, request, send_from_directory

app = Flask(__name__)

# Configuración básica de rutas
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
STATIC_DIR = os.path.join(BASE_DIR, 'static')
app.config['STATIC_DIR'] = STATIC_DIR

@app.route('/')
def index():
    ip_cliente = request.headers.get('X-Forwarded-For', request.remote_addr)
    if ip_cliente and ',' in ip_cliente:
        ip_cliente = ip_cliente.split(',')[0].strip()
    
    print(f"Conexión desde: {ip_cliente}")
    return render_template('index.html', ip_cliente=ip_cliente)

# Flask maneja /static de forma nativa. 
# Solo usa esta ruta si sirves archivos fuera de la carpeta estática por defecto.
@app.route('/static/<path:filename>')
def serve_static(filename):
    return send_from_directory(app.config['STATIC_DIR'], filename)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)