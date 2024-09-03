class StackGenerator:
    def __init__(self, myList):
        self.myList = myList
    
    def __str__(self):
        return f"{myList}"
    
    def push(self,element):
        myList.append(element)

    def pop(self):
        return myList.pop()
    
    def peek(self):
        return myList[len(myList)-1]
    
   
if __name__ == "__main__":
    myList = [2,4,5,6,3,5]
    stack = StackGenerator(myList)
    print(stack.peek(), end=" ")
    print(stack.pop(), end=" ")
    print(stack.push(105), end=" ")
    print(stack)