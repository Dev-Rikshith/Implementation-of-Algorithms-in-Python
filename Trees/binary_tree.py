class Node():
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

    # def __str__(self):
    #     print(self.val)

    def DFS(self):
        stack = []
        stack.append(self)
        while len(stack)!=0:
            current = stack.pop()
            print(current.val, end=" ")

            if(current.right):
                stack.append(current.right)
            if(current.left):
                stack.append(current.left)

    # def reDFS(self):
    #     # stack = []
    #     left_values = self.reDFS(self.left)
    #     right_values = self.reDFS(self.right)
    #     return self.val, left_values, right_values

    def BFS(self):
        queue = []
        queue.append(self)
        while(len(queue)!=0):
            current = queue.pop(0)
            print(current.val, end=" ")
            if(current.left):
                queue.append(current.left)
            if(current.right):
                queue.append(current.right)

    def tree_includes(self, target):
        queue = []
        queue.append(self)
        while(len(queue)!=0):
            current = queue.pop(0)
            if(current.val==target):
                return True
            if(current.left):
                queue.append(current.left)
            if(current.right):
                queue.append(current.right)

    def tree_includes_recursive(self, target):
        if(self.val == target):
            return True
        if(self == None):
            return False
        return self.tree_includes_recursive(self.right) or self.tree_includes_recursive(self.left)


if __name__ == "__main__":
    a = Node("a")
    b = Node("b")
    c = Node("c")
    d = Node("d")
    e = Node("e")
    f = Node("f")

    a.left = b
    a.right = c
    b.left = d
    b.right = e
    c.right = f

    if a.tree_includes_recursive("e"):
        print("Element found")

    #     a   
    #    /  \
    #    b   c
    #     /\  \
    #     d e  f