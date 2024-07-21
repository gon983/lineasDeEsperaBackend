from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/simulacion/<int:param1>/<int:param2>', methods=['GET', 'POST'])
def simulacion(param1, param2):
    # Aquí puedes agregar lógica para manejar los parámetros
    param1 += 1
    param2 += 10000000
    data = {
        "duracionSimulacion": param1,
        "lineaInicioSimulacion": param2
    }
    return jsonify(data)

if __name__ == '__main__':
    app.run(host='localhost', port=8000)
