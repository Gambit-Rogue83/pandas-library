import csv
import pandas


# with open("weather_data.csv") as forecast:
#     daily = csv.reader(forecast)
#     temperatures = []
#     for row in daily:
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))
#
#
# print(temperatures)

# data = pandas.read_csv("weather_data.csv")
# print(data["temp"])
#
# data_dic = data.to_dict()
# print(data_dic)

# temp_list = data["temp"].to_list()

# print(data.temp.max())
#
# print(data[data.temp == data.temp.max()])

#Get data in row
# monday = data[data.day == "Monday"]
# print(monday.temp *(9/5) + 32)

#Create a dataframe
# data_dict = {
#     "students": ["Joseph", "Zeke", "Polly"],
#     "scores": [69, 78, 87]
# }
#
# data = pandas.DataFrame(data_dict)
# print(data)
# data.to_csv("new_data.csv")

squirrel_data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data_20240429.csv")

# black_squirrel = len(squirrel_data[squirrel_data["Primary Fur Color"] == "Black"])


squirrel_dic = {
        "Fur Color": ["Gray", "Cinnamon", "Black"],
        "Count": [0, 0, 0]
    }

for color in squirrel_data["Primary Fur Color"]:
    if color == "Gray":
        squirrel_dic["Count"][0] += 1
    elif color == "Cinnamon":
        squirrel_dic["Count"][1] += 1
    elif color == "Black":
        squirrel_dic["Count"][2] += 1
    else:
        pass

squirrel_count = pandas.DataFrame(squirrel_dic)
squirrel_count.to_csv("squirrel_count.csv")

# print(squirrel_dic)

# squirrel_count = pandas.DataFrame(squirrel_dic)
# squirrel_count.to_csv("squirrel_count.csv")