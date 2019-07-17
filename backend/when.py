import hashlib
import re
import sqlite3
import json

class When():

  dbpath = "database.db"
  
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
      cursor.execute("UPDATE when_table SET word=? WHERE id=?", (self.word, self.id))
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
      cursor.execute("DELETE FROM when_table WHERE id=?", (self.id,))
    except sqlite3.Error as e:
      print('sqlite3.Error occurred:', e.args[0])
      return False

    connection.commit()
    connection.close()
    return True

  @classmethod
  def initDatabase(cls, path="database.db"):
    cls.dbpath = path
    
    # DB connection
    connection = sqlite3.connect(cls.dbpath)
    cursor = connection.cursor()
    try:
      cursor.execute("CREATE TABLE IF NOT EXISTS when_table (id INTEGER PRIMARY KEY, word TEXT)")
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
      cursor.execute("SELECT * FROM when_table WHERE word=?", (word,))
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
        cursor.execute("INSERT INTO when_table(word) VALUES (:word)", {'word': word})
        cursor.execute("SELECT * FROM when_table WHERE word=?", (word,))
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
      cursor.execute("SELECT * FROM when_table ORDER BY random() LIMIT 1")
      u = cursor.fetchone()
      if u:
        data = cls(u['id'], u['word'])

    except sqlite3.Error as e:
      print('sqlite3.Error occurred:', e.args[0])

    connection.close()
    return json.dumps(data.toJSON())
