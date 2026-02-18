import threading
import time

lock_a = threading.Lock()
lock_b = threading.Lock()


def thread1():
    with lock_a:
        time.sleep(0.1)
        with lock_b:
            print("Thread1 acquired both")


def thread2():
    with lock_b:
        time.sleep(0.1)
        with lock_a:
            print("Thread2 acquired both")


if __name__ == "__main__":
    t1 = threading.Thread(target=thread1)
    t2 = threading.Thread(target=thread2)

    t1.start()
    t2.start()

    t1.join(timeout=1)
    t2.join(timeout=1)

    print("Done (may be deadlocked)")
