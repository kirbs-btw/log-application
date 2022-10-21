import datetime
import tkinter as tk
from tkinter import ttk
import sqlite3

def add_to_log(logEntry):
    conn = sqlite3.connect("log.sql")
    cur = conn.cursor()

    content = logEntry.get()
    logEntry.delete(0, 9999999)
    print(content)

    now = datetime.datetime.now()
    time = now.strftime("%H:%M:%S")
    date = datetime.date.today()

    command = 'INSERT INTO log VALUES("{}", "{}", "{}")'.format(date, time, content)
    print(command)

    cur.execute(command)
    conn.commit()
    conn.close()


def main():
    root = tk.Tk()

    canvas = tk.Canvas(root, height=800, width=800)
    canvas.pack()

    logEntry = tk.Entry(canvas)
    logEntry.place(relx=0.1, rely=0.9, relwidth=0.7, relheight=0.03)

    addButton = tk.Button(canvas, text="add", command=lambda: add_to_log(logEntry))
    addButton.place(relx=0.8, rely=0.9)



    root.mainloop()


if __name__ == '__main__':
    main()
