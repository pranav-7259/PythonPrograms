from collections import deque


class Stack:
    def __init__(self):
        self.container = deque()

    def push(self, element):
        return self.container.append(element)

    def pop(self):
        return self.container.pop()

    def peek(self):
        return self.container[-1]

    def size(self):
        return len(self.container)


def is_balanced(param):
    d = {')': '(', ']': '[', '}': '{'}
    st = Stack()

    for ch in param:
        if ch in d:
            if st.size() == 0:
                return False
            if d[ch] == st.peek():
                st.pop()

        if ch in d.values():
            st.push(ch)

    return st.size() == 0


if __name__ == '__main__':
    s = Stack()
    sentence = "My name is Pranav"

    for c in sentence:
        s.push(c)

    reverse_str = ""

    while s.size() != 0:
        reverse_str += s.pop()

    print(reverse_str)

    print(is_balanced("({a+b})"))
    print(is_balanced("))((a+b}{"))
    print(is_balanced("((a+b))"))
    print(is_balanced("((a+g))"))
    print(is_balanced("))"))
    print(is_balanced("[a+b]*(x+2y)*{gg+kk}"))
