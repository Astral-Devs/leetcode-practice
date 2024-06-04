def isValid(self, s: str) -> bool:
        stack = []
        pairings = {
            ')': '(',
            ']': '[',
            '}': '{',
        }

        for l in s:
            if l in '({[':
                stack.append(l)
            else:
                if not stack or pairings[l] != stack[-1]:
                    return False
                stack.pop()

        return len(stack) == 0
