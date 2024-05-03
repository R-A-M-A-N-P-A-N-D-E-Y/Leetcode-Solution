class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        v1 = version1.split(".")
        v2 = version2.split(".")

        while len(v1) != 0 and int(v1[-1]) == 0:
            v1.pop() 

        while len(v2) != 0 and int(v2[-1]) == 0:
            v2.pop()

        # print(v1, v2)

        while len(v1) != 0 and len(v2) != 0:
            if int(v1[0]) == int(v2[0]):
                v1.remove(v1[0])
                v2.remove(v2[0])
            elif int(v1[0]) > int(v2[0]):
                return 1
            elif int(v1[0]) < int(v2[0]):
                return -1
        
        if len(v1) == 0 and len(v2) == 0:
            return 0
        elif len(v1) == 0:
            return -1
        elif len(v2) == 0:
            return 1