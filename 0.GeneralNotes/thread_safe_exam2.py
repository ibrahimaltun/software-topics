import threading


class Counter:
    def __init__(self):
        self.value = 0
        self._lock = threading.Lock()

    def increment(self):
        # Kritik bölgeyi kilitleyip güvenli şekilde güncelliyoruz
        with self._lock:
            self.value += 1


def worker(counter, times):
    for _ in range(times):
        counter.increment()


if __name__ == "__main__":
    c = Counter()
    n_threads = 10
    increments_per_thread = 10000

    threads = [threading.Thread(target=worker, args=(
        c, increments_per_thread)) for _ in range(n_threads)]

    for t in threads:
        t.start()

    for t in threads:
        t.join()

    print("Beklenen:", n_threads * increments_per_thread)
    print("Gerçek:", c.value)
