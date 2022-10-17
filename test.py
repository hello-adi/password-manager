from requests import head


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
