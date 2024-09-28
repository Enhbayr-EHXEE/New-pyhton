

class hashTable:
    def __init__(self):
        self.MAX_VALUE=15
        self.table=[None]*self.MAX_VALUE
    
    def get_hash(self,value):
        return hash(value)%self.MAX_VALUE
    
print(hash("asds"))