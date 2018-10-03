import pymysql.cursors
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
    # Подключиться к базе данных.
    connection = pymysql.connect(host='localhost',
                                 user='analytic',
                                 password='CzeY3YOW9lzk71D3',
                                 db='yandex_data',
                                 charset='utf8mb4',
                                 cursorclass=pymysql.cursors.DictCursor)

    print("connect successful!!")

    with connection.cursor() as cursor:
        # SQL
        sql = "SELECT id FROM artist WHERE ym_artist_id='%s'"

        # Выполнить команду запроса (Execute Query).
        cursor.execute(sql, id)

        print("cursor.description: ", cursor.description)

        print()

        for row in cursor:
            print(row)


def update_user():
    pass


def insert_user():
    pass
