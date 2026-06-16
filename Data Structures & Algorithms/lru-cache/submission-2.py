class Node:
    def __init__(self, key:int, value:int):
        self.key = key 
        self.value = value
        self.next = None 
        self.prev = None 
class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity 
        self.cache_map = {}

        self.head = Node(0,0)
        self.tail = Node(0,0)
        self.head.next = self.tail
        self.tail.prev = self.head 
    def insert(self, node):
        curr_first = self.head.next 

        node.prev = self.head 
        node.next = curr_first 

        self.head.next = node 
        curr_first.prev = node
    def remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev
    def get(self, key: int) -> int:
        if key in self.cache_map:
            node = self.cache_map[key]
            self.remove(node)
            self.insert(node)
            return node.value 
        else:
            return -1
    def put(self, key: int, value: int) -> None:
        if key in self.cache_map:
            node = self.cache_map[key]  
            node.value = value 
            self.remove(node)
            self.insert(node)
        else:
            new_node = Node(key, value)
            self.cache_map[key] = new_node 
            self.insert(new_node)
            if len(self.cache_map) > self.capacity:
                victim_node = self.tail.prev 
                del self.cache_map[victim_node.key]
                self.remove(victim_node)
            

        
