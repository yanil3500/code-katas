"""
Kata: Counting Duplicates - Write a function that will return the count of
distinct case-insensitive alphabetic characters and numeric digits that occur
more than once in the input string. The input string can be assumed to contain
only alphanumeric characters, including digits, uppercase and lowercase alphabets.

#1 Best Practices Solution by tpatja, nkrause323, alpen0

def duplicate_count(s):
  return len([c for c in set(s.lower()) if s.lower().count(c)>1])
"""


def duplicate_count(text):
    """
    return the count of distinct-case insensitive alphanumeric 
    character that occur more than once in a string.
    """
    duplicates = set()
    non_duplicates = []

    for letter in text.replace(' ', '').lower():
        if letter not in non_duplicates:
            non_duplicates.append(letter)
        else:
            duplicates.add(letter)
    return len(duplicates)


