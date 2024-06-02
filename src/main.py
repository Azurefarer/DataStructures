from linked_list import Linked_List
from my_queue import Queue

def main():
    ints = Linked_List()
    for i in range(6):
        # this will make 6 entries from 0 to 6
        ints.push(i)
        print(ints)

    intsq = Queue()
    for i in range(6):
        # this will make 6 entries from 0 to 6
        intsq.enqueue(i)
        print(intsq)
    for i in range(6):
        print(intsq.dequeue())
        print(intsq)
        print(intsq.len())
main()