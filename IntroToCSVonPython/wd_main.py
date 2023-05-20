import csv
import pandas

data = pandas.read_csv("weather_data.csv")
#print(data["condition"])

data_dict = data.to_dict()
print(data_dict)

temp_data = data["temp"].to_list()

print(data[data.temp == data.temp.max()])



