class Node:
    def __init__(self, data):
        self.val = data
        self.next = None


class CircularLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def print_cll(self):
        if self.head is None:
            return
        if self.head is self.tail:
            print(self.head.val)
            return
        cur = self.head
        while cur.next is not self.head:
            print(cur.val, end='->')
            cur = cur.next
        print(self.tail.val)

    def len(self):
        cur = self.head
        count = 0
        while cur.next is self.head:
            count += 1
            cur = cur.next
        return count

    def insert_begin(self, data):
        new_node = Node(data)
        cur = self.head
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            return
        if cur is self.tail:
            self.head = new_node
            new_node.next = cur
            self.tail = cur
            return
        self.head = new_node
        new_node.next = cur
        self.tail.next = new_node

    def insert_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            return
        cur = self.head
        if self.head is self.tail:
            cur.next = new_node
            self.tail = new_node
            new_node.next = cur
            return
        while cur.next is not self.head:
            cur = cur.next
        cur.next = new_node
        new_node.next = self.head
        self.tail = new_node

    def del_begin(self):
        if self.head is None:
            return
        if self.head is self.tail:
            self.head = None
            return
        if self.head.next is self.tail:
            self.head = self.tail
            return
        cur = self.head
        while cur.next is not self.head:
            cur = cur.next
        cur.next = cur.next.next
        self.head = cur.next

    def del_end(self):
        if self.head is None:
            return
        if self.head is self.tail:
            self.head = None
            return
        if self.head.next is self.tail:
            self.tail = self.head
            return
        cur = self.head
        while cur.next.next is not self.head:
            cur = cur.next
        cur.next = self.head
        self.tail = cur

    def del_by_value(self, data):
        if self.head is None:
            return
        if self.head is self.tail and self.head.val == data:
            self.head = None
            self.tail = self.head
            return
        cur = self.head
        if cur.val == data:
            self.del_begin()
            return
        if self.tail.val == data:
            self.del_end()
            return
        while cur.next is not self.head and cur.next.val != data:
            cur = cur.next
        cur.next = cur.next.next


if __name__ == '__main__':
    pass
