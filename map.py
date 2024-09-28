class Map:
    def __init__(self):
        self.__dict={}
    
    def put_item(self, key, value):
        self.__dict[key]=value
    
    def get_value(self, key):
        return self.__dict.get(key)

    def del_value(self,key):
        if self.__dict.get(key) != None:
            del self.__dict[key]
        else:
            print("key does not exist in the map")


    def value_exist(self,value):
        for key,val in self.__dict.items() :
            if val == value:
                return True
        return False
    
    def get_all_keys(self,value):
        result=[]
        for k,val in self.__dict.items():
            if(val==value):
                result.append(k)
        return result
    
    def delete_values(self,value):
        keys=self.get_all_keys(value)
        if len(keys)>0:
            for key in keys :
                del self.__dict[key]

    def display_map(self):
        print(self.__dict)  
        
def main():
    map=Map()
    map.put_item(10,10)
    map.put_item(20,10)
    map.put_item(30,11)
    map.put_item(40,11)
    map.delete_values(10)
    print(map.value_exist(11))
    map.display_map()
if __name__ == "__main__":
    main()