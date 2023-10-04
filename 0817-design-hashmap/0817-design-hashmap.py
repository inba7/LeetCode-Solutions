class MyHashMap(object):
    def __init__(self):
        self.hashMap = {}
        
    def put(self, key, value):
        self.hashMap[key] = value        

    def get(self, key):
        if key in self.hashMap:
            return self.hashMap.get(key)
        return -1        

    def remove(self, key):
        if key in self.hashMap:
            self.hashMap.pop(key)