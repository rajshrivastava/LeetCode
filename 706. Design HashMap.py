class Bucket():
    def __init__(self):
        self.bucket = []
        
    def update(self, key, value):
        for i, k_v in enumerate(self.bucket):
            if k_v[0] == key:
                self.bucket[i] = (key, value)
                return
        
        self.bucket.append((key, value))
                
        
    def get(self, key):
        for k, v in self.bucket:
            if k == key:
                return v
        return -1
        
    def remove(self, key):
        for i, k_v in enumerate(self.bucket):
            if k_v[0] == key:
                del self.bucket[i]
                return
                
class MyHashMap:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        #using chaining
        self.size = 1000
        self.hash_table = [Bucket() for i in range(self.size)]
        
    def hashIt(self, num):
        return num%self.size
    
    def put(self, key: int, value: int) -> None:
        """
        value will always be non-negative.
        """
        h = self.hashIt(key)
        self.hash_table[h].update(key, value)
                   
    def get(self, key: int) -> int:
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        """
        h = self.hashIt(key)
        
        return self.hash_table[h].get(key)        

    def remove(self, key: int) -> None:
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        """
        h = self.hashIt(key)
        
        self.hash_table[h].remove(key)
        
# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)
