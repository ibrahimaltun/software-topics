import threading
import queue
import time
import random


def producer(q, count):
    for i in range(count):
        item = f"item-{i}"
        q.put(item)  # queue.put thread-safe
        print("Produced", item)
        time.sleep(random.random() * 0.1)
    q.put(None)  # sentinel: üretimin bittiğini bildir


def consumer(q, name):
    while True:
        item = q.get()  # thread-safe, bloklar
        if item is None:
            q.put(None)  # diğer tüketiciler için bırak
            break
        print(name, "consumed", item)
        q.task_done()


if __name__ == "__main__":
    q = queue.Queue()
    prod = threading.Thread(target=producer, args=(q, 10))
    cons = threading.Thread(target=consumer, args=(q, "C1"))

    prod.start()
    cons.start()

    prod.join()
    cons.join()
