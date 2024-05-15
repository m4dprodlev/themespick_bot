import sqlite3
import datetime as dt
from datetime import datetime, timedelta

class Database_Users:

    def __init__(self):
        self.conn = sqlite3.connect('./db/database.db', check_same_thread=False)


    def create_table(self):
        cursor = self.conn.cursor()
        cursor.execute("""create table if not exists users
        (chat_id integer, rdm_choice integer, num_pick integer, dnt_click integer, donate_total float, donate_count integer)
        """)  

    def check_user(self, chat_id):
        cursor = self.conn.cursor()
        data = cursor.execute('select * from users where chat_id=?', [chat_id]).fetchall()
        return data == []

    def add_user(self, chat_id):
        cursor = self.conn.cursor()
        cursor.execute("insert into users (chat_id, rdm_choice, num_pick, dnt_click, donate_total, donate_count) values (?, ?, ?, ?, ?, ?)", [chat_id, 0, 0, 0, 0.0, 0])
        self.conn.commit()     

    def update_rdm_choice(self, chat_id):
        cursor = self.conn.cursor()
        cursor.execute('update users set rdm_choice=rdm_choice+1 where chat_id=?', [chat_id]).fetchall()
        self.conn.commit()     

    def update_num_pick(self, chat_id):
        cursor = self.conn.cursor()
        cursor.execute('update users set num_pick=num_pick+1 where chat_id=?', [chat_id]).fetchall()
        self.conn.commit()    

    def update_dnt_click(self, chat_id):
        cursor = self.conn.cursor()
        cursor.execute('update users set dnt_click=dnt_click+1 where chat_id=?', [chat_id]).fetchall()
        self.conn.commit()    

    def update_donate_count(self, chat_id):
        cursor = self.conn.cursor()
        cursor.execute('update users set donate_count=donate_count+1 where chat_id=?', [chat_id]).fetchall()
        self.conn.commit()    

    def update_donat_total(self, chat_id, amount):
        cursor = self.conn.cursor()
        cursor.execute('update users set donate_total=donate_total+? where chat_id=?', [amount, chat_id]).fetchall()
        self.conn.commit()    