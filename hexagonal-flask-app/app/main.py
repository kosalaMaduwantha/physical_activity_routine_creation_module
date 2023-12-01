from flask import Flask, request, jsonify
from .adapters import request as request_adapter
from .adapters import response as response_adapter
from .services import service as app_service

app = Flask(__name__)

@app.route('/api/resource', methods=['POST'])
def create_resource():
    resource_data = request.get_json()
    resource = request_adapter.from_request(resource_data)
    created_resource = app_service.create_resource(resource)
    return response_adapter.to_response(created_resource), 201

@app.route('/api/resource/<int:resource_id>', methods=['GET'])
def get_resource(resource_id):
    resource = app_service.get_resource(resource_id)
    if resource is None:
        return jsonify({'error': 'Resource not found'}), 404
    return response_adapter.to_response(resource)

if __name__ == '__main__':
    app.run(debug=True)