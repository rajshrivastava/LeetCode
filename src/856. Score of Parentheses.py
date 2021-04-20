class Solution:
    def scoreOfParentheses(self, S: str) -> int:
        pwr = 0
        final_score = 0
        for i in range(1, len(S)):
            if S[i] == '(':
                pwr += 1
            else:
                if S[i-1] == '(':
                    final_score += 2**pwr
                pwr -= 1
        return final_score
