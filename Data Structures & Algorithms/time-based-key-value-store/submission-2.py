class TimeMap:

    def __init__(self):
        self.map = {}   # map key -> ([value, timestamp])

    #TC: O(1)
    #SC: O(n) for size of hashMap 
    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.map:
            self.map[key] = []
        
        self.map[key].append([value, timestamp])

    #TC: O(log(n)) where n is the number of keys
    #SC: O(m * n) where m is total number of values associated with a key and m is total number of keys
    def get(self, key: str, timestamp: int) -> str:
        values = self.map.get(key, [])
        res = ""
        l, r = 0, len(values) - 1

        while l <= r:
            mid = (l + r) // 2
            if values[mid][1] <= timestamp:
                res = values[mid][0]
                l = mid + 1
            else:
                r = mid - 1
        
        return res
