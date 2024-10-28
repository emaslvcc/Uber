# Technique: sort the array, then solve
# Time complexity: O(n log n)
# Space complexity: O(n)

def merge(pairs):
    pairs.sort()
    result = [pairs[0]]
    
    for start, end in pairs[1:]:
        last_start, last_end = result[-1]

        if start <= last_end:
            result[-1] = (last_start, max(last_end, end))
        else:
            result.append((start, end))

    return result

def main():
    input_1 = [(2, 3), (4, 8), (1, 2), (5, 7), (9, 12)] # Expected output: [(4, 8), (1, 3), (9, 12)]
    input_2 = [(5, 8), (6, 10), (2, 4), (3, 6)] # Expected output: [(2, 10)]
    input_3 = [(10, 12), (5, 6), (7, 9), (1, 3)] # Expected output: [(10, 12), (5, 6), (7, 9), (1, 3)]

    print(merge(input_1))
    print(merge(input_2))
    print(merge(input_3))

if __name__ == "__main__":
    main()

# Time: 30 minutes (15 for base idea + 10 for optimization + 5 for improvement)