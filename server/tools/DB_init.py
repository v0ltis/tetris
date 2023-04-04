# import datetime that allow using time Object
from datetime import datetime
from tools.conf_load import load

from classes.database import Database

def connect() -> Database:
    """
    Establish a connection to the database

    Returns:
        Database: The database object
    """
    cfg = load()

    # connecting to the database

    return Database(
        host = cfg['database']['host'],
        database = cfg['database']['database'],
        user = cfg['database']['user'],
        password = cfg['database']['password'],
        port = cfg['database']['port']
    ).connect()
