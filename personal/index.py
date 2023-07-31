while True:
    try:
        prompt = int(input("Enter: "))
        print(prompt)
        break
    except ValueError:
        pass