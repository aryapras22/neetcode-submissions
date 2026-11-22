class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for i in range(len(s)):
            if s[i] in ["{", "(", "["]:
                stack.append(s[i])
            else:
                if len(stack) == 0:
                    return False
                match s[i]:
                    case ")":
                        key = "("
                    case "}":
                        key = "{"
                    case "]":
                        key = "["  
                out = stack[-1]
                if out == key:
                    stack.pop()
                else:
                    return False
        
        return len(stack) == 0