from collections import defaultdict

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        m = defaultdict(int)
        left = 0
        right = 0
        res = 0

        while right < len(s):
            while left < right and s[right] in m:
                res = max(res, right - left)
                m[s[left]] -= 1
                if m[s[left]] == 0:
                    del m[s[left]]
                left += 1
            m[s[right]] += 1
            right += 1

        res = max(res, right - left)
        return res   
        