prompt = input("File name: ")

def check_extension(param):
    param = param.lower().split(".")

    if param[1] == "gif":
        print("image/gif")
    elif param[1] == "jpg" or param[1] == "jpeg":
        print("image/jpeg")
    elif param[1] == "png":
        print("image/png")
    elif param[1] == "pdf":
        print("application/pdf")
    elif param[1] == "txt":
        print("text/plain")
    elif param[1] == "json":
        print("application/json")
    elif param[1] == "zip":
        print("application/zip")
    else: 
        print("application/octet-stream")

check_extension(prompt)