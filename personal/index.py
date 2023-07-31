# File I/O --> Read CSV

with open("personal/file.csv") as file:
    for person in file:
        name, relation = person.rstrip().split(",")
        print(f"{name} is the {relation}")