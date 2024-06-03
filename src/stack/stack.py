class Stack:
    def __init__(self):
        self.head = None
        self.tail = None
        self.next = None
        self.prev = None
        self.length = 0

    def __str__(self):
        temp = self.head
        str_out = ""
        while temp:
            if temp.next != None:    
                str_out = str_out + str(temp.val) + ", "
                temp = temp.next
            else:
                str_out = str_out + str(temp.val)
                temp = temp.next
        return str_out

    def enstack(self, val):
        if not isinstance(self.head, link_node):
            self.head = link_node(val)
            self.tail = self.head
            self.length += 1
        elif isinstance(self.head, link_node) and self.length > 0:
            temp = self.head
            for i in range(self.length - 1):
                temp = temp.next
            temp.next = link_node(val)
            self.tail = temp.next
            self.tail.prev = temp
            self.length += 1
            
    def destack(self):
        destack = self.tail
        if self.length == 0:
            pass
        elif self.length == 1:
            self.head, self.tail = None, None
            self.length -= 1
        elif self.length > 1:
            self.tail = self.tail.prev
            self.tail.next = None
            self.length -= 1
        return destack
    
    def len(self):
        return self.length
    
class link_node:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None
        # TODO: make a doubly linked list with self.prev

    def __str__(self):
        return f"{self.val}"

