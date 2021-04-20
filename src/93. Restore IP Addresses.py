class Solution:
    def getIP(self, cum_s, s, level):
        if level > 2:
            if len(s) > 1 and s[0] == '0':
                return
            try:
                if 0<=int(s)<=255:
                    self.valid_ips.append(cum_s + s)
            except ValueError:
                pass               
            return

        level+=1
        if s:
            self.getIP(cum_s + s[0] + '.', s[1:], level)
        else:
            return
        
        if s[0]!='0':
            if len(s) > 1 and 0<=int(s[:2])<=255:
                self.getIP(cum_s + s[:2] + '.' , s[2:], level)

            if len(s) > 2 and 0<=int(s[:3])<=255:
                self.getIP(cum_s + s[:3] + '.', s[3:], level)

    def restoreIpAddresses(self, s: str) -> List[str]:
        self.valid_ips = []
        self.getIP('', s, 0)
        return self.valid_ips
        
