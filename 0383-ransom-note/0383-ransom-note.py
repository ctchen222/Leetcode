class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        Hash_Map = {}
        for word in magazine:
            if word not in Hash_Map:
                Hash_Map[word] = 1
            else:
                Hash_Map[word] += 1
        for word in ransomNote:
            if word in Hash_Map and Hash_Map[word] != 0:
                Hash_Map[word] -= 1
            else:
                return False
        return True