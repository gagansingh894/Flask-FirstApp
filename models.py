import sqlite3
from os import path

ROOT = path.dirname(path.relpath(__file__))

def create_post(name, content):
    conn = sqlite3.connect(path.join(ROOT, 'database.db'))
    c = conn.cursor()
    c.execute('INSERT INTO posts (name, content) VALUES(?, ?)', (name, content))
    conn.commit()
    conn.close()

def get_posts():
    conn = sqlite3.connect(path.join(ROOT, 'database.db'))
    c = conn.cursor()
    c.execute('SELECT * FROM posts')
    posts = c.fetchall()
    return posts


