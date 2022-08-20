a = "abcdefg"
data  = ''
for i in a:
    with open(f"kaggle_dataset/xa{i}", "r") as f:
        data += f.read()

with open("kaggle_RC_2019-05.csv" , "w") as f:
    f.write(data)