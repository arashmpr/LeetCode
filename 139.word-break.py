class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        if s == "":
            return True
        memo = {}
        return self.dp(s, wordDict, memo)
    
    def dp(self, target, wordDict, memo={}):
        if target in memo.keys(): return memo[target]
        if target == "": return True

        for word in wordDict:
            if word in target:
                if target.index(word) == 0:
                    if self.dp(target[len(word):], wordDict, memo):
                        memo[target] = True
                        return True
        
        memo[target] = False
        return False
        