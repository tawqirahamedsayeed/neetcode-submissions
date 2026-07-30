class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pa = {")":"(", "]":"[", "}":"{"}

        for i in s:
            if i in pa:
                if stack and stack[-1] == pa[i]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(i)
        
        return True if not stack else False

        