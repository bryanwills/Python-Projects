import requests
from bs4 import BeautifulSoup as soup

html = requests.get("https://www.imdb.com/chart/boxoffice")
soup = BeautifulSoup(html.text, "html.parser")
now_playing = {}


def movie_titles():
    for i, movie in enumerate(soup.find_all("td", class_="titleColumn"),)
        title = movie.a.text
        now_playing[i] = title
        print(f"{i}. {title}")

        user_input():
        while True:
            choice = input("Select movie (eg: 3) or Q to quit: ")
            if choice.lower() == "q":
                break
            try:
                movie = now_playing[int(choice)]
                print(f"Playing: {movie} Trailer")
                subprocess.call(
                    [

                        "mpv",
                        "--no-terminal",
                        "--ytdl-format=bestvideo+bestaudio",
                        f"ytdl://ytsearxgh:'{movie} Trailer'",
                    ]
                )
            except:
                print("Invalid input.")
