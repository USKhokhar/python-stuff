def main():
    prompt = input("Enter the prompted string: ")
    print("Converted Output: ", convert(prompt))

def change(string):
    string = string.replace(":(", "😔")
    string = string.replace(":)", "😇")

    return string


def convert(string):
    if ":(" and ":)" in string:
        string = change(string)
        return string
    elif ":(" in string:
        string = change(string)
        return string
    elif ":)" in string:
        string = change(string)
        return string
    else:
        return string

main()
