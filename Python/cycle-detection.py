# solution to the HackerRank problem "Cycle Detection"
# https://www.hackerrank.com/challenges/detect-whether-a-linked-list-contains-a-cycle/problem
# Given a pointer to the head of a linked list, determine if it contains a cycle.
# Ahmetcan Ozturk

def has_cycle(head):
    cycle = False
    visited = [head]
    while (not cycle and head.next != None):
        head = head.next
        if head in visited:
            cycle = True
        visited.append(head)
        if (head.next == None):
            return False

    return cycle

# singly linked list
class SinglyLinkedListNode:
    def __init__(self, node_data):
        self.data = node_data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_node(self, node_data):
        node = SinglyLinkedListNode(node_data)

        if not self.head:
            self.head = node
        else:
            self.tail.next = node


        self.tail = node

def print_singly_linked_list(node, sep, fptr):
    while node:
        print(str(node.data))

        node = node.next

        if node:
            print(sep)

if __name__ == "__main__":
    tests = int(input())

    for tests_itr in range(tests):
        index = int(input())

        llist_count = int(input())

        llist = SinglyLinkedList()

        for _ in range(llist_count):
            llist_item = int(input())
            llist.insert_node(llist_item)

        extra = SinglyLinkedListNode(-1)
        temp = llist.head

        for i in range(llist_count):
            if i == index:
                extra = temp

            if i != llist_count-1:
                temp = temp.next

        temp.next = extra

        result = has_cycle(llist.head)
        print('output:')
        print(str(int(result)) + '\n')