class Solution:
    def spellchecker(self, wordlist: List[str], queries: List[str]) -> List[str]:
        ans = []
        newlist = []
        vowellist = []
        chng = str.maketrans("aeiou", "*****")

        for word in wordlist:
            newlist.append(word.lower())
            vowellist.append((word.lower()).translate(chng))
        newlist = list(set(newlist))
        vowellist = list(set(vowellist))

        for q in queries:
            if q in wordlist:
                ans.append(q)
            elif q.lower() in newlist:
                for word in wordlist:
                    if word.lower() == q.lower():
                        ans.append(word)
                        break
            elif (q.lower()).translate(chng) in vowellist:
                for word in wordlist:
                    if (word.lower()).translate(chng) == (q.lower()).translate(chng):
                        ans.append(word)
                        break
            else:
                ans.append("")

        return ans