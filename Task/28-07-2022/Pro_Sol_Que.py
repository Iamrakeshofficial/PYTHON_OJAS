'''1.You are given a sentence, and want to shift each letter by 2 in alphabet to create a secret code.
The sentence you want to encode is "the lazy dog jumped over the quick brown fox."
and the
output should be "vjg ncba fqi lworgf qxgt vjg swkem dtqyp hqz."

I/P-"The lazy dog jumped over the quick brown fox."

O/P-"vjg ncba fqi lworgf qxgt vjg swkem dtqyp hqz." '''

import string
Number2Letter = {}
Letter2Number ={}

for i,letter in enumerate(string.ascii_lowercase):
    Number2Letter[i] = letter
    Letter2Number[letter] = i

s2 = ' '
for letter in 'the lazy dog jumped over the quick brown fox':
    if letter in Letter2Number:
        current_letter_number = Letter2Number[letter] + 2
    
    if current_letter_number == 26:
            current_letter_number = 0
    elif current_letter_number == 27:
            current_letter_number = 1
    s2+= Number2Letter[current_letter_number]
else:
    s2+=letter

print(s2)
