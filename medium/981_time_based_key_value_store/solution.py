class TimeMap:
    """
    It works but it is not efficient due to the list comprehension in the get method.
    """

    def __init__(self):
        self.kv_store = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.kv_store:
            self.kv_store[key] = [(value, timestamp)]
        else:
            self.kv_store[key].append((value, timestamp))
        
    def get(self, key: str, timestamp: int) -> str:
        if key not in self.kv_store:
            return ""
        else:
            selected_value = [v for (v,t) in self.kv_store[key]]
            selected_time = [t for (v,t) in self.kv_store[key]]

            if timestamp < selected_time[0]:
                return ""

            left = 0
            right = len(selected_time) - 1
            best_ind = left

            while left <= right:
                mid = (left + right)//2

                if selected_time[mid] == timestamp:
                    return selected_value[mid]
                elif selected_time[mid] < timestamp:
                    best_ind = mid
                    left = mid + 1
                elif selected_time[mid] > timestamp:
                    right = mid - 1

            return selected_value[best_ind]
        
class TimeMap_2:
    """
    Get rid of the list comprehension in the get method.
    """

    def __init__(self):
        self.kv_store = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.kv_store:
            self.kv_store[key] = [(value, timestamp)]
        else:
            self.kv_store[key].append((value, timestamp))
        
    def get(self, key: str, timestamp: int) -> str:
        if key not in self.kv_store:
            return ""
        else:
            selected_kv = self.kv_store[key]
            if timestamp < selected_kv[0][1]:
                return ""

            left = 0
            right = len(selected_kv) - 1
            best_ind = left 

            while left <= right:
                mid = (left + right)//2

                if selected_kv[mid][1] == timestamp:
                    return selected_kv[mid][0]
                elif selected_kv[mid][1] < timestamp:
                    # only if the timestamp is less than the target timestamp, we update the best index
                    # due to the question requirement
                    best_ind = mid
                    left = mid + 1
                elif selected_kv[mid][1] > timestamp:
                    right = mid - 1

            return selected_kv[best_ind][0]
        
class TimeMap_NeetCode:
    """
    time complexity: O(1) for set, O(logn) for get
    """
    def __init__(self):
        self.keyStore = {}  # key : list of [val, timestamp]

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.keyStore:
            self.keyStore[key] = []
        self.keyStore[key].append([value, timestamp])
        
    def get(self, key: str, timestamp: int) -> str:
        res, values = "", self.keyStore.get(key, [])
        l, r = 0, len(values) - 1
        while l <= r:
            m = (l + r) // 2
            if values[m][1] <= timestamp:
                res = values[m][0]
                l = m + 1
            else:
                r = m - 1
        return res


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)