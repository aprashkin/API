import psycopg2


def get_db_connection():
    conn = psycopg2.connect(
        host="193.176.78.35",
        port="5433",
        database="user1",
        user="user1",
        password="vVplV"
    )
    return conn