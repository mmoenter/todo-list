from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/todo-lists', methods=['POST'])

def todoLists():
    response = jsonify("todoList")
    return response

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000)