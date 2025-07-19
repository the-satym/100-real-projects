import requests
import time
import sqlite3

movie_data= []
def get_movie_info(movie_name):
    url= f"https://www.omdbapi.com/?t={movie_name}&apikey=67a9323a"
    res= requests.get(url).json()

    imdb_rating = None
    for rating in res.get("Ratings", []):
        if rating.get("Source") == "Internet Movie Database":
            imdb_rating = (rating.get("Value").rstrip("/10"))
            break

    return {
        "Title": res.get("Title"),
        "Rated": res.get("Rated"),
        "Released": res.get("Released"),
        "Runtime": res.get("Runtime"),
        "Genre": res.get("Genre"),
        "Director": res.get("Director"),
        "Writer": res.get("Writer"),
        "Actors": res.get("Actors"),
        "Plot": res.get("Plot"),
        "Language": res.get("Language"),
        "Country": res.get("Country"),
        "imdb_rating": imdb_rating,
        "Type": res.get("Type"),
        "BoxOffice": res.get("BoxOffice"),
    }

info=get_movie_info("Inception")

#save it in database
def save_to_db(movie_info):
    connection = sqlite3.connect('movies.db')
    c = connection.cursor()

    c.execute('''CREATE TABLE IF NOT EXISTS movie_db(
        Title TEXT,
        Rated TEXT,
        Released TEXT,
        Runtime TEXT,
        Genre TEXT,
        Director TEXT,
        Writer TEXT,
        Actors TEXT,
        Plot TEXT,
        Language TEXT,
        Country TEXT,
        imdb_rating REAL,
        Type TEXT,
        BoxOffice TEXT
    )''')

    c.execute('''INSERT INTO movie_db(
        Title, Rated, Released, Runtime, Genre,
        Director, Writer, Actors, Plot, Language,
        Country, imdb_rating, Type, BoxOffice)
        VALUES (:Title, :Rated, :Released, :Runtime, :Genre,
        :Director, :Writer, :Actors, :Plot, :Language,
        :Country, :imdb_rating, :Type, :BoxOffice)''',movie_info)
    connection.commit()
    connection.close()
save_to_db(info)
print("Data saved to database successfully.")