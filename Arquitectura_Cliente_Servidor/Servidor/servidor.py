from flask import Flask, jsonify, request

class Server:
    def __init__(self):
        self.app = Flask(__name__)
        self.setup_routes()
        
    def setup_routes(self):
        @self.app.route('/saludo', methods=['GET'])
        def saludar():
            name = request.args.get('nombre', 'Mundo')
            return jsonify(message=f'¡Hola, {name}!')

        @self.app.route('/data', methods=['POST'])
        def receive_data():
            data = request.json
            return jsonify(response=f'Datos recibidos: {request.json}')

    def run(self):
        self.app.run(debug=True)

if __name__ == '__main__':
    server = Server()
    server.run()
