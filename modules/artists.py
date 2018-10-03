import modules.db as db
import json
import time


def save_artists_page(artist_list):
    for a in artist_list:
        artist = a["artist"]
        data = {
            "name": artist["name"],
            "available": 1 if artist["available"] else 0 ,
            "links": json.dumps(artist["links"]),
            "genres": ', '.join(artist["genres"]),
            "date_update_parse": int(time.time())
        }


        if check_artist(artist["id"]):
            update_user(artist["id"], data)
        else:
            data['ym_artist_id'] = artist["id"]
            insert_user(data)


def check_artist(artist_id: int):
    connection = db.get_connection()
    with connection.cursor() as cursor:
        sql = "SELECT id FROM `artists` WHERE ym_artist_id='"+artist_id+"'"
        cursor.execute(sql)

        return cursor


def update_user(artist_id, data):
    connection = db.get_connection()
    with connection.cursor() as cursor:
        kv_list = ["{0}='{1}'".format(k, v) for k, v in data.items()]
        sql = "UPDATE `artists` SET "+", ".join(kv_list)+" WHERE ym_artist_id='"+artist_id+"'"
        cursor.execute(sql)
        connection.commit()


def insert_user(data):
    connection = db.get_connection()
    with connection.cursor() as cursor:
        keys = data.keys()
        values = data.values()
        kv_list = ["{0}='{1}'".format(k, v) for k, v in (keys, values)]
        sql = "INSERT INTO `artists` SET "+", ".join(kv_list)
        cursor.execute(sql)
        connection.commit()
