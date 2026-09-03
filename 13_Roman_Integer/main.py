'''
Submitted: September 3, 2026

Runtime: 5ms, beats 51,81%

Memory: 19,14mb, beats 89,58%
'''


class Solution:
    def romanToInt(self, s: str) -> int:
        result = 0
        for i in range(len(s)):
            if s[i] == "I":
                if s[i:i+2] == 'IV':
                    result-=1
                elif s[i:i+2] == 'IX':
                    result-=1
                else:
                    result+=1
            if s[i]=='V':
                result+=5
            if s[i]=='X':
                if s[i:i+2] == 'XL':
                    result-=10
                elif s[i:i+2] == 'XC':
                    result-=10
                else:
                    result+=10
            if s[i]=='L':
                result+=50
            if s[i]=='C':
                if s[i:i+2] == 'CD':
                    result-=100
                elif s[i:i+2] == 'CM':
                    result-=100
                else:
                    result+=100
            if s[i]=='D':
                result+=500
            if s[i]=='M':
                result+=1000
        return result