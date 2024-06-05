class Tree: # Tree Data Structure | Tree Data Type Inspector
    def __init__(self):
        self.root = None
        self.current = None
        self.index = 0

        self.id = {
            "level" : 1,
            "tree_height" : 0,
            "depth" : 0,
            "node_height" : 0
        }
        # Level | Tree_Height | Depth | Node_Height

    def __str__(self):
        str_out = ""
        for key in self.id:
            str_out += f"{key}: {self.id[key]}\n"
        str_out += str(self.current) + "\n"

        return str_out

    # Manipulation
    def insert(self, val, *args): # *args should be an index
        if self.root == None:
            self.root = Tree_Node(val)
            self.current = self.root
        else:
            if args: self.index = args[0]
            if self.current.head == None:
                self.id["tree_height"] += 1
                self.id["node_height"] += 1
            self.current.add_child(val, self.index)
            if self.current.len() == self.index:
                self.index += 1
            else: pass

    def replace(self, val, index):
        if self.current.child == None:
            temp = self.current.parent
            self.current.add_child(val)
        
        elif self.root != None and self.current.child != None:
            temp = self.current.child
            self.current.child = Tree_Node(val)
            self.current.child.child = temp
            self.current.child.child.parent = self.current.child
            self.current.child.parent = self.current
            self.current = self.current.child

    # Navigation
    def p2c(self, index):
        temp = self.current.head
        parent = self.current
        for i in range(index - 1):
            temp = temp.next
        self.current = temp
        self.current.parent = parent
        self.id["level"] += 1
        self.id["depth"] += 1
        self.id["node_height"] -= 1

    def c2p(self):
        self.current = self.current.parent
        self.id["level"] -= 1
        self.id["depth"] -= 1
        self.id["node_height"] += 1

    def reset(self):
        self.current = self.root
        self.id["level"] = 1
        self.id["depth"] = 0
        self.id["node_height"] = self.id["tree_height"]


class Tree_Node: # Tree Data Type | It's a linked list
    def __init__(self, val):
        self.val = val
        self.head = None # Leftmost child node
        self.parent = None # Ancestor of this node
        self.next = None # Pointer to Children of this node
    
    def __str__(self):
        str_out = f"Current Node:\nValue: {self.val}\n"
        str_out += f"Parent: {self.parent}\n" if self.parent == None else f"Parent: {self.parent.val}\n"
        temp = self.head
        while temp:
            if temp.next != None:
                str_out += str(temp.val) + ","
                temp = temp.next
            else:
                str_out += str(temp.val) + "\n"
                temp = temp.next
        return str_out
    
    def add_child(self, val, index):
        if self.head == None:
            self.head = Tree_Node(val)
        elif self.head != None:
            temp = self.head
            for i in range(index - 1):
                temp = temp.next
            old_link = temp.next
            temp.next = Tree_Node(val)
            temp.next.next = old_link
    
    def ins_child(self, val, index):
        if index > self.len():
            try:
                raise Exception("insert index out of range")
            except Exception as inst:
                print(inst)
        elif self.head != None and (index-1) != self.len():
            temp = self.head
            for i in range(index-1):
                temp = temp.next
            old_link = temp.next
            temp.next = Tree_Node(val)
            temp.next.next = old_link
            
    def len(self):
        length = 0
        temp = self.head
        while temp:
            temp = temp.next
            length += 1
        return length
