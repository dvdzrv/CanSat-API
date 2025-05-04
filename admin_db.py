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
                 "sensor": row[1],
                 "data_type": row[2],
                 "value": row[3],
                 "time": row[4]
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
        """CREATE TABLE IF NOT EXISTS data (data_id INTEGER PRIMARY KEY, sensor TEXT NULL, data_type TEXT NULL, value TEXT NULL, time TIMESTAMP DEFAULT CURRENT_TIMESTAMP);"""
    )


    db_con.commit()
    db_con.close()



##Reinicialazion of tables
def reinit_db():
    os.remove("db/data.db")
    init_db()


def input_data_to_db(sensor: str, data_type: str, value: str):
    query_db(
        f"""INSERT INTO data (sensor, data_type, value) values ('{sensor}', '{data_type}', '{value}');"""
    )



def data_list_all():
    return query_db(
        f"""SELECT * FROM data"""
    )


def data_list_by_id(id):
    return query_db(
        f"""SELECT * FROM data WHERE data_id ={id}"""
    )[0]


if __name__ == "__main__":
    init_db()