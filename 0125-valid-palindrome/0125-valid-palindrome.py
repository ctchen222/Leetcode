class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        cleaned_string = re.sub(r'[^a-zA-Z0-9]', '', s).lower()
        return cleaned_string == cleaned_string[::-1]