class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        n = len(speed)
        hmap = {}
        stack = []
        for i in range(n):
            hmap[position[i]] = (target - position[i]) / speed[i]
        hmap = dict(sorted(hmap.items(), reverse=True)) 
        for p in hmap:
            stack.append(hmap[p])
            #print(stack)
            if len(stack)>=2 and stack[-1] <= stack[-2]:
                stack.pop()
        return len(stack)