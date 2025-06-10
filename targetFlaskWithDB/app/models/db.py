from mysql.connector import pooling


class Db:
    def __init__(self):
        self._pool = pooling.MySQLConnectionPool(
            pool_name="mypool",
            pool_size=5,
            host="localhost",
            user="root",
            password="1234",
            database="test",
        )

    def select(self):
        conn = self._pool.get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM test")
        rows = cursor.fetchall()
        cursor.close()
        conn.close()
        return rows
