class Location:
    def __init__(self,name,country):
        self.name=name
        self.country=country
    def myLocation(self):
        print("Hi my name is " + self.name + " and I live in "+self.country+".")
loc1=Location("Enkhbayar","Mongolia")
loc2 = Location("Ying", "China") 
loc3 = Location("Amare", "Kenya")
loc1.myLocation()
loc2.myLocation()
loc3.myLocation()