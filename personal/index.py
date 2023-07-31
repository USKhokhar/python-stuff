class Details:
    def __init__(self, name, relation):
        self.name = name
        self.relation = relation

def main():
    details = getDetails()
    print(f"{details.name} is the {details.relation}")

def getDetails():
    name = input("Enter Name: ")
    relation = input("Enter Relation: ")
    return Details(name, relation)

if __name__ == "__main__":
    main()

# OUTPUT
# Enter Name: Peter 
# Enter Relation: STUD
# Peter is the STUD