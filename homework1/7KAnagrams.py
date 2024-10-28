# Technique: two arrays/strings two-pointer
# Time complexity: O(n)
# Space complexity: O(n)

from collections import Counter

def k_anagram(str_1, str_2, k):
    if len(str_1) != len(str_2): return False

    # Count frequency of each character in both strings
    count_1 = Counter(str_1)
    count_2 = Counter(str_2)

    changes = 0
    for char in count_1:
        if count_1[char] > count_2.get(char, 0):
            changes += count_1[char] - count_2.get(char, 0)
    
    return changes <= k

def main():
    input_1A = "apple" # Expected output: False
    input_2A = "apple" # Expected output: True
    input_3A = "cat" # Expected output: True
    input_4A = "debit curd" # Expected output: True
    input_5A = "baseball" # Expected output: False
    
    input_1B = "peach"
    input_2B = "peach"
    input_3B = "dog"
    input_4B = "bad credit"
    input_5B = "basketball"

    input_1C = 1
    input_2C = 2
    input_3C = 3
    input_4C = 1
    input_5C = 2

    print(k_anagram(input_1A, input_1B, input_1C))
    print(k_anagram(input_2A, input_2B, input_2C))
    print(k_anagram(input_3A, input_3B, input_3C))
    print(k_anagram(input_4A, input_4B, input_4C))
    print(k_anagram(input_5A, input_5B, input_5C))

if __name__ == "__main__":
    main()

# Time: 25 minutes (20 for base idea + 5 for improvement)
# Was trying a different approach and couldn't get the result, so asked ChatGPT for a clue. This is where I learned what the Counter import was.