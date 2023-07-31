# File I/O --> Read (Sorted/Ascending)

with open("personal/file.txt") as names:
    for name in sorted(names):
        print(name.rstrip())