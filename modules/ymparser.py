import config
import urllib.parse as query
import requests
import json
import modules.artists as Artists

def get_music_data(url, **kwargs):
    headers = {
        "Cookie": "L=Q2wDel9xdVoEeVRlQWZWelYOCAxpQ09EejkFJR0jJAwOM1giAA==.1537519857.13630.368393.78cb2cf7e0cb62e45c83501c1319d7b6;",
        "Accept-Encoding": "gzip, deflate, br",
        "X-Retpath-Y": "https://music.yandex.ru/",
        "Accept-Language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36",
        "X-Current-Uid": "167208532",
        "Accept": "application/json, text/javascript, */*; q=0.01",
        "Referer": "https://music.yandex.ru/",
        "X-Requested-With": "XMLHttpRequest",
        "Connection": "keep-alive"
    }

    if kwargs["headers"]:
        headers = {**headers, **kwargs["headers"]}

    r = requests.get(url + "&dir=&lang=ru&external-domain=music.yandex.ru&overembed=false", headers=headers)
    response = r.json()
    return response


def get_artist_list(page: int):
    params = {
        'id': 'музыка всех жанров',
        'page': page,
        'tab': 'artists',
        'sortBy': 'popular'
    }
    params = query.urlencode(params)
    url = config.parse_url + config.parse_artists_url + "?" + params

    text = query.urlencode({"музыка всех жанров": ""})[:-1]
    refer_url = config.parse_genre_url + text + "/artists?page=" + str(page)
    headers = {
        "Refer": refer_url,
        "X-Retpath-Y": refer_url
    }
    return get_music_data(url, headers=headers)


def parse_info():
    return None


def parse_artists():
    """
    Парсит весь список артистов
    :return:
    """
    page = 0

    while True:

        list_artists = get_artist_list(page)

        try:
            artists = list_artists["metatag"]["artists"]
        except KeyError:
            break

        Artists.save_artists_page(artists)

        # print(json.dumps(artists))
        page += 1
