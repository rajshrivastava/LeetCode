class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        n = len(palindrome)
        if n == 1:
            return ''

        for i in range(n//2):
            if palindrome[i] !='a':
                # if n%2!=1 or i != n//2:
                return palindrome[:i] + 'a' + palindrome[i+1:]
                   
        return palindrome[:-1] + 'b'
