class Solution:
    def reportSpam(self, message: List[str], bannedWords: List[str]) -> bool:
        s = set(bannedWords)
        ct = 0
        for x in message:
            if x in s:
                ct += 1
                if ct == 2:
                    return True
        return False