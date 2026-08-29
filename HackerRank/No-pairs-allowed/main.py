def minimalOperations(words):
    result = []
    for word in words:
        changes = 0
        i = 0
        
        while i < len(word) - 1:
            if word[i] == word[i + 1]:
                changes += 1
                i += 2
            else:
                i += 1
        result.append(changes)
    return result

assert(minimalOperations(["ab", "aab", "abb", "abab", "abaaaba"]))
assert(minimalOperations(['aabbc']))
