from flask import request
from flask import Flask, jsonify
from flask import Flask
app = Flask(__name__)

todos=[ { "label": "My first task", "done": False } ]


@app.route('/todos', methods=['GET'])
def hello_world():
    json_text = jsonify(todos)
    return json_text

@app.route('/todos', methods=['POST'])
def add_new_todo():
    request_body = request.json
    print("Incoming request with the following body", request_body)
    todos.append(request_body)
    return jsonify(todos)

@app.route('/todos/<int:position>', methods=['DELETE'])
def delete_todo(position):
    if 0 <= position < len(todos):  # Verifica que la posición sea válida
        deleted_todo = todos[position]  # Almacena el todo que se va a eliminar
        del todos[position]  # Elimina el todo en la posición especificada
        return jsonify(deleted_todo)  # Retorna el todo eliminado
    return jsonify({"error": "Posición no válida"}), 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3246, debug=True)