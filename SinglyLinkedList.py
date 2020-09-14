class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.next = None

    def __len__(self):
        cur = self.head
        count = 0
        while cur:
            count += 1
            cur = cur.next
        return count

    def len(self):
        self.__len__()

    def print_sll(self):
        if self.head:
            cur = self.head
            while cur:
                print(cur.val, end="->")
                cur = cur.next
            print(None)

    def insert_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        cur = self.head
        while cur.next:
            cur = cur.next
        cur.next = new_node
        return None

    def insert_begin(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        cur = self.head
        self.head = new_node
        new_node.next = cur
        return None

    def insert_with_pos(self, pos, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        length = len(self)
        if pos<length:
            self.insert_begin(data)
            return
        if pos>length:
            self.insert_end(data)
            return
        cur = self.head
        count = 0
        while count + 1 < pos:
            cur = cur.next
            count += 1
        aux = cur.next
        cur.next = new_node
        new_node.next = aux

    def del_begin(self):
        cur = self.head
        if cur is None:
            return
        if cur.next is None:
            self.head = None
            return
        self.head = cur.next
        cur.next = None

    def del_end(self):
        cur = self.head
        if self.head is None:
            return
        if cur.next is None:
            self.head = None
            return
        while cur.next.next is not None:
            cur = cur.next
        cur.next = None

    def del_with_pos(self, pos):
        length = len(self)
        count = 0
        cur = self.head
        if pos < 0 or pos > length - 1:
            print("Invalid Position")
            return
        if pos == 0:
            self.head = cur.next
            return
        if pos == length:
            self.del_end()
            return
        while count + 1 < pos:
            cur = cur.next
            count += 1
        aux = cur.next
        if aux.next:
            cur.next = aux.next
        else:
            cur.next = None

    def __add__(self, other):
        cur = self.head
        other_head = other.head
        if cur is None:
            self.head = other_head
        while cur.next is not None:
            cur = cur.next
        cur.next = other_head

    def add(self, other):
        self.__add__(other)

    def print_reverse(self):
        self.__print_reverse(self.head)
        print(None)

    def __print_reverse(self, cur):
        if cur is None:
            return
        if cur.next:
            self.__print_reverse(cur.next)
        print(cur.val, end='->')

    def clear(self):
        self.head = None

    def __reversed__(self, cur):
        last = None
        while cur:
            aux = cur.next
            cur.next = last
            last = cur
            cur = aux
        self.head = last

    def reversed(self):
        if self.head is None:
            return
        elif self.head.next is None:
            return
        else:
            self.__reversed__(self.head)


if __name__ == '__main__':
    pass
