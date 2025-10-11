class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        longest = 0
        l = 0
        sett = set()
        
        for r in range(len(s)):
            while s[r] in sett:
                sett.remove(s[l])
                l += 1
            
            w = r - l + 1
            sett.add(s[r])
            longest = max(longest, w)
        
        return longest