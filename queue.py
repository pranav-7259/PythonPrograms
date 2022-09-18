from collections import deque


class Queue:
    def __init__(self):
        self.buffer = deque()

    def enqueue(self, element):
        return self.buffer.appendleft(element)

    def dequeue(self):
        return self.buffer.pop()

    def size(self):
        return len(self.buffer)

    def is_empty(self):
        return len(self.buffer) == 0


if __name__ == "__main__":
    pq = Queue()
    pq.enqueue(20)
    pq.enqueue(30)
    pq.enqueue(40)

    l = pq.dequeue()

    print(pq.buffer)
