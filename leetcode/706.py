class LLNode:
    def __init__(self, k, v):
        self.val = (k, v)
        self.next = None

class MyHashMap:

    def __init__(self):
        self.buckets = [None] * (10**5)

    def put(self, key: int, value: int) -> None:
        bucket = self.buckets[self.hsh(key)]
        if not bucket:
            self.buckets[self.hsh(key)] = LLNode(key, value)
        else:
            while bucket:
                if key == bucket.val[0]:
                    bucket.val = (key, value)
                    return
                last_bucket = bucket
                bucket = bucket.next
            last_bucket.next = LLNode(key, value)

    def get(self, key: int) -> int:
        bucket = self.buckets[self.hsh(key)]
        while bucket:
            if key == bucket.val[0]:
                return bucket.val[1]
            bucket = bucket.next
        return -1

    def remove(self, key: int) -> None:
        h = self.hsh(key)
        bucket = self.buckets[h]
        while bucket:
            if key == bucket.val[0]:
                if self.buckets[h] == bucket:
                    self.buckets[h] = bucket.next
                else:
                    last_bucket.next = bucket.next
                break
            last_bucket = bucket
            bucket = bucket.next
        
    def hsh(self, key):
        MOD = len(self.buckets)
        return (key%MOD+MOD)%MOD