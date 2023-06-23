prompt = input("Greeting: ")

def check(param):
    param = param.strip().lower()

    if param.startswith("hello"):
        print("$0")
    elif param.startswith("h"):
        print("$20")
    else:
        print("$100")

check(prompt)