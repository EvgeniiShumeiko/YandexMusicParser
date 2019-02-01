import pymysql.cursors


def get_connection():
    connection = pymysql.connect(host='localhost',
                                 user='user',
                                 password='pass',
                                 db='yandex_data',
                                 charset='utf8mb4',
                                 cursorclass=pymysql.cursors.DictCursor)

    return connection

