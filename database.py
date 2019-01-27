# Python SQLite Database wrapper file.

import sqlite3
import uuid


def get_all_comments(chat_id):
    chat = (chat_id, )
    with sqlite3.connect("C:\\Users\\Keegan\\Desktop\\dbFolder\\meetings.db") as conn:
        cursor = conn.cursor()
        cursor.execute(""" SELECT comment \
                               FROM COMMENTS CM\
                               JOIN CHATS C \
                               on c.ID == cm.CHAT_ID \
                               WHERE cm.CHAT_ID=?""", chat)
        item = cursor.fetchall()
        return item


def insert_comment(chat_id, comment):
    if len(comment) == 0:
        raise ValueError
    comment = [(chat_id, comment)]
    with sqlite3.connect("C:\\Users\\Keegan\\Desktop\\dbFolder\\meetings.db") as conn:
        cursor = conn.cursor()
        cursor.executemany("INSERT INTO comments (chat_id, comment) VALUES(?, ?)", comment)
        conn.commit()



def insert_chat(meeting_id):
    if len(meeting_id) == 0:
        raise ValueError
    chat = [(meeting_id,)]
    with sqlite3.connect("C:\\Users\\Keegan\\Desktop\\dbFolder\\meetings.db") as conn:
        cursor = conn.cursor()
        cursor.executemany("INSERT INTO chats (meeting_id) VALUES(?)", chat)
        conn.commit()


def get_chat_id(meeting_id):
    if len(meeting_id) == 0:
        raise ValueError
    t = (meeting_id, )
    with sqlite3.connect("C:\\Users\\Keegan\\Desktop\\dbFolder\\meetings.db") as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM chats WHERE MEETING_ID=?", t)
        chat = cursor.fetchone()
        return chat[0]




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


def comment_test():
    try:
        insert_comment(3, "Hello There")
    except Exception as e:
        print(str(e))
    try:
        get_all_comments(4)
    except Exception as e:
        print(str(e))



if __name__ == "__main__":
    comment_test()
    # try:
    #     id = insert_meeting("This is another test", "Hello", "01/13/12", "1957 Avanti Way", "This is a test")
    #     insert_chat(id)
    #     print(get_chat_id(id))
    # except Exception as e:
    #     print(str(e))
    #
    # try:
    #     meeting = get_meeting(id)
    # except Exception:
    #     print("Cannot get meeting")


