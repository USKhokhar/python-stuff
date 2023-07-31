# File I/O --> Read (Unsorted)

with open("personal/file.txt") as names:
    for name in names:
        print(name.rstrip())