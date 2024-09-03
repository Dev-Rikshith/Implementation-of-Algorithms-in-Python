def binary_search(myList, low, high, target):
    if high >= low:
        mid = (high + low) // 2
        
        if myList[mid] == target:
            return mid
        elif myList[mid] > target:
            return binary_search(myList, low, mid - 1, target)
        else:
            return binary_search(myList, mid + 1, high, target)
    else:
        return -1  # Target not found

def main():
    myList = [2, 3, 4, 10, 40]
    target = 10
    
    
    index = binary_search(myList, 0, len(myList) - 1, target)
    
    if index != -1:
        print(f"Element found at index {index}")
    else:
        print("Element not found in the list")

if __name__ == "__main__":
    main()
