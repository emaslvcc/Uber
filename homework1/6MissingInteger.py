# Technique: fixed-size sliding window
# Time complexity: O(log n)
# Space complexity: O(1)
# Doubt: How should we handle the case where the missing integer is the last one in the sequence?

def missing_integer(arr, n):
    start = 0
    end = len(arr) - 1

    # Binary search approach
    while start <= end:
        mid = (start + end) // 2

        if arr[mid] != mid + 1: # Finds missing element
            if mid == 0 or arr[mid - 1] == mid:
                return mid + 1
            end = mid - 1 # Search to the left
        else:
            start = mid + 1 # Search to the right

    return n + 1

def main():
    input_1 = [1, 2, 3, 4, 6, 7] # Expected output: 5
    input_2 = [1] # Expected output: 2
    input_3 = [1, 2, 3, 4, 5, 6, 7, 8, 10, 11, 12] # Expected output: 9
    input_4 = [2, 3, 4] # Expected output: 1
    input_5 = [1, 2, 3] # Expected output: 4

    n_1 = 7
    n_2 = 2
    n_3 = 12
    n_4 = 4
    n_5 = 4

    print(missing_integer(input_1, n_1))
    print(missing_integer(input_2, n_2))
    print(missing_integer(input_3, n_3))
    print(missing_integer(input_4, n_4))
    print(missing_integer(input_5, n_5))

main()

# Time: 30 minutes (2 for base idea + 28 for improvement)