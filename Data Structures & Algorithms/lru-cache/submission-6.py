'''Straight forward approach is implementing this with HashMap and Doubly Linkedlist
TC: O(1) 
SC: O(c) where is the capacity of the cache
'''

class Node:
    def __init__(self, key=0, val=0):
        self.key = key
        self.val = val
        self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {}     # key -> node

        # left=lru, right=the most recent
        self.left, self.right = Node(0, 0), Node(0, 0)
        self.left.next, self.right.prev = self.right, self.left

    # remove from the left
    def remove(self, node: Node):
        prev, nxt = node.prev, node.next
        prev.next, nxt.prev = nxt, prev

    # insert to the right
    def insert(self, node: Node):
        prev, nxt = self.right.prev, self.right
        prev.next = nxt.prev = node
        node.prev, node.next = prev, nxt

    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        self.cache[key] = Node(key, value)
        self.insert(self.cache[key])

        if len(self.cache) > self.cap:
            lru = self.left.next
            self.remove(lru)
            del self.cache[lru.key]





