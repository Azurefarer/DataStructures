class Queue:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0
    
    def __str__(self):
        temp = self.head
        str_out = ""
        while temp:
            str_out = str_out + str(temp.val) + ", "
            temp = temp.next
        return str_out
    
    def enqueue(self, val):
        if self.head == None and self.length == 0:    
            self.head = link_node(val)
            self.length += 1
        else:
            temp = self.head
            for i in range(self.length - 1):
                temp = temp.next
            temp.next = link_node(val)
            self.length += 1

    def dequeue(self):
        dequeue = self.head
        self.head = self.head.next
        self.length -= 1      
        return dequeue
    
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
