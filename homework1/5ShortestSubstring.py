# Technique: variable-size (shrinking/growing) sliding window
# Time complexity: O(n^2 * m)
# Space complexity: O(m)
# What was the ideal solution? I could not think of something more efficient within the 40 minutes.

import math

def shortest_substring(str, target):
    target_list = list(target)
    min = math.inf

    # Check all substrings
    for start in range(len(str)):
        for end in range(start, len(str)):
            if check_substring(str, target_list[:], start, end):
                curr_len = end - start + 1
                if curr_len < min: min = curr_len
    
    if min == math.inf: return("String does not contain all the required characters.")
    return min

# Check if substring contains target characters (with a copy of target array)
def check_substring(str, target, start, end):
    for i in range(start, end + 1):
        if str[i] in target:
            target.remove(str[i])
    
    return target == []

def main():
    input_1A = "abracadabra" # Expected output: 4
    input_2A = "zxycbaabcdwxyzzxwdcbxyzabccbazyx" # Expected output: 10
    input_3A = "dog" # Expected output: 3
    input_4A = "abcd" # Expected output: String does not contain all the required characters.
    
    input_1B = "abc"
    input_2B = "zzyzx"
    input_3B = "god"
    input_4B = "efg"

    print(shortest_substring(input_1A, input_1B))
    print(shortest_substring(input_2A, input_2B))
    print(shortest_substring(input_3A, input_3B))
    print(shortest_substring(input_4A, input_4B))

if __name__ == "__main__":
    main()

# Time: 40 minutes (30 for base idea + 10 for improvement)