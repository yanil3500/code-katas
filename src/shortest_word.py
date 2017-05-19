"""
Kata: Shortest Word - given a string of words, return the length of the shortest word(s).

#1 Best Practices Solution by MiraliN, Cptnprice, FranzSchubert92, Chris_Rands, Mr.Child, gallione11 

def find_short(s):
    return min(len(x) for x in s.split())
"""


def main():
    print('Whatevs')


def find_short(words):
    """
    given a string of words, returns the length of the shortest word
    """
    if are_valid_words(words):
        if len(words) > 1:
            return min(map(lambda word: len(word), words.split()))
        else:
            return len(words)


def are_valid_words(words):
    """
    checks for valid input
    """
    return type(words) == str


if __name__ == '__main__':
    main()
