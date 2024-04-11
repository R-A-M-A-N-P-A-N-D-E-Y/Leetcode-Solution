class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack = []

        for digit in num:
            while k > 0 and len(stack) != 0 and digit < stack[-1]:
                stack.pop()
                k -= 1
            if len(stack) == 0 and digit == '0':
                continue
            stack.append(digit)

        while k > 0 and len(stack) != 0:
            stack.pop()
            k -= 1

        return '0' if len(stack) == 0 else ''.join(stack)