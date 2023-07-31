def main():
    while True:
        try:
            steps = int(input("Number of steps: "))
            pyramid(steps)
            break
        except ValueError:
            print("Enter an integer please")


def pyramid(steps):
    for i in range(1, steps):
        print(" * " * i)

main()