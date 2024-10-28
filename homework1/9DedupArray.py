# Technique: forward two-pointer
# Time complexity: O(n) but O(n^2) in the worst-case scenario
# Space complexity: O(1)

def dedup(arr):
    i = 0
    while i < len(arr) - 1:
        if arr[i] == arr[i + 1]: arr.pop(i + 1)
        else: i += 1

    return arr

def main():
    input_1 = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4] # Expected output: [1, 2, 3, 4]
    input_2 = [0, 0, 1, 4, 5, 5, 5, 8, 9, 9, 10, 11, 15, 15] # Expected output: [0, 1, 4, 5, 8, 9, 10, 11, 15]
    input_3 = [1, 3, 4, 8, 10, 12] # Expected output: [1, 3, 4, 8, 10, 12]
    input_4 = [0, 0, 0, 0, 0, 0] # Expected output: [0]

    print(dedup(input_1))
    print(dedup(input_2))
    print(dedup(input_3))
    print(dedup(input_4))

if __name__ == "__main__":
    main()

# Time: 10 minutes (5 for base idea + 5 for improvement)