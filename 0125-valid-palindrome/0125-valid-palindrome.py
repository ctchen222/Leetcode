import re

class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleaned_string = re.sub(r'[^a-zA-Z0-9]', '', s).lower()
        return cleaned_string == cleaned_string[::-1]