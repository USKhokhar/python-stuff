# LINEAR SEARCH

def linear_search(arr, target):
    for index, item in enumerate(arr):
        if item == target:
            return index
    return 1

listx = [1,2,3,4,5,6,7]
my_target = int(input("Enter the number to be found: "))

flag = linear_search(listx, my_target)

if flag != 1:
    print(f"{my_target} found at index {flag}")
elif flag == 1:
    print(f"{my_target} not present in list!")
else:
    print(f"Some error occured!")