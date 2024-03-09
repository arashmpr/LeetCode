class Solution:
    def minimumRounds(self, tasks: List[int]) -> int:
        count = {}
        for task in tasks:
            if task in count.keys():
                count[task] += 1
            else:
                count[task] = 1
        if 1 in count.values(): return -1
        rounds = 0
        for num in count.values():
            rounds += ((num+2)//3)
        return rounds