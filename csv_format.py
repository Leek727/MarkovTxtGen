import pandas as pd

df = pd.read_csv("kaggle_RC_2019-05.csv", on_bad_lines='skip')
saved_column = df['body']

data = ""
for row in saved_column:
    if type(row) == type("a"):
        data += '\n '+ row

with open("formatted.txt", "w") as f:
    f.write(data)