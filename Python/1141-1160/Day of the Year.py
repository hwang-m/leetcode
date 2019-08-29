class Solution:
    def dayOfYear(self, date: str) -> int:
        year, month, day = [int(x) for x in date.split('-')]
        mo_days = [31,28,31,30,31,30,31,31,30,31,30,31]
        for m in range(month-1):
            day += mo_days[m]
        if month > 2:
            if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
                day += 1
        return day
