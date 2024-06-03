from linked_list import Linked_List
from my_queue import Queue
from stack import Stack

def main():
    ints = Linked_List()
    for i in range(6):
        # this will make 6 entries from 0 to 5
        ints.push(i)
        print(f"Linked List: {ints}")

    intsq = Queue()
    for i in range(6):
        # this will make 6 entries from 0 to 5
        intsq.enqueue(i)
        print(f"queue: {intsq}")
    for i in range(6):
        intsq.dequeue()
        print(f"queue: {intsq}")        

    intss = Stack()
    for i in range(6):
        intss.enstack(i)
        print(f"stack: {intss}")
    for i in range(6):
        intss.destack()
        print(f"stack: {intss}")

main()
