class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items)-1]

    def size(self):
        return len(self.items)
    
    def printAll(self):
        for data in self.items[::-1]:
            print(data)

# Queue implementing two stacks
class MyQueue:
    
    def __init__(self, s1, s2):
        self.queue = []

        while(s2.size() != 0):
            v2 = s2.pop()
            self.queue.insert(0, v2) 

        while(s1.size() != 0):
            v = s1.pop()
            self.queue.insert(0, v) 

    def pop(self):
        poppedItem = self.queue[0]
        del self.queue[0]
        return poppedItem
    
    def peek(self):
        return self.queue[0]
    
    def isEmpty(self):
        return self.queue == []
    
    def size(self):
        return len ( self.queue )
    
    def printValues(self):
        for i in range(len( self.queue )):
            print(self.queue[i])
        return

stack1 = Stack()
stack1.push(-1)
stack1.push(5)
stack1.push(1)
stack1.push(7)
stack1.push(1)
stack1.push(8)   

stack2 = Stack()
stack2.push(-2)
stack2.push(55)
stack2.push(11)
stack2.push(77)
stack2.push(11)
stack2.push(88)   

q1 = MyQueue(stack1, stack2)
# q1.printValues()
q1.pop()
q1.printValues()
print(q1.peek())
print(q1.size())


        