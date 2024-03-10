from collections import defaultdict
class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        temp = set()
        for s, d in edges:
            if s in temp:
                return s
            if d in temp:
                return d
            temp.add(s)
            temp.add(d)