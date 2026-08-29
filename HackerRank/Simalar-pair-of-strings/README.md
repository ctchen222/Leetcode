# Similar Pairs of Strings

You are given two arrays of strings, `s` and `t`, each of length `n`.

Each pair `(s[i], t[i])` contains two lowercase English strings.

Two strings are considered similar if, for every letter `x` from `'a'` to `'z'`, the absolute difference between the number of times `x` appears in the two strings is at most `3`.

## Task

For each pair `(s[i], t[i])`, determine whether the two strings are similar.

Return an array of `n` elements where:

- `YES` if the pair is similar
- `NO` otherwise

## Example

```text
s = ["aabaab", "aaaaabb"]
t = ["bbabbc", "abbbbbb"]
output = ["YES", "NO"]
```

### Explanation

For the first pair:

```text
s[0] = "aabaab"
t[0] = "bbabbc"
```

The character counts are:

| letter | s[0] count | t[0] count | difference |
| --- | ---: | ---: | ---: |
| a | 4 | 1 | 3 |
| b | 2 | 4 | 2 |
| c | 0 | 1 | 1 |

Every difference is at most `3`, so the answer is `YES`.

For the second pair:

```text
s[1] = "aaaaabb"
t[1] = "abbbbbb"
```

The character counts are:

| letter | s[1] count | t[1] count | difference |
| --- | ---: | ---: | ---: |
| a | 5 | 1 | 4 |
| b | 2 | 6 | 4 |

The differences for `a` and `b` are greater than `3`, so the answer is `NO`.

## Constraints

- `1 <= n <= 5`
- `1 <=` length of any input string `<= 10^5`

## Input Format

```text
The first line contains an integer, `n`.
The next `n` lines each contain a string element of `s`.
The next line contains an integer, `n`.
The next `n` lines each contain a string element of `t`.
```
