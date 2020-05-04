class Dog:
    def __init__(self, name):
        self.name = name

class Cat:
    def __init__(self, name):
        self.name = name

class QueueNode:
    def __init__(self, val):
        self.value = val
        self.next = None

class AnimalShelter:
    def __init__(self):
       self.first = None
       self.last = None 
    
    def size(self):
        s = 0
        runner = self.first
        while runner != None:
            s += 1
            runner = runner.next
        return s
    
    def enqueue(self, val):
        q = QueueNode(val)
   
        if self.last != None:
           self.last.next = q
        self.last = q

        if self.first == None:
            self.first = self.last
        return self
    
    def dequeueAny(self):
        if self.first == None:
            return "There are no animals"
        dq = self.first
        self.first =  self.first.next
        return dq.value
    
    def dequeueDog(self):
        if self.first == None:
            return "There are no animals"

        if isinstance(self.first.value, Dog):
            dq_dog = self.first.value
            self.first = self.first.next
            return dq_dog.name

        runner = self.first
        while runner.next != None:
            if isinstance(runner.next.value, Dog):
                dq_dog = runner.next
                runner.next = runner.next.next
                return dq_dog.name
            runner = runner.next
        return "There are only cats"
    
    def dequeueCat(self):
        if self.first == None:
            return "There are no animals"
        
        if isinstance(self.first.value, Cat):
            dq_cat = self.first.value
            self.first = self.first.next
            return dq_cat.name
            
        runner = self.first
        while runner.next != None:
            if isinstance(runner.next.value, Cat):
                dq_cat = runner.next.value
                runner.next = runner.next.next
                return dq_cat.name
            runner = runner.next
        return "There are only dogs"

d1 = Dog("jacky")
c1 = Cat("meow")
d2 = Dog("lovely")
c2 = Cat("hakuna")

newShelter = AnimalShelter()
newShelter.enqueue(d1)
newShelter.enqueue(c2)
newShelter.enqueue(c1)
newShelter.enqueue(d2)
print(newShelter.dequeueDog())
print(newShelter.dequeueCat())

            
