import csv

all_articles = []

with open(r"E:\avi\whitehatjr\multi_language\movie_recommendation\flask-mockup-2\p\project-c-142-main\articles.csv", encoding="utf8") as f:
    reader = csv.reader(f)
    data = list(reader)
    all_articles = data[1:]

liked_articles = []
not_liked_articles = []
