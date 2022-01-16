from tabulate import tabulate as table

your_data = []


choice = input("Open previous data?\n**If no previous data is found you will be directed to a new chart**\n (yes/no): ")
if choice == "no":
    mode = "w"
else:
    mode = "a"



#append data into list

def open_data():
    with open("file_1.txt",mode="r") as file:
        open_list = file.readlines()
        for i,v in enumerate(open_list):
            open_list=v.split()
            your_data.append(open_list)

def make_data():
    global mode
    create_list = input("Enter your data:\n(enter as a row with a single space seperating the data)")
    create_list = f"{create_list}\n"

    with open("file_1.txt", mode=mode) as file:
        file.writelines(create_list)
        mode= "a"


if choice:
    heads = input("Input the Categories for your chart: ")
    header = heads.split()
    rows = int(input('How Many Rows: '))

    for i in range(rows):
        make_data()
        open_data()
    print(table(your_data, header, "grid"))



input("Press enter to exit")



























