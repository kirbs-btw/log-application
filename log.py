import datetime
import tkinter as tk
from tkinter import ttk
import sqlite3

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

def add_to_log(logEntry, logTextbox):
    content = logEntry.get()
    logEntry.delete(0, 9999999)
    print(content)

    now = datetime.datetime.now()
    time = now.strftime("%H:%M:%S")
    date = datetime.date.today()

    command = 'INSERT INTO log VALUES("{}", "{}", "{}")'.format(date, time, content)
    print(command)

    conn.execute(command)

    logText = "{} {} {}\n".format(date, time, content)
    logTextbox.insert(tk.END, logText)

def insert(textBox):
    textBox.delete('1.0', tk.END)
    command = 'SELECT * FROM log'
    entry = conn.execute(command).fetchall()
    for log in entry:
        text = "{} {} {}\n".format(log[0], log[1], log[2])
        textBox.insert(tk.END, text)

def main():
    root = tk.Tk()

    canvas = tk.Canvas(root, height=800, width=800)
    canvas.pack()

    logEntry = tk.Entry(canvas)
    logEntry.place(relx=0.025, rely=0.9, relwidth=0.85, relheight=0.03)

    logTextbox = tk.Text(canvas, bg="#ffffff", height=2, width=30)
    logTextbox.place(relx=0.025, rely=0.025, relwidth=0.95, relheight=0.7)

    addButton = tk.Button(canvas, text="add", command=lambda: add_to_log(logEntry, logTextbox))
    addButton.place(relx=0.9, rely=0.9)

    getLog = tk.Button(canvas, text="get", command=lambda: insert(logTextbox))
    getLog.place(relx=0.94, rely=0.025)

    insert(logTextbox)

    root.mainloop()


if __name__ == '__main__':
    main()
