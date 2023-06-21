def main():
    cost = dollars_to_float(input("How much was the meal? "))
    tip_percentage = percent_to_float((input("What percentage would you like to tip? ")))
    tip = cost * tip_percentage

    print(f"Total tipping amount: ${tip:.2f} ")

def dollars_to_float(d):
    return float(d[1:])

def percent_to_float(d):
    return float(d[:-1]) / 100

main()