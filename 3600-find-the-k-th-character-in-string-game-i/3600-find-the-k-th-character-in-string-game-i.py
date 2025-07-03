class Solution:
    def kthCharacter(self, k: int) -> str:
        app = ""
        res = "a"

        while len(res) < k:
            for i in range(len(res)):
                a = ord(res[i])
                a += 1
                app += chr(a)
            res += app
            app = ""
        
        return res[k-1]