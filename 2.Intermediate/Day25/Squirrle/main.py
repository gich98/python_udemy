import pandas

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

colors = ["Gray", "Cinnamon", "Black"]
count = []

for color in colors:
    num_squirrels = len(data[data["Primary Fur Color"] == color])
    count.append(num_squirrels)


squirrels_dict = {"Fur Color": colors, "Count": count}

print(squirrels_dict)

squirrels_dataframe = pandas.DataFrame(squirrels_dict)
squirrels_dataframe.to_csv("squirrel_count.csv")
