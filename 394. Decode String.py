class Solution:
    def decodeString(self, s: str) -> str:
        counts = []
        strings = []
        
        curr_num = 0
        curr_s = ''
        for ch in s:
            if ch.isdigit():
                curr_num = curr_num*10 + int(ch)
            elif ch.isalpha():
                curr_s += ch
            elif ch == '[':
                counts.append(curr_num)
                strings.append(curr_s)
                curr_num= 0
                curr_s = ''
            else:
                curr_s = strings.pop() + curr_s*counts.pop()
               
        return curr_s
