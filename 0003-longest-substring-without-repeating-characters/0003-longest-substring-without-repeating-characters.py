class Solution:
    def lengthOfLongestSubstring(self, st: str) -> int:
        n=len(st)
        d=[-1]*256
        left=right=0
        length=0
        for right in range(n):
            if d[ord(st[right])]!=-1:
                left=max(left,d[ord(st[right])]+1)
            d[ord(st[right])]=right
            length=max(length,right-left+1)
        return length