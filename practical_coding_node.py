class BinaryTree:
    def __init__(self, data):
        self.__data = data
        self.__left = None
        self.__right = None

    def set_data(self, data):
        self.__data = data

    def get_data(self):
        return self.__data

    def set_left(self, data):
        self.__left = data

    def get_left(self):
        return self.__left

    def set_right(self, data):
        self.__right = data

    def get_right(self):
        return self.__right

    def __str__(self):
        return f"Data is {self.get_data()}"

    def insert(self, data):
        if self.get_data():
            if data < self.get_data():
                if self.get_left() is None:
                    self.set_left(BinaryTree(data))
                else:
                    self.get_left().insert(data)
            elif data > self.get_data():
                if self.get_right() is None:
                    self.set_right(BinaryTree(data))
                else:
                    self.get_right().insert(data)
            else:
                print("The value is already in the tree")
        else:
            self.set_data(data)

    def find_min_value(self):
        if self.get_left() is None:
            return self.get_data()
        else:
            return self.get_left().find_min_value()

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

    def delete(self, data):
        if self is None:
            return self

        if data < self.get_data():
            self.set_left(self.get_left().delete(data))
        elif data > self.get_data():
            self.set_right(self.get_right().delete(data))
        else:
            # Node with one child or no child
            if self.get_left() is None:
                return self.get_right()
            elif self.get_right() is None:
                return self.get_left()

            # Node with two children
            temp_val = self.get_right().find_min_value()
            self.set_data(temp_val)
            self.set_right(self.get_right().delete(temp_val))

        return self


def main():
    tree = BinaryTree(100)
    tree.insert(101)
    tree.insert(99)
    tree.insert(98)
    tree.insert(97)
    tree.insert(96)
    tree.insert(1)

    # Test finding min and max
    print(f"Min value: {tree.find_min_value()}")
    print(f"Max value: {tree.find_max_value()}")

    # Test traversal
    print("\nIn-order traversal:")
    tree.in_order()

    print("\nPre-order traversal:")
    tree.pre_order()

    print("\nPost-order traversal:")
    tree.post_order()

    # Test deletion
    print("\n\nAfter deleting 99:")
    tree.delete(99)
    tree.in_order()


if __name__ == "__main__":
    main()
