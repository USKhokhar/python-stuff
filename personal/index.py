class GriffinTester():
    def __init__(self, name):
        if name not in ["peter", "louis", "meg", "chris", "brian", "stewie"]:
            raise ValueError("Not A Griffin!")
        self.name = name
    def __str__(self):
        return "Griffin Spotted!"

def main():
    griffin = getGriffin()
    print(griffin)

def getGriffin():
    name = input("Enter Name: ")
    return GriffinTester(name)

if __name__ == "__main__":
    main() 