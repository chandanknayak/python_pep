class ArrayQueue:
    def __init__(self):
        self._data = [None] * 1
        self._size = 0
        self._front = 0

    def __len__(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    def first(self):
        if self.is_empty():
            raise Exception("Queue is empty")
        return self._data[self._front]

    def enqueue(self, e):
        if self._size == len(self._data):
            self._resize(2 * len(self._data))
        avail = (self._front + self._size) % len(self._data)
        self._data[avail] = e
        self._size += 1

    def dequeue(self):
        if self.is_empty():
            raise Exception("Queue is empty")
        answer = self._data[self._front]
        self._data[self._front] = None
        self._front = (self._front + 1) % len(self._data)
        self._size -= 1
        if 0 < self._size < len(self._data) // 4:
            self._resize(len(self._data) // 2)
        return answer

    def _resize(self, cap):
        old = self._data
        self._data = [None] * cap
        walk = self._front
        for k in range(self._size):
            self._data[k] = old[walk]
            walk = (walk + 1) % len(old)
        self._front = 0


if __name__ == "__main__":
    q = ArrayQueue()
    q.enqueue(10)
    q.enqueue(20)
    q.enqueue(30)
    print(q.first())
    print(q.dequeue())
    print(q.first())
    print(len(q))
    print(q.dequeue())
    print(q.dequeue())
    print(q.is_empty())

    