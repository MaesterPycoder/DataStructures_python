class Node:
    def __init__(self, val):
        self.val = val
        self.prev = None
        self.next = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.prev = None
        self.next = None

    def print_dll(self):
        if self.head:
            cur = self.head
            print("None", end='<=>')
            while cur:
                print(cur.val, end="<=>")
                cur = cur.next
            print(None)

    def insert_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = Node(data)
            return
        cur = self.head
        while cur.next:
            cur = cur.next
        cur.next = new_node
        new_node.prev = cur

    def insert_begin(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        cur = self.head
        new_node.next = cur
        cur.prev = new_node
        self.head = new_node

    def insert_with_pos(self, pos, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        if pos == 0:
            self.insert_begin(data)
            return
        length = self.__len__(self.head)
        if pos > length:
            self.insert_end(data)
            return
        cur = self.head
        while cur.next:
            cur = cur.next
        aux = cur.next
        cur.next = new_node
        new_node.prev = cur
        new_node.next = aux
        aux.prev = new_node

    def del_begin(self):
        if self.head is None:
            return
        cur = self.head
        if cur.next is None:
            self.head = None
            return
        aux = cur.next
        self.head = aux
        aux.prev = None

    def del_end(self):
        if self.head is None:
            return
        cur = self.head
        if cur.next is None:
            self.head = None
            return
        while cur.next.next is not None:
            cur = cur.next
        aux = cur.next
        cur.next = None
        aux.prev = None

    def del_with_pos(self, pos):
        if self.head is None:
            return
        count = 0
        cur = self.head
        length = self.__len__(self.head)
        if pos < 0 or pos > length:
            print("Invalid Position")
            return
        if pos == 0:
            self.del_begin()
            return
        if pos == length - 1:
            self.del_end()
            return
        while count + 1 < pos:
            cur = cur.next
            count += 1
        aux = cur.next.next
        cur.next = aux
        aux.prev = cur

    def __len__(self, cur):
        count = 0
        while cur:
            count += 1
            cur = cur.next
        return count

    def len(self):
        print(self.__len__(self.head))

    def print_reversed(self):
        cur = self.head
        while cur.next is not None:
            cur = cur.next
        print("None", end='<=>')
        while cur is not None:
            print(cur.val, end='<=>')
            cur = cur.prev
        print(None)

    def reversed(self):
        cur = self.head
        if cur is None or cur.next is None:
            return
        temp = None
        while cur:
            temp = cur.prev
            cur.prev = cur.next
            cur.next = temp
            cur = cur.prev
        if temp:
            self.head = temp.prev

    def clear(self):
        self.head = None
        self.prev = None

    def add(self, other):
        if self.head is None:
            self.head = other.head
            return
        cur = self.head
        other_head = other.head
        while cur.next is not None:
            cur = cur.next
        cur.next = other_head
        other_head.prev = cur


if __name__ == '__main__':
    pass
