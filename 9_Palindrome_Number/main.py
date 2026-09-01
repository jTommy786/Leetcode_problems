""""
Submitted: September 1st, 2026

Runtime: 11ms, beats 36,97%

Memory: 19,43mb, beats 19,35%
"""

class Solution:
    def isPalindrome(self, x: int) -> bool:
        y = x
        digits = []
        if x<0:
            return False
        elif x == 0:
            return True
        else:
            while x>0:
                res = x % 10
                digits.append(res)
                x = x//10
            final = int("".join(map(str, digits)))
            if final == y:
                return True
            else:
                return False