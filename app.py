from flask import Flask, jsonify
from flask_cors import CORS
from Simulacion import *

app = Flask(__name__)
CORS(app)



@app.route('/simulacion/<int:cantidadLineasASimular>/<int:duracionSimulacion>/<int:lineaInicioVisualizacion>/<int:lineaFinVisualizacion>/<int:cantidadSurtidores>/<int:cantidadEmpleadosGomeria>/<int:cantidadEmpleadosVentaAccesorios>/<int:llegadaClientesMedia>/<int:llegadaClientesDesviacion>/<int:aDuracionCargaCombustible>/<int:bDuracionCargaCombustible>/<int:aDuracionAtGomeria>/<int:bDuracionAtGomeria>/<int:aDuracionVentaAccesorios>/<int:bDuracionVentaAccesorios>', methods=['GET', 'POST'])
def generarSimulacion(cantidadLineasASimular, duracionSimulacion, lineaInicioVisualizacion,
        lineaFinVisualizacion, cantidadSurtidores, cantidadEmpleadosGomeria, cantidadEmpleadosVentaAccesorios,
        llegadaClientesMedia, llegadaClientesDesviacion, aDuracionCargaCombustible, bDuracionCargaCombustible,
        aDuracionAtGomeria, bDuracionAtGomeria, aDuracionVentaAccesorios, bDuracionVentaAccesorios):
# Aquí puedes agregar lógica para manejar los parámetros

        simulacion = Simulacion(cantidadLineasASimular, duracionSimulacion, lineaInicioVisualizacion,
        lineaFinVisualizacion, cantidadSurtidores, cantidadEmpleadosGomeria, cantidadEmpleadosVentaAccesorios,
        llegadaClientesMedia, llegadaClientesDesviacion, aDuracionCargaCombustible, bDuracionCargaCombustible,
        aDuracionAtGomeria, bDuracionAtGomeria, aDuracionVentaAccesorios, bDuracionVentaAccesorios)


        data = simulacion.simular()
        # print(data)
        
        
        


        return jsonify(data)

if __name__ == '__main__':
        from waitress import serve
        serve(app, host='0.0.0.0', port=8000, threads=1)

