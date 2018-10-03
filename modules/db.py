import pymysql.cursors


def get_connection():
    connection = pymysql.connect(host='localhost',
                                 user='analytic',
                                 password='CzeY3YOW9lzk71D3',
                                 db='yandex_data',
                                 charset='utf8mb4',
                                 cursorclass=pymysql.cursors.DictCursor)

    return connection

