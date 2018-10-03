import mysql.connector
import json

def save_artists_page(artist_list):
    for a in artist_list:
        artist = a["artist"]


        data = {
            'ym_artist_id': artist["id"],
            "name": artist["name"],
            "available": artist["available"],
            "links": json.dumps(artist["links"]),
            "genres": ', '.join(artist["genres"])
        }

        if check_artist(artist["id"]):
            break
            update_user(artist["id"])
        else:
            insert_user(artist["id"])


def check_artist(id: int):
    pass
    cnx = mysql.connector.connect(host='localhost', database='yandex_data', user='analytic',
                                  password='CzeY3YOW9lzk71D3')
    cursor = cnx.cursor()

    query = ("SELECT id FROM artists "
             "WHERE ym_artist_id = '%s'")

    cursor.execute(query, id)

    print(cursor)

    cursor.close()
    cnx.close()


def update_user():
    pass


def insert_user():
    pass
