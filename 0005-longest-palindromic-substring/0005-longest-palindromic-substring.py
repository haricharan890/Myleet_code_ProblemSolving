class Solution:
    def longestPalindrome(self, s: str) -> str:
        def isPalindrome(new):
            if new==new[::-1]:
                return True
            return False
        dup=s[0]
        maxi=0
        n=len(s)
        for i in range(n-1):
            for j in range(i+1,n):
                if isPalindrome(s[i:j+1]):
                    l=len(s[i:j+1])
                    if l>maxi:
                        dup=s[i:j+1]
                        maxi=l
        return dup

        
        