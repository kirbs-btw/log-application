import sqlite3
import datetime

class sqlConn:
    def __init__(self, path):
        self.conn = sqlite3.connect(path)
        self.cur = self.conn.cursor()

    def execute(self, command):
        out = self.cur.execute(command)
        self.conn.commit()

        return out

    def check(self, table):
        command = 'SELECT * FROM {}'.format(table)
        content = self.execute(command).fetchall()
        print(content)

    def reset(self, table):
        command = 'DELETE FROM {}'.format(table)
        self.execute(command)

conn = sqlConn('log.sql')

def shell():
    conn.check('log')


def createSQL():
    f = open("log.sql", "w+")

def createTable():
    command = "CREATE TABLE log(date DATE, time VARCHAR(8), entry TEXT)"
    conn.execute(command)

if __name__ == '__main__':
    shell()