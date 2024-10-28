# Technique: forward/backward two-pointer
# Time complexity: O(n)
# Space complexity: O(n)

def reverse_vowels(str):
    str_list = list(str) # Allows for swapping
    vowels = "aeiouAEIOU"
    start = 0
    end = len(str) - 1

    # Input verification
    if (str == ""): return("Please input a non-empty string.")

    while start < end:
        # Forward pointer going from start to end
        if (str_list[start] not in vowels):
            start += 1

        # Backward pointer going from end to start
        if (str_list[end] not in vowels): 
            end -= 1

        # Swap values when both pointers encounter a vowel
        if (str_list[start] in vowels and str_list[end] in vowels):
            temp = str_list[start]
            str_list[start] = str_list[end]
            str_list[end] = temp
            start += 1
            end -= 1

    return ''.join(str_list)

def main():
    input_1 = "Uber Career Prep"
    input_2 = "xyz"
    input_3 = "flamingo"
    input_4 = ""
    input_5 = "aeiou"
    input_6 = "banana"

    print(reverse_vowels(input_1)) # Expected output: "eber Ceraer PrUp"
    print(reverse_vowels(input_2)) # Expected output: "xyz"
    print(reverse_vowels(input_3)) # Expected output: "flominga"
    print(reverse_vowels(input_4)) # Expected output: "Please input a non-empty string."
    print(reverse_vowels(input_5)) # Expected output: "uoiea"
    print(reverse_vowels(input_6)) # Expected output: "banana"

if __name__ == "__main__":
    main()

# Time: 25 minutes (10 for base idea + 15 for improvement)