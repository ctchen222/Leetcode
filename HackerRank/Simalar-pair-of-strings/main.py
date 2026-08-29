def similarPairs(s, t):
    result = [] # ["YES", "NO", ....] depending on how much pairs we have
    
    for str1, str2 in zip(s, t):
        alpha_num_list = [0] * 26

        for ch in str1:
            alpha_num_list[ord(ch) - ord('a')] += 1

        for ch in str2:
            alpha_num_list[ord(ch) - ord('a')] -= 1

        is_simalar = True
        for diff in alpha_num_list:
            if abs(diff) > 3:
                is_simalar = False

        result.append("YES" if is_simalar else "NO")
    return result

print(similarPairs(["aabaab", "aaaaabb"], ["bbabbc", "abbbbbb"]))
assert(similarPairs(["aabaab", "aaaaabb"], ["bbabbc", "abbbbbb"]))
