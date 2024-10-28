# Technique: fixed-size sliding window
# Time complexity: O(n)
# Space complexity: O(1)

def max_mean(arr, k):
    start = 0
    end = k-1
    max = 0

    # Input verification
    if not arr: return("Array cannot be empty.")
    if k <= 0: return("Subarray length must be greater than 0.")
    if k > len(arr): return("Subarray length (k) is too big.")

    # Select subarrays one by one
    while end < len(arr):
        curr = get_mean(arr, start, end) # Get subarray's mean
        if curr > max: max = curr
        start += 1
        end += 1
    
    return max

def get_mean(arr, start, end):
    sum = 0
    len = end - start + 1

    while start <= end:
        sum += arr[start]
        start += 1
    
    return (sum / len)

def main():
    input_1 = [4, 5, -3, 2, 6, 1] # Expected output: 4.5
    input_2 = [4, 5, -3, 2, 6, 1] # Expected output: 3.0
    input_3 = [1, 1, 1, 1, -1, -1, 2, -1, -1] # Expected output: 1.0
    input_4 = [1, 1, 1, 1, -1, -1, 2, -1, -1, 6] # Expected output: 1.0
    input_5 = [1, 2, 3] # Expected output: Subarray length (k) is too big.
    input_6 = [] # Expected output: Array cannot be empty.
    input_7 = [1, 2] # Expected output: Subarray length must be greater than 0.

    k_1 = 2
    k_2 = 3
    k_3 = 3
    k_4 = 5
    k_5 = 4
    k_6 = 1
    k_7 = -2

    print(max_mean(input_1, k_1))
    print(max_mean(input_2, k_2))
    print(max_mean(input_3, k_3))
    print(max_mean(input_4, k_4))
    print(max_mean(input_5, k_5))
    print(max_mean(input_6, k_6))
    print(max_mean(input_7, k_7))

if __name__ == "__main__":
    main()

# Time: 20 minutes (10 for base idea + 10 for improvement)
