class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mapping = {'(' : ')', '{':'}', '[' : ']'}
        for br in s:
            if br in mapping:
                stack.append(br)
            else:
                if stack and mapping[stack[-1]] == br:
                    stack.pop()
                else:
                    return False
        if not stack:
            return True
        else:
            return False                