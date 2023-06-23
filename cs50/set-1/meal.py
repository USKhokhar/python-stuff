def main():
    prompt = input("What time it is? ")
    result = convert(prompt)

    print(result)

def convert(time):
    time = time.replace(":", ".")
    time = float(time)

    if 7 <= time <= 8:
        return "breakfast time"
    elif 12 <= time <= 13:
        return "lunch time"
    elif 18 <= time <= 19:
        return "dinner time"
    else:
        return 


if __name__ == "__main__":
    main()