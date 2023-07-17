def binary_search(arr, target, high, low):
    while low <= high:
        mid = (low+high)//2
        if arr[mid] == target:
            return mid
        elif arr[mid] > target:
            high = mid -1
        else: 
            low = mid + 1
    return -1

listx = [1,2,3,4,5,6]
my_target = int(input("Enter element to be found: "))

flag = binary_search(listx, my_target, len(listx)-1, 0)

if flag != -1:
    print(f"{my_target} found at index {flag}")
else:
    print("Not found!")