from flask import Flask, request, jsonify

app = Flask(__name__)

# Base de datos simulada en memoria
estudiantes = []

# Endpoint para la raíz (index)
@app.route('/', methods=['GET'])
def index():
    return jsonify({"message": "Bienvenido a la API de estudiantes"}), 200

# Endpoint para crear un nuevo estudiante
@app.route('/estudiantes', methods=['POST'])
def crear_estudiante():
    data = request.get_json()
    
    # Validación de datos
    if not data or 'nombre' not in data or 'edad' not in data:
        return jsonify({'error': 'Datos inválidos'}), 400

    if not isinstance(data['edad'], int) or data['edad'] < 0:
        return jsonify({'error': 'Edad debe ser un número entero positivo'}), 400
    
    estudiante = {
        'id': len(estudiantes) + 1,
        'nombre': data['nombre'],
        'edad': data['edad']
    }
    
    estudiantes.append(estudiante)
    return jsonify(estudiante), 201

# Endpoint para listar todos los estudiantes
@app.route('/estudiantes', methods=['GET'])
def listar_estudiantes():
    return jsonify(estudiantes), 200

# Punto de entrada de la aplicación
if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port=5000)
