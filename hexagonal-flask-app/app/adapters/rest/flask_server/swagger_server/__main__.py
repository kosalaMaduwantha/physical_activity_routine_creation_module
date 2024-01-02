#!/usr/bin/env python3
import sys
sys.path.append('/home/kosala/git-repositories/physical_activity_routine_creation_module/hexagonal-flask-app/')
sys.path.append('/home/kosala/git-repositories/physical_activity_routine_creation_module/hexagonal-flask-app/app/adapters/rest/flask_server/')
import connexion
from app.adapters.db.mysql_adapter import MySQLAdapter
from app.adapters.db.db_table_creation import create_db_and_tables, drop_db
from swagger_server import encoder


def main():
    create_db_and_tables()
    # temporily enter user data
    data_base_adapter = MySQLAdapter()
    data_base_adapter.enter_user_tempory(user_id="user_0001", username="kosala", 
                                         password="1234", email="kosala@gmail.com")
    app = connexion.App(__name__, specification_dir='./swagger/')
    app.app.json_encoder = encoder.JSONEncoder
    app.add_api('swagger.yaml', arguments={'title': 'Diabtrek'}, pythonic_params=True)
    app.run(port=8081)


if __name__ == '__main__':
    main()
