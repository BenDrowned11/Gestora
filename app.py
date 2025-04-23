from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

inventario = []

@app.route('/api/inventario', methods=['GET'])
def obtener_inventario():
    return jsonify(inventario)

@app.route('/api/inventario', methods=['POST'])
def agregar_producto():
    producto = request.json
    inventario.append(producto)
    return jsonify({"mensaje": "Producto agregado", "producto": producto}), 201

@app.route('/api/inventario/<int:indice>', methods=['DELETE'])
def eliminar_producto(indice):
    if 0 <= indice < len(inventario):
        eliminado = inventario.pop(indice)
        return jsonify({"mensaje": "Producto eliminado", "producto": eliminado})
    return jsonify({"error": "Índice fuera de rango"}), 400

if __name__ == '__main__':
    app.run(debug=True)
