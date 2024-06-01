class Linked_List:
    def __init__(self):
        self.head = None

    def __str__(self):
        temp = self.head
        str_out = ""
        while temp:
            str_out = str_out + str(temp.val) + ", "
            temp = temp.next
        return str_out

    def insert(self, val, index):
        if index == 0:
            old_link = self.head
            self.head = link_node(val)
            self.head.next = old_link
        elif self.head != None and index == 1:
            old_link = self.head.next
            new_node = link_node(val)
            new_node.next = old_link
            self.head.next = new_node
        elif self.head != None and index > 1:
            temp = self.head
            for i in range(index-1):
                temp = temp.next
            old_link = temp.next
            new_node = link_node(val)
            new_node.next = old_link
            temp.next = new_node

    def remove(self, index):
        removal = None
        if index == 0:
            removal = self.head
            self.head = self.head.next
        elif index > 0:
            temp = self.head
            for i in range(index-1):
                temp = temp.next
            removal = temp.next
            temp.next = temp.next.next
        return removal

    def get(self, index):
        get = None
        if index == 0:
            get = self.head
        elif index > 0:
            temp = self.head
            for i in range(index-1):
                temp = temp.next
            get = temp.next
        return get

    def set(self, val, index):
        if index == 0:
            self.head.val = val
        elif index > 0:
            temp = self.head
            for i in range(index):
                temp = temp.next
            temp.val = val

    def len(self):
        length = 0
        temp = self.head
        while temp:
            temp = temp.next
            length += 1
        return length

    def push(self, val):
        if self.len() == 0:
            self.head = link_node(val)
        elif self.len() == 1:
            self.head.next = link_node(val)
        elif self.len() > 1:
            temp = self.head
            for i in range(self.len() - 1):
                temp = temp.next
            temp.next = link_node(val)

    def pop(self):
        pop_val = None
        if self.len() == 1:
            pop_val = self.head
            self.head = None
        else:
            temp = self.head
            for i in range(self.len() - 2):
                temp = temp.next
            pop_val = temp.next
            temp.next = None
        return pop_val

    def sort(self):
        pass

class link_node:
    def __init__(self, val):
        self.val = val
        self.next = None
        # TODO: make a doubly linked list with self.prev

    def __str__(self):
        return f"{self.val}"

def main():
    ints = Linked_List()
    ints.insert(10, 0)
    ints.insert(5, 1)
    ints.insert(5, 2)
    ints.insert(6, 3)
    print(f"length = {ints.len()}")
    print(ints)
    ints.set(12, 0)
    print(ints)
    print(ints.pop())
    print(ints)
    ints.push(7)
    print(ints)

main()
