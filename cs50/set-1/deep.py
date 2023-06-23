question = "What is the Answer to the Great Question of Life, the Universe, and Everything?  "
prompt = input(question)

def check(param):
    param = param.lower().replace(" ", "").replace("-", "")
    if param == "42" or param == "fortytwo":
        print("Yes")
    else:
        print("No")

check(prompt)