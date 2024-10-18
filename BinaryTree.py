class BinaryTree:
    def __init__(self,data):
        self.__data=data
        self.__left=None
        self.__right=None
    
    def set_data(self,data):
         self.__data=data

    def get_data(self):
        return self.__data
    
    def set_left(self,data):
        self.__left=data
    
    def get_left(self):
        return self.__left
    
    def set_right(self,data):
        self.__right=data
    
    def get_right(self):
        return self.__right
    
    def __str__(self):
        return f"data is {self.get_data()}"
    
    def insert(self,data):
        if self.get_data():
            if data < self.get_data():
                if self.get_left() == None:
                    self.set_left(BinaryTree(data))
                else:
                    self.__left.insert(data)
            elif data > self.get_data():
                if self.get_right() == None:
                    self.set_right(BinaryTree(data))
                else:
                    self.__right.insert(data)
            else:
                print("the value is already in the tree")
        else:
            self.__data=data

    def find_min_value(self):
        if self.get_left() is None:
            return self.get_data()
        else:
            return self.__left.find_min_value()

    def find_max_value(self):
        if self.get_right() is None:
            return self.get_data()
        else:
            return self.get_right().find_max_value()

    def in_order(self):
        if self.get_left():
            self.get_left().in_order()
        print(self.get_data(), end=' ')
        if self.get_right():
            self.get_right().in_order()  

    def pre_order(self):
        print(self.get_data(), end=' ')
        if self.get_left():
            self.get_left().pre_order()
        if self.get_right():
            self.get_right().pre_order()

    def post_order(self):
        if self.get_left():
            self.get_left().post_order()
        if self.get_right():
            self.get_right().post_order()
        print(self.get_data(), end=' ')  
def Binary_Search(array,target):
    low=0
    high=len(array)-1
    while low<=high:
        mid=(low+high)//2
        if array[mid]==target:
            return True
        elif target<array[mid]:
            high=mid-1
        elif target>array[mid]:
            low=mid+1
    return False

def main():
    target=21
    array=[1,2,3,5,8,10,20]
    print(Binary_Search(array,target))
if __name__ == "__main__":
    main()