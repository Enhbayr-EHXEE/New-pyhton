class Deque:
    def __init__(self):
        self.__items = []

    def isEmpty(self):
        return len(self.__items) == 0

    def insertFront(self, item):
        self.__items.insert(0, item)

    def insertRear(self, item):
        self.__items.append(item)

    def deleteFront(self):
        if not self.isEmpty():
            return self.__items.pop(0)
        else:
            return "Deque is empty"

    def deleteRear(self):
        if not self.isEmpty():
            return self.__items.pop()
        else:
            return "Deque is empty"

    def size(self):
        return len(self.__items)

    def getFront(self):
        if not self.isEmpty():
            return self.__items[0]
        else:
            return "Deque is empty"

    def getRear(self):
        if not self.isEmpty():
            return self.__items[-1]
        else:
            return "Deque is empty"
    
    def __str__(self):
        return ", ".join(str(item) for item in self.__items)

# Example usage:
deque = Deque()
deque.insertFront(1)
deque.insertFront(2)
deque.insertFront(3)
deque.insertFront(4)
deque.insertRear(5)
deque.insertRear(6)
print(deque)          

print(deque.deleteFront()) 
print(deque.deleteRear())   
print(deque)        
