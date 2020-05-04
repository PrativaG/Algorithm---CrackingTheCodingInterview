class StackNode:
    def __init__(self, val):
        self.value = val
        self.next = None
    
class MyStack:
    def __init__(self):
        self.top = None

    def pop(self):
        if self.top == None:
            return None

        self.top = self.top.next 
        return 

    def push(self, val):
        s = StackNode(val)
        if self.top == None:
            self.top = s
        else:
            s.next = self.top
            self.top = s
        return self
    
    def peek(self):
        if self.top == None:
            return None
        else:
            return self.top.value
    
    def isEmpty(self):
        if self.top == None:
            return True
        return False

    #3.2
    def minValue(self):
        min = self.top
        runner = self.top.next
        while runner != None:
            if min.value > runner.value:
                min = runner
            runner = runner.next
        return min.value
    
# 3.5
def sortStack(stack):
    tempStack = MyStack()
    tempStack.push(stack.top.value)

    runner = stack.top.next
    while True:
        if tempStack.top.value > runner.value:
            tempStack.pop()
            tempStack.push(runner.value)
        
        if size(stack) == size(tempStack):
            return tempStack
        
        if runner.next == None:
            runner = stack.top.next
        runner = runner.next
        

def printValues(stack):
    if stack.top == None:
        return None
    runner = stack.top
    while runner != None:
        print(runner.value)
        runner = runner.next
    return

def size(stack):
    runner = stack.top
    s = 0
    while runner != None:
        s += 1
        runner = runner.next
    return s



stack1 = MyStack()
stack1.push(55)
stack1.push(66)
stack1.push(7)
stack1.push(32)
# # printValues(stack1)
# # stack1.pop()
# # printValues(stack1)
# print("*********")
# print(stack1.peek())
# print(stack1.minValue())
new = sortStack(stack1)
new.printValues()
