# with open("weather_data.csv") as data_file:
#    data = data_file.readlines()
#    print(data)

# import csv

# with open("weather_data.csv") as data_file:
#    data = csv.reader(data_file)
#    temperatures = []
#    for row in data:
#        if row[1] != "temp":
#           temperatures.append(int(row[1]))
#        print(row[1])

import pandas

#data = pandas.read_csv("weather_data.csv")

#data_dict = data.to_dict()
#print(data_dict)

#temperatura_list = data["temp"]
#step_1 = 0
#counter = 0
#for temp in temperatura_list:
#    step_1 += int(temp)
#    counter += 1
#avg = step_1/counter
#(f"The average is: {avg}")

#print(temperatura_list)

#temperatura_list = data["temp"].to_list()
#avg = sum(temperatura_list) / len(temperatura_list)
#print(avg)

#temperatura_list = data["temp"].to_list()
#print(data["temp"].mean())

#temperatura_list = data["temp"].to_list()
#print(data["temp"].max())

#print(data["condition"])
#print(data.condition)

#print(data[data.day == "Monday"])

#print(data[data.day == "Monday"])
#print(data[data.temp == data.temp.max()])

#monday = data[data.day == "Monday"]
#print(monday.condition)

#monday = data[data.day == "Monday"]
#monday_temp = monday.temp[0]
#monday_temp_F = monday_temp * 9/5 + 32
#print(monday_temp_F)

#data_dict = {
#    "students": ["Ana", "Lebron", "Curry"],
#    "scores": [50, 60,80]
#}

#data = pandas.DataFrame(data_dict)
#data.to_csv("new_data.csv")
#print(data)
#counter = 0
data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data_20231014.csv")
gray_squirrels_list = len(data[data["Primary Fur Color"] == "Gray"])
red_squirrels_list = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_squirrels_list = len(data[data["Primary Fur Color"] == "Black"])
print(gray_squirrels_list)
print(red_squirrels_list)
print(black_squirrels_list)

data_dict = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [gray_squirrels_list, red_squirrels_list, black_squirrels_list]
}

data_to_new_file = pandas.DataFrame(data_dict)
data_to_new_file.to_csv("New_amount_of_each_color_squirrel.csv")

#for c in squirrels_list:
#    if c == "Gray":
#       counter += 1

#print(counter)





