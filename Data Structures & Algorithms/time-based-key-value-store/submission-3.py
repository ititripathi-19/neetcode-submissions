class TimeMap:

    def __init__(self):
        self.hashTab = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        hashKeys = self.hashTab.keys()
        if key not in hashKeys:
            self.hashTab[key] = []
        self.hashTab[key].append([timestamp, value])
        #print(self.hashTab)

    def get(self, key: str, timestamp: int) -> str:
        res = ''
        valList = self.hashTab.get(key,[])
        l = 0
        r = len(valList)-1
        while(l<=r):
            m = (l+r)//2
            if valList[m][0] <= timestamp:
                res = valList[m][1]
                l = m+1
            else:
                r = m-1
        return res
