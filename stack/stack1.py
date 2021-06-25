# Implementing Stack Data Structure in Python




class Stack:
    def __init__(self) -> None:
        self.stack = []

    def add_element(self, value):
        self.stack.append(value)


    def pop_element(self):
        return self.stack.pop(-1)

    def size(self):
        return len(self.stack)

    def print_stack(self):
        lst = self.stack[::-1]
        for ele in lst:
            print(ele)


if __name__ == '__main__':
    st  = Stack()
    st.add_element(10)
    st.add_element(20)
    st.add_element(30)
    st.add_element(40)
    print("Size = ",st.size())
    st.print_stack()
    print("-------------------------------- pop1 ")
    st.pop_element()
    st.print_stack()
    print("Size = ",st.size())
    print("--------------------------------pop2")
    st.pop_element()
    st.print_stack()
    print("Size = ",st.size())




