# with open("weather_data.csv") as data_file:
#     data = data_file.readlines()
#     print(data)

# import csv
#
# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     for row in data:
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))
#     print(temperatures)

import pandas
import math

# df = pandas.read_csv("weather_data.csv")
# # print(df["temp"])
# #
# # data_dict = df.to_dict()
# # print(data_dict)
# #
# # temp_list = df["temp"].to_list()
# # print(temp_list)
# #
# # print(df["temp"].mean())
# # print(df["temp"].max())
# #
# # # Get data in columns
# # print(df["condition"])
# # print(df.condition)
#
# # Get data in row
# # print(df[df.day == "Monday"])
# # print(df[df.temp == df["temp"].max()])
#
# # temp_monday = df[df.day == "Monday"].temp
# # temp_monday = int(temp_monday) * 9/5 + 32
# # print(temp_monday)
#
# # Create a df from scratch
# data_dict = {
#     "students": ["Amy", "James", "Angela"],
#     "scores": [76, 56, 65]
# }
#
# data = pandas.DataFrame(data_dict)
# data.to_csv("new_data.csv")

df = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
grey_squirrels = len(df[df["Primary Fur Color"] == "Gray"])
red_squirrels = len(df[df["Primary Fur Color"] == "Cinnamon"])
black_squirrels = len(df[df["Primary Fur Color"] == "Black"])

data_dict = {
    "Fur Color": ["Grey", "Cinnamon", "Black"],
    "Count": [grey_squirrels, red_squirrels, black_squirrels]
}

data = pandas.DataFrame(data_dict)
data.to_csv("squirrel_count.csv")
