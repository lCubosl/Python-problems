# LRU cache
# Implement the Least Recently Used LRU cache class. the class should support the following
# LRU cache, initialize of size "capacity"
# "int get(int key)" return the value corresponding to the key if the key exists otherwhise return -1
# "void put(int key, int value)" Update the value of the key if the key exists Otherwise add the key-value
# to the cache. If the introduction of the new pair causes the cache to exceed its capacity,
# remove the least recently used key
# a key is considered used if a "get" or a "put" operation is called on it

# hash map O(n)
class Node:
  def __init__(self, key, val):
    self.key, self.val = key, val
    self.prev = self.next = None

class LRUCache:
  def __init__(self, capacity):
    self.cap = capacity
    self.cache = {}

    # l_lru = left LRU, r_mru = right MRU
    self.l_lru, self.r_mru = Node(0, 0), Node(0, 0)
    self.l_lru.next, self.r_mru.prev = self.r_mru, self.l_lru
  
  def remove(self, node):
    prev, nxt = node.prev, node.next
    prev.next, nxt.prev =  nxt, prev

  def insert(self, node):
    prev, nxt = self.r_mru.prev, self.r_mru
    prev.next = nxt.prev = node
    node.next, node.prev = nxt, prev
    
  def get(self, key:int):
    if key in self.cache:
      self.remove(self.cache[key])
      self.insert(self.cache[key])
      return self.cache[key].val
    return -1

  def put(self, key:int, value:int):
    if key in self.cache:
      self.remove(self.cache[key])
    self.cache[key] = Node(key, value)
    self.insert(self.cache[key])

    if len(self.cache) > self.cap:
      lru = self.l_lru.next
      self.remove(lru)
      del self.cache[lru.key]

# run leetcode in vs code
commands = ["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"]
args = [[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]

results = []
lru = None

for cmd, arg in zip(commands, args):
    if cmd == "LRUCache":
        lru = LRUCache(*arg)
        results.append(None)
    elif cmd == "put":
        lru.put(*arg)
        results.append(None)
    elif cmd == "get":
        res = lru.get(*arg)
        results.append(res)

print(results)