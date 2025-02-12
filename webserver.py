from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/todo-list', methods=['POST'])

def addTodoList():
    response = jsonify("todoList")
    return response

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000)