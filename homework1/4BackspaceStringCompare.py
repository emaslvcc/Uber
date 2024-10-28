# Technique: fixed-size sliding window
# Time complexity: O(n + m)
# Space complexity: O(n + m)

def compare(str_1, str_2):

    if (str_1 == "" and str_2 == ""): return("Cannot have both strings be empty.")

    str_1_normal = normalize(str_1)
    str_2_normal = normalize(str_2)

    if str_1_normal == str_2_normal: return True
    return False

def normalize(str):
    str_list = list(str)
    i = 0

    while i < len(str_list):
        if str_list[i] == '#':
            if i > 0: # Ensure there is a character to remove
                str_list.pop(i - 1)
                i -= 1 # Move back one step to check the new current character
            str_list.pop(i) # Remove the '#' itself
        else:
            i += 1  # Move to the next character only if no pop occurred

    return ''.join(str_list)

def main():
    input_1A = "abcde" # Expected output: True
    input_2A = "Uber Career Prep" # Expected output: True
    input_3A = "abcdef###xyz" # Expected output: True
    input_4A = "abcdef###xyz" # Expected output: False
    input_5A = "" # Expected output: Cannot have both strings be empty.
    input_6A = "" # Expected output: False
    input_7A = "###" # Expected output: True
    
    input_1B = "abcde"
    input_2B = "u#Uber Careee#r Prep"
    input_3B = "abcw#xyz"
    input_4B = "abcdefxyz###"
    input_5B = ""
    input_6B = "abc"
    input_7B = ""

    print(compare(input_1A, input_1B))
    print(compare(input_2A, input_2B))
    print(compare(input_3A, input_3B))
    print(compare(input_4A, input_4B))
    print(compare(input_5A, input_5B))
    print(compare(input_6A, input_6B))
    print(compare(input_7A, input_7B))

if __name__ == "__main__":
    main()

# Time: 25 minutes (15 for base idea + 10 for improvement)
