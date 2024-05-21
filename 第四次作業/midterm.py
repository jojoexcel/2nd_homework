import pack.modu as lib
import os
import sqlite3

db_path = 'library.db'

# 檢查DB 是否存在
if os.path.exists(db_path):
    #存在
    conn = sqlite3.connect(db_path)

else:
   #不在在
