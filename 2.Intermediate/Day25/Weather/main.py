import pandas

data = pandas.read_csv("weather_data.csv")

print(data[data.temp == data.temp.max()])

monday = data[data.day == "Monday"]
# fahrenheit = (celsius * 1.8) + 32
print(f"{(int(monday.temp) * 1.8) + 32}")
