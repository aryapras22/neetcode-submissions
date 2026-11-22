class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        symbol_dict = {"(": ")", "{": "}", "[": "]"}

        for symbol in s:
            if symbol in ["(", "{", "["]:
                stack.append(symbol)
            else:
                if len(stack) == 0:
                    return False
                else:
                    item = stack.pop()
                    if symbol_dict[item] != symbol:
                        return False
        return len(stack) == 0
