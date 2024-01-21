from sqlite3 import connect


class Database:
    def __init__(self):
        self.conn = connect("database.db", check_same_thread=False)
        self.cur = self.conn.cursor()
        self.cur.execute("""CREATE TABLE IF NOT EXISTS users (id INTEGER)""")
        self.conn.commit()

    def insertUser(self, id: int):
        """Функция добавляет пользователя с `ID` в список донатеров"""
        self.cur.execute("INSERT INTO users VALUES (?)", (id,))
        self.conn.commit()

    def isPurchased(self, id: int) -> bool:
        """Функция проверяет купил ли пользователь с таким `ID` подписку или нет.\n
        Возращает тип `bool`
        """
        self.cur.execute("SELECT id FROM users WHERE id = ?", (id,))
        return not (self.cur.fetchone() is None)
