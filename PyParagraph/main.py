#importing libraries
import os

#asking the user for the path and name of the file to be analyzed
print("============================================")
print("|                                          |")
print("|  Welcome to the paragraph analysis tool  |")
print("|                                          |")
print("============================================")
file = input("What's the name of the file you want to analyze? (in Resources folder):")

txtpath = os.path.join('Resources', file)
#checking if the file exists
file_exists = False
while file_exists == False:
    file_exists = os.path.exists(txtpath)
    if file_exists == False:
        file = input("Error: file doesn't exist, make sure it's on the /Resources folder and is typed correctly:")
        txtpath = os.path.join('Resources', file)


