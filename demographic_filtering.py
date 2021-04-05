import pandas as pd
import numpy as np

df = pd.read_csv(r'E:\avi\whitehatjr\multi_language\movie_recommendation\flask-mockup-2\p\project-c-142-main\articles.csv', encoding="utf8")

df = df.sort_values(['total_events'], ascending=[False])

output = df[["url", "title", "text", "lang", "total_events"]].head(20).values.tolist()