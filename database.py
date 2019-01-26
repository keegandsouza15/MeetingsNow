# Python SQLite Database wrapper file.

import sqlite3
import uuid




def insert_meeting(name, date, time, location, description):
    id = str(uuid.uuid1())
    if len(name) == 0:
        raise ValueError
    if len(date) == 0:
        raise ValueError
    meeting = [(id, name, date, time, location, description)]
    
    with sqlite3.connect("C:\\Users\\Keegan\\Desktop\\dbFolder\\meetings.db") as conn:
        cursor = conn.cursor()
        cursor.executemany("INSERT INTO meetings VALUES(?, ?, ?, ?, ?, ?)", meeting)
        conn.commit()
        return id

def get_meeting(id):
    t = (id,)
    conn = sqlite3.connect("C:\\Users\\Keegan\\Desktop\\dbFolder\\meetings.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM meetings WHERE ID=?" , t)
    return cursor.fetchone()



if __name__ == "__main__":
    try:
        id = insert_meeting("This is another test", "Hello", "01/13/12", "1957 Avanti Way", "This is a test")
    except Exception as e:
        print("There was an error inserting into the database")

    try:
        meeting = get_meeting(id)
    except Exception:
        print("Cannot get meeting")


