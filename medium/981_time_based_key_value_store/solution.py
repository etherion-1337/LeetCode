class TimeMap:
    """
    It works but it is not efficient.
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


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)