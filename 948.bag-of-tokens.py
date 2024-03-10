class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        score = 0
        tokens.sort()
        max_score = 0
        while tokens:
            if score == 0 and power < tokens[0]:
                return max_score
            if tokens[0] <= power:
                power = power - tokens.pop(0)
                score += 1
                if score > max_score:
                    max_score = score
            else:
                power += tokens.pop(-1)
                score -= 1
        return max_score