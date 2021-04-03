class Stack:
    def __init__(self):
        self.data = list()
        self.index = 0
    
    def getData(self):
        return self.data

    def append(self, item):
        self.data.append(item)
    
    def pop(self):
        return self.data.pop()



stack = Stack()
stack.append('A')
stack.append('B')
stack.append('C')

top_item = stack.pop()



print(stack.getData(), top_item)
