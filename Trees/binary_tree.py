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
        if self is None:
            return False
        
        if self.val == target:
            return True
        
        return (self.left.tree_includes_recursive(target) if self.left else False) or (self.right.tree_includes_recursive(target) if self.right else False)

    def tree_sum(self):
        if self is None:
            return 0
        
        return self.val + (self.left.tree_sum() if self.left else 0) + (self.right.tree_sum() if self.right else 0)

if __name__ == "__main__":
    # a = Node("a")
    # b = Node("b")
    # c = Node("c")
    # d = Node("d")
    # e = Node("e")
    # f = Node("f")

    # a.left = b
    # a.right = c
    # b.left = d
    # b.right = e
    # c.right = f

    a = Node(3)
    b = Node(11)
    c = Node(4)
    d = Node(4)
    e = Node(2)
    f = Node(1)

    a.left = b
    a.right = c
    b.left = d
    b.right = e
    c.right = f



    print(a.tree_sum())

    #     a   
    #    /  \
    #    b   c
    #     /\  \
    #     d e  f