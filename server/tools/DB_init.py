# reading the yaml config file
from yaml import load, Loader
from server.classes.database import Database

def connect() -> Database:
    # reading the config file
    with open("../config.yml", 'r') as ymlfile:
        cfg = load(ymlfile, Loader=Loader)

    # connecting to the database

    return Database(
        host = cfg['database']['host'],
        database = cfg['database']['database'],
        user = cfg['database']['user'],
        password = ['database']['password'],
        port = cfg['database']['port']
    )

x = connect()
