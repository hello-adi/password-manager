from Crypto.Cipher import AES
import os
import csv

# get add or view argument as cli argument with the master password

# get password

# add will ask for the name of service
# ask user for password
# encode it (diff function)
# add it to the db

# check if db is empty so don't add headers everytime
def add():

    website = input("enter name of service")
    password = input("enter password")

    data = [website, password]
    header = ["Website", " password\n"]

    with open("pass.txt", "a") as f:
        # f.writelines(header)
        f.write(data[0])
        f.write(" ")
        f.write(data[1])
        f.write("\n")


# view will ask the name of service
# search the database for the name
# get encrypted password
# decrypt it and display it
def view():
    website = input("enter name of service")

    with open("pass.txt", "a") as f:
        # f.writelines(header)
        f.write(data[0])
        f.write(" ")
        f.write(data[1])
        f.write("\n")


def input():
    master = input("password")
    # add or view
    choice = input("add or view password")
    if choice == "add":
        add()
    elif choice == "view":
        view()
