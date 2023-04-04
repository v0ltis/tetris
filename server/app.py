from tools import DB_init as db_conn

def start() -> None:
    """
    Start the server
    """
    # Log to the database
    db = db_conn.connect()

if __name__ == '__main__':
    start()
