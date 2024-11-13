from flask import Flask, request, jsonify

app = Flask(__name__)

# Base de datos simulada en memoria
estudiantes = []

@app.route('/estudiantes', methods=['POST'])
def crear_estudiante():
    data = request.get_json()
    if 'nombre' not in data or 'edad' not in data or data['edad'] < 0:
        return jsonify({'error': 'Datos inválidos'}), 400

    estudiante = {
        'id': len(estudiantes) + 1,
        'nombre': data['nombre'],
        'edad': data['edad']
    }
    estudiantes.append(estudiante)
    return jsonify(estudiante), 201

@app.route('/estudiantes', methods=['GET'])
def listar_estudiantes():
    return jsonify(estudiantes), 200

if __name__ == '__main__':
    app.run(debug=True, port=5000)
