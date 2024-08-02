from flask import Flask, jsonify
from flask_cors import CORS
from Simulacion import *

app = Flask(__name__)
CORS(app)



@app.route('/simulacion/<int:cantidadLineasASimular>/<int:duracionSimulacion>/<int:lineaInicioVisualizacion>/<int:lineaFinVisualizacion>/<int:cantidadSurtidores>/<int:cantidadEmpleadosGomeria>/<int:cantidadEmpleadosVentaAccesorios>/<float:llegadaClientesMedia>/<float:llegadaClientesDesviacion>/<float:aDuracionCargaCombustible>/<float:bDuracionCargaCombustible>/<int:aDuracionAtGomeria>/<int:bDuracionAtGomeria>/<int:aDuracionVentaAccesorios>/<int:bDuracionVentaAccesorios>', methods=['GET', 'POST'])
def generarSimulacion(cantidadLineasASimular, duracionSimulacion, lineaInicioVisualizacion,
        lineaFinVisualizacion, cantidadSurtidores, cantidadEmpleadosGomeria, cantidadEmpleadosVentaAccesorios,
        llegadaClientesMedia, llegadaClientesDesviacion, aDuracionCargaCombustible, bDuracionCargaCombustible,
        aDuracionAtGomeria, bDuracionAtGomeria, aDuracionVentaAccesorios, bDuracionVentaAccesorios):
# Aquí puedes agregar lógica para manejar los parámetros

        simulacion = Simulacion(cantidadLineasASimular, duracionSimulacion, lineaInicioVisualizacion,
        lineaFinVisualizacion, cantidadSurtidores, cantidadEmpleadosGomeria, cantidadEmpleadosVentaAccesorios,
        llegadaClientesMedia, llegadaClientesDesviacion, aDuracionCargaCombustible, bDuracionCargaCombustible,
        aDuracionAtGomeria, bDuracionAtGomeria, aDuracionVentaAccesorios, bDuracionVentaAccesorios)


        simulacion.simular()
        data = simulacion.generarTabla()
        


        return jsonify(data)

if __name__ == '__main__':
        app.run(host='localhost', port=8000)

