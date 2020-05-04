import math
class SLNode:
    def __init__(self, val):
        self.value = val
        self.next = None
        
class SLList:

    def __init__(self):
        self.head = None

    def addToFront(self, val):
        newNode = SLNode(val)
        if self.head == None:
            self.head =  newNode
        else:
            newNode.next = self.head
            self.head = newNode
        return self
    
    def printValues(self):
        runner = self.head
        while(runner != None):
            print(runner.value)
            runner = runner.next
        return self
    
    def addToEnd(self, val):
        newNode = SLNode(val)
        if self.head == None:
            newNode = self.head
            return self 

        runner = self.head
        while(runner.next != None):
            runner = runner.next
        runner.next = newNode
        return self
    
    def size(self):
        runner = self.head
        s = 0
        while runner != None:
            s += 1
            runner = runner.next
        return s

    # 2.1
    def removeDupes(self):
        runner1 = self.head
        runner2 = self.head
        while runner1.next != None:
            if runner1.value == runner2.next.value:
                runner2.next = runner2.next.next

            else:
                runner2 = runner2.next
                if runner2.next == None:
                    runner1 = runner1.next
                    runner2 = runner1
        return self   

    # 2.2
    def kthToLast(self, k):
        runner1 = self.head
        countNode = 0

        while runner1 != None:
            countNode += 1
            if countNode > k:
                print(runner1.value)
            runner1 = runner1.next
            
        return self
    
    # 2.3
    def deleteMiddle(self):

        if self.head.next == None:
            self.head = None
        elif self.head.next.next == None:
            self.head.next = None

        slowRunner = self.head
        fastRunner = slowRunner.next.next

        while(slowRunner != None):
           
            if fastRunner.next == None:
                slowRunner.next = slowRunner.next.next
                return

            slowRunner = slowRunner.next
            fastRunner = fastRunner.next.next

    #2.4
    def partition(self, x):

        fastRunner = self.head
        slowRunner = self.head
        # 3 44 56 5 2 1
        print("Hello from partition")
        while fastRunner.next != None:
            if fastRunner.next.value < x:
                self.head = fastRunner.next
                fastRunner.next = fastRunner.next.next
                fastRunner.next.next = slowRunner

                slowRunner = self.head
                print("inside while")
                # if fastRunner.next.value > x:
            fastRunner = fastRunner.next
                # else:
                #     fastRunner = fastRunner
        print("Bye bye from partition")
        return self

    # 2.5
    # assuming lists passed in parameters have same length
    def sumLists(self, list1, list2):
        runner1 = list1.head
        runner2 = list2.head
        listSum = SLList()
        carryover = 0
        while(runner1 != None):
            nodeVal = runner1.value + runner2.value + carryover
           
            if nodeVal > 9 :
                carryover = math.floor(nodeVal / 10) 
                listSum.addToFront(nodeVal % 10)
            else:
                listSum.addToFront(nodeVal)
            runner1 = runner1.next
            runner2 = runner2.next
        return listSum

    #2.6 [ Creating reverse list approach ]
    def palindrome(self, slist):
        reverseList = SLList()
        runner = self.head
        print(runner.value)
        while(runner != None):
            reverseList.addToFront(runner.value)
            print("Runner value",runner.value)
            runner = runner.next
        
        r1 = self.head
        r2 = reverseList.head
        print("outside loop")
        while(r1 != None):
            print("r1 vs r2")
            if r1.value != r2.value:
                return False
            r1 = r1.next
            r2 = r2.next
        return True

    # 2.6 [ Creating object and checking occurrence of letters ]
    def palindrom(self, slist):
        pass

 
            


mySll = SLList()
mySll.addToFront(78)
mySll.addToEnd(6)
mySll.addToEnd(50)
mySll.addToEnd(7)
mySll.addToEnd(50)
mySll.addToEnd(7)
mySll.addToEnd(30)

# mySll.printValues() 

# mySll.removeDupes()
# print("After removing Duplicate!")
# print("After kth to last!")
# mySll.kthToLast(3)
print("************")
# mySll.deleteMiddle()
# mySll.printValues()

# mySll.partition(50)
# mySll.printValues()

# [ Testing  2.5 sumLists ]
l1 = SLList()
l1.addToFront(7)
l1.addToEnd(1)
l1.addToEnd(6)

l2 = SLList()
l2.addToFront(5)
l2.addToEnd(9)
l2.addToEnd(2)

# l1.sumLists(l1, l2)

# [ Testing 2.6 palindrome ]
p = SLList()
p.addToEnd("a")
p.addToEnd("y")
p.addToEnd("b")
p.addToEnd("a")

print(p.palindrome(p))


    