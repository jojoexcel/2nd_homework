import os
import sqlite3
import json
import csv

dp_name='library.db'

def create_db():

    conn = sqlite3.connect(dp_name)
    create_table_users='''
    CREATE TABLE IF NOT EXISTS users (
    user_id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT NOT NULL,
    password TEXT NOT NULL
    )'''

    create_table_books='''
    CREATE TABLE IF NOT EXISTS books (
    book_id	 INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    author TEXT NOT NULL,
    publisher TEXT NOT NULL,
    year INTEGER NOT NULL
    )
    '''
    cursor = conn.cursor()
    cursor.execute(create_table_users)
    cursor.execute(create_table_books)
    conn.commit()
    conn.close()

def insert_users_from_csv(csv_file):
    '''从 CSV 文件中批量插入 users 数据'''
    df = pd.read_csv(csv_file)
    users = df.to_dict(orient='records')
    insert_users(users)

def insert_users(filers):
    conn = sqlite3.connect(dp_name)
    cursor = conn.cursor()

    # json to db
    # 安全的佔位符號寫法

    data = (vid, name, age)
    cursor.execute("INSERT INTO users (sid, name, age) VALUES (?, ?, ?)", data)
    # 還記得嗎？ 為何可省略欄位名稱？
    cursor.execute("INSERT INTO users VALUES (?, ?, ?)", ('001', 'John Smith', 18))
    conn.commit()
    conn.close()

def insert_user(username, password):
    '''insert into 資料表 users'''
    try:
        conn = sqlite3.connect('library.db')
        c = conn.cursor()
        c.execute("INSERT INTO users (username, password) VALUES (?, ?)",
                  (username, password))
        conn.commit()
    except sqlite3.Error as error:
        print(f"新增 users 作業發生錯誤：{error}")
    conn.close()


