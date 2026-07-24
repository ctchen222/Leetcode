https://www.coderbyte.com/editor/Min%20Window%20Substring:Python3
Difficulty: Medium

## Critical thinking
This is a classic sliding window problems from the term like "substring" and "window". The brute force solution is to use two nested loops to check all possible substrings, but that would be inefficient. Instead, we can use a sliding window approach to keep track of the current substring and its length. We can expand the window by adding characters to the right and contract it by removing characters from the left, while keeping track of the maximum length of valid substrings found so far. This way, we can achieve an O(n) time complexity solution.
The tricky part is when you start remove characters from the left, you need to make sure that the substring is still valid which means you need to check if the character being removed is still part of the current substring. Which you can check by using a hash map to keep track of the count of each character in the current substring. If the count of a character becomes zero, it means that character is no longer part of the current substring and you can safely remove it from the hash map.

## Complexity
### Time complexity: **O(N + K)** / **O(N)**. (K often < N)
N is the length of the input string and K is the number of unique characters in the input string. The sliding window approach ensures that we only traverse the string once, and the hash map operations (insert, delete, lookup) are O(1) on average.
### Space complexity: **O(K)**. 
The hash map will store at most K unique characters, where K is the number of unique characters in the input string. In the worst case, all characters are unique, so the space complexity is O(K).

## Further optimization
### 1. Code Optimization
- If the character set is fixed (e.g., only ASCII letters), use an array (list) instead of a dictionary for faster lookups.
- Only update the answer when `formed == required` to avoid unnecessary comparisons.
- Use `collections.defaultdict(int)` to simplify code and avoid repeated `.get()` calls.
- Return early if `t` is longer than `s`, or if `t` contains characters not present in `s`.
- Refactor the code into smaller functions for initialization, main loop, and window contraction to improve readability and maintainability.

### 2. Handling Large Data
- For very large `s` (hundreds of MB), consider reading in chunks. (Note: For this problem, splitting is not trivial since the window may cross chunk boundaries.)
- If `s` is a stream, use a sliding window approach, but ensure the window size does not exceed memory limits.
- Use arrays instead of dictionaries and only track characters present in `t`.
- For extreme performance, consider multi-threading or distributed processing, but be careful with merging results across window boundaries.
- Set limits on maximum window length or computation time to avoid OOM (out-of-memory) or timeouts.

### 3. API Design Considerations
- Validate input types, lengths, and contents; return clear error messages for invalid input.
- Use try/except blocks to catch exceptions and return standardized error formats.
- Set a maximum input length to prevent resource exhaustion or denial-of-service attacks.
- Return results in a standard JSON format, e.g., `{"result": "aksfajee", "error": null}`.
- Log request parameters, execution time, and errors for monitoring and debugging.
- Write comprehensive unit and stress tests to cover all scenarios and performance.
- Provide clear API documentation, including specifications, input/output examples, and error formats.
