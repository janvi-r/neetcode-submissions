class Solution:
    def firstUniqChar(self, s: str) -> int:
        res = n = len(s)
        for ch in range(ord('a'), ord('z') + 1):
            index = s.find(chr(ch))
            if index != -1 and s.rfind(chr(ch)) == index:
                res = min(res, index)

        return -1 if res == n else res
            
        