import mysql.connector


def save_artists_page(artist_list):
    for a in artist_list:
        artist = a["artist"]

