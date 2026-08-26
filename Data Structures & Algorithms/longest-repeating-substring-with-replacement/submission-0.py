class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        res = 0
        count = {}
        l = 0
        maxNum = 0
        for i in range(len(s)):
            count[s[i]] = 1 + count.get(s[i], 0)
            maxNum = max(maxNum, count[s[i]])
            while (i - l + 1) - maxNum > k:
                count[s[l]] -= 1
                l += 1
            res = max(res, i - l + 1)
        return res