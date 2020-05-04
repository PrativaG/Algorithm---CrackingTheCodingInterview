class QueueNode:
    def __init__(self, val):
        self.value = val
        self.next = None
    
class MyQueue:
    def __init__(self):
        self.first = None
        self.last = None

    def remove(self):
        if self.first == None:
            return None
       
        self.first =  self.first.next
        return 

    def add(self, item):
        q = QueueNode(item)
   
        if self.last != None:
           self.last.next = q
        self.last = q

        if self.first == None:
            self.first = self.last
        return self
    
    def peek(self):
        if self.first == None:
            return None
       
        return self.first.value
    
    def isEmpty(self):
        if self.first == None:
            return True
        else:
           return  False

def printValues(queue):
    if queue.first == None:
        return None
    runner = queue.first
    while runner != None:
        print(runner.value)
        runner = runner.next
    return

q1 = MyQueue()
q1.add(101)
q1.add(105)
q1.add(106)
q1.add(109)
printValues(q1)
q1.remove()
printValues(q1)
print(q1.peek())
print(q1.isEmpty())

q2 = MyQueue()
print(q2.isEmpty())
