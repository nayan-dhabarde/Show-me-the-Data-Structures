from collections import OrderedDict


class LRU_Cache(object):
    def __init__(self, capacity):
        # Initialize class variables
        self.cache = OrderedDict()
        self.capacity = capacity
        pass

    def get(self, key):
        if key is None:
            return -1

        if key in self.cache:
            popped_value = self.cache.pop(key)
            self.cache[key] = popped_value
            return popped_value
        else:
            return -1
        # Retrieve item from provided key. Return -1 if nonexistent.
        pass

    def set(self, key, value):
        if self.capacity <= 0:
            return

        # Set the value if the key is not present in the cache. If the cache is at capacity remove the oldest item.
        if len(self.cache) == self.capacity:
            deleted_key = self.cache.popitem(last=False)

        self.cache[key] = value
        pass


# Test case 1: Cache with zero capacity
our_cache = LRU_Cache(0)
our_cache.set(1, 1)
print(our_cache.get(1))
# returns -1 because capacity is zero and thus there are no items

# Test case 2: Cache with capacity without values set
our_cache = LRU_Cache(1)
print(our_cache.get(2))
# returns -1 because value is not present

# Test case 3: Cache with capacity with values set
our_cache = LRU_Cache(5)
our_cache.set(1, 1)
our_cache.set(2, 2)
our_cache.set(3, 3)
our_cache.set(4, 4)


print(our_cache.get(1))
# returns 1

print(our_cache.get(2))
# returns 2

print(our_cache.get(9))
# returns -1 because 9 is not present in the cache

# Test case 4: Recent use
our_cache.set(5, 5)
our_cache.set(6, 6)

print(our_cache.get(3))
# returns -1 because the cache reached it's capacity and 3 was the least recently used entry
