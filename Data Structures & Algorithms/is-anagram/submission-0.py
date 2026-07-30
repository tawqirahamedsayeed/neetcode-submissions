class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        a={}
        b={}
        for i in  range(len(s)):
            if s[i] not in a:
                a[s[i]] = 1
            else:
                 a[s[i]] += 1
        
        for i in range(len(t)):
            if t[i] not in b:
                 b[t[i]] = 1
            else:
                b[t[i]] += 1

        if a==b:
            return True
        else:
            return False