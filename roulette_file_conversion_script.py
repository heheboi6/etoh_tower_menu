import os
file_name = ""
while not os.path.exists(file_name):
    if file_name != "":
        print("This file doesn't exist. Please try again.")
    file_name = input("Enter file name: ")
times_beaten = 0
while times_beaten <= 0:
    if times_beaten != 0:
        print("The number of times that you have to beat a tower must be greater than 0.")
    try:
        times_beaten = int(input("How many times you have to beat a tower to be eliminated: "))
    except ValueError:
        print("The number of times that you have to beat a tower must be a number.")
file_string = ""
with open(file_name, "r") as file:
    total_data = file.readlines()
    for line in total_data:
        data = line.split(" ")
        if len(data) < 2:
            data[0] = data[0].replace("\n", "")
            file_string += f"{data[0]} 0/{times_beaten}\n"
        else:
            file_string += f"{line}"
with open(f"new_{file_name}", "w") as file:
    file.write(file_string)
    file.close()