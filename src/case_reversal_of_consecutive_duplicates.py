"""
Kata: Case Reversal of Consecutive Duplicates - The aim of this Kata is to
write a function which will reverse the case of all consecutive
duplicate letters in a string. That is, any letters that occur one after
 the other and are identical. If the duplicate letters are lowercase then
 they must be set to uppercase, and if they are uppercase then they need to be changed to lowercase.

#1 Best Practices Solution Blind4Basics

def reverse(strng): return re.sub(r'(\w)\1+', lambda m: m.group().swapcase(), strng)

"""


def reverse_case(word):
    boolean_list = [None] * len(word)
    previous_letter = word[0]
    for index in range(len(word)-1):
        if previous_letter != word[index+1]:
            previous_letter = word[index+1]
        else:
            if previous_letter.istitle():
                boolean_list[index] = previous_letter.lower()
                boolean_list[index + 1] = word[index + 1].lower()
            else:
                boolean_list[index] = previous_letter.upper()
                boolean_list[index + 1] = word[index + 1].upper()
                previous_letter = word[index + 1]

    for index in range(len(word)):
        if boolean_list[index] is None:
            boolean_list[index] = word[index]
    return ''.join(boolean_list)


