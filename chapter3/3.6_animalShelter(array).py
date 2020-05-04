class AnimalShelter:
    def __init__(self):
        self.items = []
    
    def enqueue(self, species, name):
        record = {}
        if species.lower() == "dog":
            record = {"dog" : name}
        elif species.lower() == "cat":
            record = {"cat" : name}
        else:
            return "Shelter of dogs and cats only"
        self.items.append(record)
        return self
    
    def dequeueAny(self):
        if self.items == []:
            return "There  no animals right now"

        dq = self.items[0]
        del self.items[0]
        return dq
    
    def dequeueDog(self):
        if len( self.items ) == 0:
            return "There are no animals right now"

        for i in range(len( self.items )):
            if "dog" in self.items[i]:
                dq_dog = self.items[i]
                del self.items[i]
                return dq_dog
        return "There are only cats"
    
    def dequeueCat(self):
        if len( self.items ) == 0:
            return "There are no animals right now"

        for i in range(len( self.items )):
            if "cat" in self.items[i]:
                dq_cat = self.items[i]
                del self.items[i]
                return dq_cat
        return "There are only dogs"
    
coolShelter = AnimalShelter()
coolShelter.enqueue("dog", "bhau-bhau")
coolShelter.enqueue("dog", "jacky")
coolShelter.enqueue("cat", "meow")
print(coolShelter.dequeueAny())
# print(coolShelter.dequeueDog())



