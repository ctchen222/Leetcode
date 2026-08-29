# No Pairs Allowed

You are given a list of words.

For each word, determine the minimum number of character replacements required so that no two adjacent characters are the same.

You may replace any character with any other character.

## Task

Return an array where each element represents the minimum number of replacements needed for the corresponding word.

## Example

```text
words = ["ab", "aab", "abb", "abab", "abaaaba"]
output = [0, 1, 1, 0, 1]
```

### Explanation

- `"ab"`: no change needed, so the answer is `0`
- `"aab"`: change one `'a'`, so the answer is `1`
- `"abb"`: change one `'b'`, so the answer is `1`
- `"abab"`: no change needed, so the answer is `0`
- `"abaaaba"`: change the middle `'a'`, so the answer is `1`

## Constraints

- `1 <= n <= 100`
- `2 <= length of words[i] <= 10^5`
- Each character in `words[i]` is in the range `ascii[a-z]`

## Input Format

```text
The first line contains an integer, n.
The next n lines each contain a string element of words.
```
