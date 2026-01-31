class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        arr = set(letters)
        arr = sorted(list(arr))
        x = ord(target)
        
        if x >= ord(arr[-1]):
            return arr[0]

        for i in arr:
            if ord(i) > x:
                return i
