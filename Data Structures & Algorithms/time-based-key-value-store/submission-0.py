#alice data structure
#timestamp 1 : set "hello"
#timestamp 3: set "goodbye"
#get alice(2) -> hello
#get alice(1) -> hello
#get alice(3) -> goodbye
#[1,4,7] coming 6

#data structure: list of tuples -> [(1,"hello"),(3,"goodbye")]
from collections import defaultdict
class TimeMap:

    def __init__(self):
        self.data = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        if not self.data[key] or self.data[key][-1][1] != value:
            self.data[key].append((timestamp,value))

    def get(self, key: str, timestamp: int) -> str:
        array = self.data[key]
        l = 0
        r = len(array)

        while l<r:
            m = l + (r-l) // 2

            if array[m][0] <= timestamp:
                l = m + 1
            else:
                r = m

        return array[r-1][1] if r > 0 else ""
        

        
