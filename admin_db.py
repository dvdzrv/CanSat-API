import sqlite3
import os
from types import NoneType


#DB ACCESS
##QUERY DB
def query_db(query: str):
    db_con = sqlite3.connect('db/data.db')
    db_cursor = db_con.cursor()
    db_cursor.execute(query)
    rows = db_cursor.fetchall()
    db_con.commit()
    db_con.close()
    return rows



def construct_data(row):
    if not row:
        return None
    return {"data_id": row[0],
                 "message": row[1],
                 "time": row[2]
               }


def construct_data_list(rows):
    if not rows:
        return []
    parts = []
    for row in rows:
        parts.append(construct_data(row))
    return parts


#DB TABLE HANDLING
##INICIALIZATION OF TALBLES
def init_db():
    db_con = sqlite3.connect('db/data.db')
    db_cursor = db_con.cursor()

    db_cursor.execute(
        """CREATE TABLE IF NOT EXISTS data (data_id INTEGER PRIMARY KEY, message TEXT NULL, time TIMESTAMP DEFAULT CURRENT_TIMESTAMP);"""
    )


    db_con.commit()
    db_con.close()



##Reinicialazion of tables
def reinit_db():
    os.remove("db/data.db")
    init_db()


def input_data_to_db(message: str):
    message = str(message).replace("'", "\"")

    query_db(
        f"""INSERT INTO data (data_id, message) VALUES(NULL, '{message}');"""
    )



def data_list_all():
    return construct_data_list( query_db(
        f"""SELECT * FROM data"""
        )
    )

def data_list_by_id(id: int):
    return construct_data( query_db(
        f"""SELECT * FROM data WHERE data_id = {id}"""
        )[0]
    )
def data_list_latest():
    return construct_data( query_db(
        f"""SELECT * FROM data ORDER BY data_id DESC LIMIT 1"""
        )[0]
    )

if __name__ == "__main__":
    init_db()