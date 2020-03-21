class LRUCache:
    def __init__(self, capacity: int):
        self.storage = collections.OrderedDict()
        self.capacity = capacity

    def get(self, key: int) -> int:
        if key in self.storage:
            self.storage.move_to_end(key)
            return self.storage[key]
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.storage:
            self.storage[key] = value
            self.storage.move_to_end(key)
        else:
            if self.capacity == len(self.storage):
                self.storage.popitem(last=False)
                self.storage[key] = value
            else:
                self.storage[key] = value
