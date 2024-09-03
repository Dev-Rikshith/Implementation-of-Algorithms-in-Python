def linear_search(myList, key):
    for i in range(len(myList)):
        if(myList[i]==key):
            return i+1
    return -1
        

def main():
    list = [3,7,6,5,4]
    index = linear_search(list, 3)
    if index == -1: 
        print("Element not found") 
    else: 
        print(index)
   
        

if __name__ == "__main__":
    main()

