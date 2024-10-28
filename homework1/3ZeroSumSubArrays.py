# Technique: variable-size (shrinking/growing) sliding window
# Time complexity: O(n^2)
# Space complexity: O(1)

def zero_sum(arr):
    total = 0

    # Input validation
    if not arr: return("Array cannot be empty.")

    for start in range(len(arr)): # Iterate subarrays' start point
        sum = 0
        for end in range(start, len(arr)): # Iterate subarrays' end point
            sum += arr[end]
            if sum == 0: total += 1
    
    return total

def main():
    input_1 = [4, 5, 2, -1, -3, -3, 4, 6, -7] # Expected output: 2
    input_2 = [1, 8, 7, 3, 11, 9] # Expected output: 0
    input_3 = [8, -5, 0, -2, 3, -4] # Expected output: 2
    input_4 = [] # Expected output: Array cannot be empty.
    input_5 = [0, 0, 0, 0] # Expected output: 10

    print(zero_sum(input_1))
    print(zero_sum(input_2))
    print(zero_sum(input_3))
    print(zero_sum(input_4))
    print(zero_sum(input_5))

if __name__ == "__main__":
    main()

# Time: 15 minutes (10 for base idea + 5 for improvement)
