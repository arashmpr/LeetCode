from collections import defaultdict 

class Solution:
    def customSortString(self, order: str, s: str) -> str:
        res = ""
        freq = defaultdict(str)
        for w in s:
            freq[w] += w
        for w in order:
            if w in s:
                res += freq[w]
        
        for w in s:
            if w not in order:
                res += w
        return res
        