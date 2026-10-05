'''
Submitted: October 5, 2026

Runtime: 0ms, beats 100%

Memory: 19,29mb, beats 73,95%
'''

class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        if not strs:
            return ""
        base = strs[0]
        for i in range(len(base)):
            char = base[i]
            for word in strs[1:]:
                if i == len(word) or word[i] != char:
                    return base[:i]
                    
        return base
