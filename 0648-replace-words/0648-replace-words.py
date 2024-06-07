class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        ls = sentence.split(" ")
        
        for i in range(len(ls)):
            small = 1000
            for pre in dictionary:
                if ls[i].startswith(pre):
                    if small > len(pre):
                        ls[i] = pre
                        small = len(pre)


        return " ".join(ls)