class LRUCache:

    def __init__(self, capacity: int):
        self.hmap = {}
        self.size = capacity

    def get(self, key: int) -> int:
        #print(self.hmap)
        if key in self.hmap:
            val = self.hmap[key]
            del self.hmap[key]
            self.hmap[key] = val
            return val
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.hmap:
            del self.hmap[key]
            self.hmap[key] = value
        else:
            if len(self.hmap) < self.size:
                self.hmap[key] = value
            else:
                self.hmap.pop(next(iter(self.hmap)))
                self.hmap[key] = value

