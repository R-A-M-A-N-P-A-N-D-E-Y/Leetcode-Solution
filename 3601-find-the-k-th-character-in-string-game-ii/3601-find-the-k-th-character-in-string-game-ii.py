class Solution:
    def kthCharacter(self, k: int, operations: List[int]) -> str:
        def helper(k, ops):
            if not ops:
                return 'a'  # base case

            last_op = ops[-1]
            prev_len = 1
            for op in ops[:-1]:
                if op == 0:
                    prev_len *= 2
                else:
                    prev_len *= 2  # since incremented part is same length

            if last_op == 0:
                if k <= prev_len:
                    return helper(k, ops[:-1])
                else:
                    return helper(k - prev_len, ops[:-1])
            else:  # increment
                if k <= prev_len:
                    return helper(k, ops[:-1])
                else:
                    c = helper(k - prev_len, ops[:-1])
                    return 'a' if c == 'z' else chr(ord(c) + 1)

        return helper(k, operations)