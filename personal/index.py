class GriffinTester():
    def __init__(self, name):
        if name not in ["peter", "lois", "meg", "chris", "brian", "stewie"]:
            raise ValueError("Not A Griffin!")
        self.name = name
    def __str__(self):
        return "Griffin Spotted!"
    def checkRel(self): 
        match self.name:
            case "peter":
                return "family guy"
            case "lois":
                return "wife"
            case "chris":
                return "eldest son"
            case "stewie":
                return "youngest son"
            case "brian": 
                return "liberal son"
            case "meg":
                return "..."
            case _:
                return "Not a valid griffin!"

def main():
    griffin = getGriffin()
    print(griffin.checkRel())

def getGriffin():
    name = input("Enter Name: ")
    return GriffinTester(name,)

if __name__ == "__main__":
    main() 