def MinWindowSubstring(strArr):
  s = strArr[0]
  t = strArr[1]

  # Count required characters
  need = {}
  for c in t:
      need[c] = need.get(c, 0) + 1

  required = len(need)
  formed = 0
  window = {}

  left = 0
  min_len = float("inf")
  ans = ""

  for right in range(len(s)):
    c = s[right]
    window[c] = window.get(c, 0) + 1

    if c in need and window[c] == need[c]:
      formed += 1

      while formed == required:
        if right - left + 1 < min_len:
          min_len = right - left + 1
          ans = s[left:right + 1]
        
        left_char = s[left]
        window[left_char] -= 1
        
        if left_char in need and window[left_char] < need[left_char]:
          formed -= 1
        left += 1

  return ans
  
# keep this function call here 
print(MinWindowSubstring(["ahffaksfajeeubsne", "jefaa"])) # Output: aksfaje
assert MinWindowSubstring(["ahffaksfajeeubsne", "jefaa"]) == "aksfaje"
assert MinWindowSubstring(["aaffhkksemckelloe", "fhea"]) == "affhkkse"
