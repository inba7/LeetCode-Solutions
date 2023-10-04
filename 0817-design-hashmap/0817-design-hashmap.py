class MyHashMap(object):
    def __init__(self):
        self.ans = [-1] * 1000001

    def put(self, key, value):
        self.ans[key] = value

    def get(self, key):
        return self.ans[key]

    def remove(self, key):
        self.ans[key] = -1