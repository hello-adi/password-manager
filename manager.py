from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
import os
import csv

# TODO 1. add encryption function, 2. connect to db 3. general flow
# get add or view argument as cli argument with the master password

# get password

# ecrypt takes data and uses the aes module to encrypt
# store key with the database to decrypt the password
# store cipher.nonce to verify?


def encrypt(user_password):
    # Using bytes(str, enc)
    # convert string to byte form
    byte_string = bytes(user_password, "utf-8")
    key = get_random_bytes(16)  # must be 16, 24 or 32 bytes long
    # aes constructor which takes in key and optional mode
    cipher_obj = AES.new(key, AES.MODE_EAX)
    encrypted_password, tag = cipher_obj.encrypt_and_digest(byte_string)
    nonce = cipher_obj.nonce

    # return whatever is encrypted


# add will ask for the name of service
# ask user for password
# encode it (diff function)
# add it to the db

# decrypt to get the 1.service from the database
# the key, the password and the tag
# decrypts the password using the key
# verifies the password using the tag
# then showcases it to the user.

def decrypt(key, encrypt_pass, tag, nonce):
    cipher_obj = AES.new(key, AES.MODE_EAX, nonce)
    decoded_password = cipher_obj.decrypt_and_verify(encrypt_pass, tag)

    # return decoded password

# check if db is empty so don't add headers everytime
def add():
    website = input("enter name of service")
    password = input("enter password")

    data = [website, password]
    header = ["Website", " password\n"]

    # encrypt the website and password
    # call encrypt function with data[1] as parameter
    # encrypt(data[1])
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
