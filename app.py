from flask import Flask, jsonify, request

app = Flask(__name__)


@app.route('/simulacion/<int:cantidadLineasASimular>/<int:duracionSimulacion>/<int:lineaInicioVisualizacion>'
        '/<int:lineaFinVisualizacion>/<int:cantidadSurtidores>/<int:cantidadEmpleadosGomeria>/<int:cantidadEmpleadosVentaAccesorios>'
        '/<float:llegadaClientesMedia>/<float:llegadaClientesDesviacion>/<float:aDuracionCargaCombustible>/<float:bDuracionCargaCombustible>'
        '/<float:aDuracionAtGomeria>/<float:bDuracionAtGomeria>/<float:aDuracionVentaAccesorios>/<float:bDuracionVentaAccesorios>', methods=['GET', 'POST'])
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
        "cantidadSurtidores": cantidadSurtidores,
        "cantidadEmpleadosGomeria": cantidadEmpleadosGomeria,
        "cantidadEmpleadosVentaAccesorios": cantidadEmpleadosVentaAccesorios,
        "llegadaClientesMedia": llegadaClientesMedia,
        "llegadaClientesDesviacion": llegadaClientesDesviacion,
        "aDuracionCargaCombustible": aDuracionCargaCombustible,
        "bDuracionCargaCombustible": bDuracionCargaCombustible,
        "aDuracionAtGomeria": aDuracionAtGomeria,
        "bDuracionAtGomeria": bDuracionAtGomeria,
        "aDuracionVentaAccesorios": aDuracionVentaAccesorios,
        "bDuracionVentaAccesorios": bDuracionVentaAccesorios,
    }

    # Aquí puedes agregar la lógica de simulación utilizando los parámetros
    # Esta es una muestra de modificación de parámetros para mostrar que funciona
    data["duracionSimulacion"] += 1
    data["lineaInicioVisualizacion"] += 10000000

    return jsonify(data)

if __name__ == '__main__':
    app.run(host='localhost', port=8000)

