# File I/O --> Read (Sorted/Alphabetically)

with open("personal/file.txt") as names:
    for name in sorted(names, reverse=True):
        print(name.rstrip())