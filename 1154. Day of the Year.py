class Solution:
    
    def dayOfYear(self, date: str) -> int:
        def leapDay(y, m):
            if m <=2:
                return 0
            if y%4 == 0:
                if y%100==0 and y%400!=0:
                    return 0
                else:
                    return 1
            else:
                return 0
            
        monthDays = [0,31,28,31,30,31,30,31,31,30,31,30,31]
        for i in range(1, 13):
            monthDays[i] += monthDays[i-1]
        
        print(date)
        y, m, d = list(map(int, date.split('-')))
        
        return leapDay(y, m) + monthDays[m-1] + d
