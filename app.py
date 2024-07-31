from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)



@app.route('/simulacion/<int:cantidadLineasASimular>/<int:duracionSimulacion>/<int:lineaInicioVisualizacion>/<int:lineaFinVisualizacion>/<int:cantidadSurtidores>/<int:cantidadEmpleadosGomeria>/<int:cantidadEmpleadosVentaAccesorios>/<int:llegadaClientesMedia>/<int:llegadaClientesDesviacion>/<int:aDuracionCargaCombustible>/<int:bDuracionCargaCombustible>/<int:aDuracionAtGomeria>/<int:bDuracionAtGomeria>/<int:aDuracionVentaAccesorios>/<int:bDuracionVentaAccesorios>', methods=['GET', 'POST'])
def simulacion(cantidadLineasASimular, duracionSimulacion, lineaInicioVisualizacion,
            lineaFinVisualizacion, cantidadSurtidores, cantidadEmpleadosGomeria, cantidadEmpleadosVentaAccesorios,
            llegadaClientesMedia, llegadaClientesDesviacion, aDuracionCargaCombustible, bDuracionCargaCombustible,
            aDuracionAtGomeria, bDuracionAtGomeria, aDuracionVentaAccesorios, bDuracionVentaAccesorios):
    # Aquí puedes agregar lógica para manejar los parámetros
    data = {
        "cantidadLineasASimular": cantidadLineasASimular,
        "duracionSimulacion": duracionSimulacion,
        "lineaInicioVisualizacion": lineaInicioVisualizacion,
        "lineaFinVisualizacion": lineaFinVisualizacion,
    }

    # Aquí puedes agregar la lógica de simulación utilizando los parámetros
    # Esta es una muestra de modificación de parámetros para mostrar que funciona
    data["duracionSimulacion"] += 1
    data["lineaInicioVisualizacion"] += 10000000

    return jsonify(data)

if __name__ == '__main__':
    app.run(host='localhost', port=8000)

