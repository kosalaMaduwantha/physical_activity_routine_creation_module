#!/usr/bin/env python3
import sys
sys.path.append('/home/kosala/git-rep/physical_activity_routine_creation_module/hexagonal-flask-app/app/adapters/rest/flask_server/')
import connexion

from swagger_server import encoder


def main():
    app = connexion.App(__name__, specification_dir='./swagger/')
    app.app.json_encoder = encoder.JSONEncoder
    app.add_api('swagger.yaml', arguments={'title': 'Diabtrek'}, pythonic_params=True)
    app.run(port=8081)


if __name__ == '__main__':
    main()
