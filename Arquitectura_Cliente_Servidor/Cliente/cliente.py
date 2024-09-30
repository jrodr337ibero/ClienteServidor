from flask import Flask, jsonify
import requests
import json

class Client:
    def __init__(self, server_url):
        self.server_url = server_url
    def send_saludando(self):
        nombre = input('Escribe tu nombre: ')
        response = requests.get(f'{self.server_url}/saludo', params={'nombre': nombre})
        return response.json()

    def send_data(self, data):
        response = requests.post(f'{self.server_url}/data', json=data)
        return response.json()

if __name__ == '__main__':
    client = Client('http://127.0.0.1:5000') 

    saludando_response = client.send_saludando()
    print(saludando_response)
    
    enviar_data = input('Escribe la informacion  que quieres enviar al servidor: ')
    data_response = client.send_data({'key': enviar_data})
    print(data_response)
