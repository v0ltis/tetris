from tools import DB_init as db_conn
from datetime import datetime

def start():
    # Log to the database
    db = db_conn.connect()
    
    print(db.get_scores(3))

    print(db.get_scores(3, 2))

if __name__ == '__main__':
    start()
