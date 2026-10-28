class Solution:
    def isHappy(self, n: int) -> bool:
        maps =[]
        total = sum(int(d)**2 for d in str(n))

        while total != 1:
            if total not in maps:
                maps.append(total)
            else:
                return False
            strr = [int(d) for d in str(total)]
            total = sum(int(d)**2 for d in strr)
        return True
        