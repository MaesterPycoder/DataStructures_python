# Now we Implement Fixed Size Stack



class Stack:
    def __init__(self,stackSizeLimit):
        self.stack = []
        self.stSize = stackSizeLimit

    def add_element(self, value):
        if self.length()<self.stSize:
            self.stack.append(value)
        else:
            raise Exception("Stack OverFlow")

    def pop_element(self):
        if self.length()>0:
            return self.stack.pop(-1)
        else:
            raise Exception("Stack UnderFlow")



    def length(self):
        return len(self.stack)

    def print_stack(self):
        lst = self.stack[::-1]
        for ele in lst:
            print(ele)



if __name__ == "__main__":
    st = Stack(3)

    print("Size of Stack",st.length())
    st.print_stack()
    print("--------------------------")

    st.add_element(10)
    print("Size of Stack",st.length())
    st.print_stack()

    print("--------------------------")


    # st.add_element(10)
    st.add_element(20)
    st.add_element(30)
    print("Size of Stack",st.length())
    st.print_stack()

    print("--------------------------")


    st.pop_element()
    st.pop_element()
    st.pop_element()
    st.pop_element()
    print("Size of Stack",st.length())
    st.print_stack()