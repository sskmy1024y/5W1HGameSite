import hashlib
import re
import sqlite3
import json


class Element():

    dbpath = "database.db"
    table_name = "when_table"

    def __init__(self, id, word):
        self.id = id
        self.word = word

    def setWord(self, word):
        self.word = word

    def getWord(self):
        return self.word

    def toJSON(self):
        return {'id': self.id, 'word': self.word}

    def update(self):
        # DB connection
        connection = sqlite3.connect(self.dbpath)
        cursor = connection.cursor()

        try:
            cursor.execute("UPDATE " + self.table_name + " SET word=? WHERE id=?",
                           (self.word, self.id))
        except sqlite3.Error as e:
            print('sqlite3.Error occurred:', e.args[0])
            return False

        connection.commit()
        connection.close()
        return self

    def delete(self):
        connection = sqlite3.connect(self.dbpath)
        cursor = connection.cursor()
        try:
            cursor.execute("DELETE FROM " + self.table_name +
                           " WHERE id=?", (self.id,))
        except sqlite3.Error as e:
            print('sqlite3.Error occurred:', e.args[0])
            return False

        connection.commit()
        connection.close()
        return True

    @classmethod
    def initAllDatabase(cls, path="database.db"):
        cls.dbpath = path
        table_names = ['when_table', 'where_table', 'who_table',
                       'why_table', 'what_table', 'how_table']  # 70点以下はないので、合格

        for table_name in table_names:
            cls.initDatabase(table_name, cls.dbpath)

    @classmethod
    def initDatabase(cls, table_name, path="database.db"):
        cls.dbpath = path

        # DB connection
        connection = sqlite3.connect(cls.dbpath)
        cursor = connection.cursor()
        try:
            cursor.execute(
                "CREATE TABLE IF NOT EXISTS " + table_name + " (id INTEGER PRIMARY KEY, word TEXT)")
        except sqlite3.Error as e:
            print('sqlite3.Error occurred:', e.args[0])

        connection.commit()
        connection.close()

    @classmethod
    def find(cls, word):
        data = False
        # DB connection
        connection = sqlite3.connect(cls.dbpath)
        connection.row_factory = sqlite3.Row
        cursor = connection.cursor()

        try:
            cursor.execute("SELECT * FROM " + cls.table_name +
                           " WHERE word=?", (word,))
            u = cursor.fetchone()
            if u:
                data = cls(u['id'], u['word'])
        except sqlite3.Error as e:
            print('sqlite3.Error occurred:', e.args[0])

        connection.close()
        return data

    @classmethod
    def register(cls, word):
        if cls.find(word):
            return False
        else:
            data = False
            # DB connection
            connection = sqlite3.connect(cls.dbpath)
            connection.row_factory = sqlite3.Row
            cursor = connection.cursor()
            try:
                cursor.execute(
                    "INSERT INTO " + cls.table_name + "(word) VALUES (:word)", {'word': word})
                cursor.execute(
                    "SELECT * FROM " + cls.table_name + " WHERE word=?", (word,))
                u = cursor.fetchone()
                if u:
                    data = cls(u['id'], u['word'])

            except sqlite3.Error as e:
                print('sqlite3.Error occurred:', e.args[0])
                return False

            connection.commit()
            connection.close()
            return data

    @classmethod
    def getRandom(cls):
        data = []
        # DB connection
        connection = sqlite3.connect(cls.dbpath)
        connection.row_factory = sqlite3.Row
        cursor = connection.cursor()

        try:
            cursor.execute(
                "SELECT * FROM " + cls.table_name + " ORDER BY random() LIMIT 1")
            u = cursor.fetchone()
            if u:
                data = cls(u['id'], u['word'])

        except sqlite3.Error as e:
            print('sqlite3.Error occurred:', e.args[0])

        connection.close()
        if data:
            return data.toJSON()
        else:
            return {}


class When(Element):

    table_name = "when_table"

    def __init__(self, id, word):
        super().__init__(id, word)


class Where(Element):

    table_name = "where_table"

    def __init__(self, id, word):
        super().__init__(id, word)


class Who(Element):

    table_name = "who_table"

    def __init__(self, id, name):
        super().__init__(id, name)


class Why(Element):

    table_name = "why_table"

    def __init__(self, id, word):
        super().__init__(id, word)


class What(Element):

    table_name = "what_table"

    def __init__(self, id, word):
        super().__init__(id, word)


class How(Element):

    table_name = "how_table"

    def __init__(self, id, word):
        super().__init__(id, word)
