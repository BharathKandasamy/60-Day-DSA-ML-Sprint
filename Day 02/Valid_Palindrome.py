class Solution:
    def isPalindrome(self, s: str) -> bool:
        s1 = ''
        for i in s:
            if i.isalnum():
                s1 += i.lower()
        
        l = 0
        h = len(s1) - 1
        while l < h:
            if s1[l] != s1[h]:
                return False
            l+=1
            h-=1
        return True
