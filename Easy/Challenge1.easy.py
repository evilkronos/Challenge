import os, errno
#create a program that will ask the users name, age, and reddit username. have it tell them the information back, in the format:
#your name is (blank), you are (blank) years old, and your username is (blank)
#for extra credit, have the program log this information in a file to be accessed later.

def inputs():

    ageValid = 0
    name = input("Please enter your Name: ")
    while ageValid == 0:
        age = input("Please enter your Age: ")
        if age.isdigit():
            ageValid = 1
        else:
            print("The value " + age + " is not a valid age, please enter a numeric value for your Age")
            age = input("Please enter your Age: ")
    username = input("Please enter your Reddit username: ")

    outputdir = input("Please enter the directory you wish to output your answer to e.g. C:\output\: ")
    filename = input("Please enter the name of the .txt file you wish to create or write to e.g. output.txt: ")
    if not os.path.exists(outputdir):
        os.makedirs(outputdir)
    with open(outputdir + filename, "w+") as text_file:
     print("Your name is " + str(name) + ", you are " + str(age) + " years old, and your Reddit username is " + str(
         username) + ".", file=text_file)
     print("name = " + name, file=text_file)
     print("age = " + age, file=text_file)
     print("username = " + username, file=text_file)

    print("Output saved: " + outputdir + filename)

inputs()
