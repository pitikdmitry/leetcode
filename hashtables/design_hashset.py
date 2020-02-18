'''
Design a HashSet without using any built-in hash table libraries.

To be specific, your design should include these functions:

add(value): Insert a value into the HashSet.
contains(value) : Return whether the value exists in the HashSet or not.
remove(value): Remove a value in the HashSet. If the value does not exist in the HashSet, do nothing.
'''


class MyHashSet:
    START_SIZE = 1000

    def __init__(self) -> None:
        self._arr = [[] for _ in range(self.START_SIZE)]

    def hash(self, key: int) -> int:
        idx = key ** 2 % self.START_SIZE
        return idx

    def add(self, key: int) -> None:
        idx = self.hash(key)
        bucket_arr = self._arr[idx]
        bucket_arr.append(key)

    def remove(self, key: int) -> None:
        idx = self.hash(key)
        bucket_arr = self._arr[idx]
        self._arr[idx] = list(filter(lambda x: x != key, bucket_arr))

    def contains(self, key: int) -> bool:
        idx = self.hash(key)
        bucket_arr = self._arr[idx]
        if key in bucket_arr:
            return True
        return False

# Your MyHashSet object will be instantiated and called as such:
obj = MyHashSet()
obj.add(3)
obj.remove(2)
param_3 = obj.contains(3)
