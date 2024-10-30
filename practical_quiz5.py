class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self):
        return str(self.data)
    
class LinkedList:
    def __init__(self):
        self.head = None

    def set_head(self, node):
        self.head = node

    def get_head(self):
        return self.head

    def __repr__(self):
        nodes=""
        current = self.head
        while current:
            nodes=nodes+" "+str(current)
            current = current.next
        return nodes

    def insert_after(self, key, data):
        current = self.head
        while current:
            if current.data == key:
                new_node = Node(data)
                new_node.next = current.next
                current.next = new_node
                return
            current = current.next
        print(f"Key '{key}' not found in the list.")

    def insert_before(self, key, data):
        if self.head is None:
            print("List is empty.")
            return

        if self.head.data == key:
            new_node = Node(data)
            new_node.next = self.head
            self.head = new_node
            return

        current = self.head
        while current.next:
            if current.next.data == key:
                new_node = Node(data)
                new_node.next = current.next
                current.next = new_node
                return
            current = current.next
        print(f"Key '{key}' not found in the list.")

    def delete_after(self, key):
        current = self.head
        while current:
            if current.data == key:
                if current.next:
                    current.next = current.next.next
                else:
                    print(f"No node found after the key '{key}'.")
                return
            current = current.next
        print(f"Key '{key}' not found in the list.")


# Example Usage:
ll = LinkedList()
node_a = Node('A')
node_b = Node('B')
node_c = Node('C')

ll.set_head(node_a)
node_a.next = node_b
node_b.next = node_c

print("Original list:")
print(ll)

print("\nAfter insert_after('B', 'W'):")
ll.insert_after('B', 'W')
print(ll)

print("\nAfter insert_before('B', 'W'):")
ll.insert_before('B', 'W')
print(ll)

print("\nAfter delete_after('B'):")
ll.delete_after('B')
print(ll)