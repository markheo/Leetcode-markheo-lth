class Solution:
    def longestPalindrome(self, s: str) -> str:
        last = len(s)
        num = 1
        if s == s[::-1]:
            return s
        else:
            while num < last:
                num += 1
                lst = []
                for i in range(num):
                    lst.append(s[i:last-num+1+i])
                for subs in lst:
                    if subs == subs[::-1]:
                        return subs
                        break