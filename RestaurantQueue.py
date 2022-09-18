import time
import threading
from collections import deque


class Queue:
    def __init__(self):
        self.buffer = deque()

    def enqueue(self, val):
        return self.buffer.appendleft(val)

    def dequeue(self):
        return self.buffer.pop()

    def is_empty(self):
        return len(self.buffer) == 0

    def size(self):
        return len(self.buffer)


food_orders = Queue()


def PlaceOrder(orders):
    for order in orders:
        print("Placing order: ", order)
        food_orders.enqueue(order)
        time.sleep(0.5)


def ServeOrder():
    time.sleep(1)
    while not food_orders.is_empty():
        print("Serving Order: ", food_orders.dequeue())
        time.sleep(2)


if __name__ == '__main__':
    orders = ["Chicken Chilly", "Fried Rice", "Naan", "Paneer Curry"]
    t1 = threading.Thread(target=PlaceOrder(orders))
    t2 = threading.Thread(target=ServeOrder())

    t1.start()
    t2.start()
