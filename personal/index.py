# File I/O --> Write
print("Enter 0000 to stop prompts")
while True:
    prompt = input("Enter Text: ")
    
    if prompt == "0000":
        break
    else:
        with open("personal/file.txt", "a") as file:
            file.write(f"{prompt} \n")