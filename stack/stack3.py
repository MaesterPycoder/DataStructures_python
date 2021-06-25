# Implementing Stack using Linked List




class Node:
    def __init__(self, value) -> None:
        self.value = value
        self.next = None

class Stack:
    def __init__(self) -> None:
        self.head = None

    def add_element(self,value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            return
        cur = self.head

        while cur.next:
            cur = cur.next
        cur.next = new_node

    def pop_element(self):
        if self.head is None:
            raise Exception("Stack UnderFlow")

        if self.head.next is None:
            self.head = None
            return 
        cur = self.head

        prev= None
        while cur.next:
            prev = cur
            cur = cur.next
        prev.next = None
        cur = None

        
    def size_of_stack(self):
        count = 0
        cur = self.head

        while cur:
            count+=1
            cur = cur.next
        return count

    
    def print_stack(self):
        cur = self.head
        while cur:
            print(cur.value, end="->")
            cur = cur.next
        




if __name__ == "__main__":
    st = Stack()
    st.add_element(10)
    st.add_element(20)
    st.add_element(30)
    st.add_element(40)
    st.print_stack()
    print("\n")
    print("Size = ",st.size_of_stack())

    print("------------------pop Element__________------")

    st.pop_element()
    st.pop_element()
    st.pop_element()
    st.pop_element()
    st.pop_element()
    st.print_stack()
    print("\n")
    print("Size = ",st.size_of_stack())

