import random

def parser(num):
    num = str(num)
    l = [str(i) for i in range(65, 91)]

    parsed_num = []
    for n in range(0, len(num), 2):
        if (num[n:n+2]) in l:
            parsed_num.append(num[n:n+2])    
    parsed_num = [int(n) for n in parsed_num]
    return parsed_num

# User word
given_word = str(input("Please enter a word: "))

given_word = given_word.upper()

# Each character of the word 
given_chr = list(given_word)
# ASCII of each character
given_split_chr = [ord(c) for c in given_chr]
# STR of each ASCII of each character
given_split_chr_str = [str(s) for s in given_split_chr]
# Join characters
given_split_chr_str = ''.join(given_split_chr_str)
# Int of str number
fusion_ascii_word = int(given_split_chr_str)

# Shuffle original word
shuffled_given_split_chr = given_split_chr

# Save every word combination
shuffles = []
for i in range(1000):
    shuffled_given_split_chr = sorted(shuffled_given_split_chr, key=lambda k: random.random())
    # List of shuffled words
    shuffles.append(shuffled_given_split_chr)

# Transform shuffled list numbers to str
shuffle_strings = []
for shuffle in shuffles:
    S = [str(s) for s in shuffle]
    shuffle_strings.append(S)

# Joining number
joined_shuffle_strings = [''.join(num) for num in shuffle_strings]

# Comparing each combination with the original word
diff = []
for j in range(0, len(joined_shuffle_strings)):
    d = abs(fusion_ascii_word - int(joined_shuffle_strings[j]))
    diff.append(d)

# Remove 0s
diff = [f for f in diff if f != 0]

# Closest shuffled combination to the original word
closest_shuffled_word = joined_shuffle_strings[diff.index(min(diff))]

# Fetch parsed number
parsed_closest_shuffled_word = parser(closest_shuffled_word)

restored_closest_word = [chr(c) for c in parsed_closest_shuffled_word]
print(restored_closest_word)

