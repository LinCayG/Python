
#import csv

#with open("weather_data.csv") as data_file:
#    data = csv.reader(data_file) #creates a csv reader object
#    temperatures = []
#    for row in data:
#        if row[1] != "temp":
#            temperatures.append(int(row[1]))
#    print(temperatures)

#Easier to use the pandas library

import pandas

data = pandas.read_csv("weather_data.csv")
#print(data["temp"])

data_dict = data.to_dict() #converts to a dictionary
print(data_dict)

temp_list = data["temp"].to_list()
print(temp_list)
average = sum(temp_list) / len(temp_list)
print(average)

#Can find the average in a different way too
print(data["temp"].mean())

#Max temp
data["temp"].max()
print(data["temp"].max())

#Get Data in Columns: take the data frame, and specify the name of the column in the square brackets (default first row)
print(data["condition"])
#Make sure the string matches the name exactly - includes capitalization!
#You can also call them by an attribute - Pandas has created the columns as attributes:
print(data.condition)

#Get data in the rows of the data frame
print(data[data.day == "Monday"])

#Pull row of data where temperature is at the maximum
print(data[data.temp == max(data.temp)])
#or can do:
print(data[data.temp == data.temp.max()])

monday = data[data.day == "Monday"]
print(monday.condition)

#Get Monday's temperature in Farenheit:
monday_temp_F = monday.temp[0] * 9/5 +32
print(monday_temp_F)

#Create a dataframe from scratch:
data_dict = {
    "students": ["Amy", "James", "Angela"],
    "scores": [76, 56, 65]
}
#call Pandas and initialize the dataframe and choose your dictionary name above
New_data = pandas.DataFrame(data_dict)
print(New_data)
#Can make the data into a .csv file, just need the dataframe and the path where you want to save the csv.
New_data.to_csv("new_datafile.csv")



