class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left, right = 0, 0
        longest = 0
        sett = set()

        for right in range(len(s)):
            while s[right] in sett:
                sett.remove(s[left])
                left += 1
            
            w = (right - left) + 1
            longest = max(w, longest)
            sett.add(s[right])
        
        return longest
