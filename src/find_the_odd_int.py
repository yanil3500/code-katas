"""
Kata: Find The Odd Int - Given an array, find the int that appears an odd number of times.
There will always be only one integer that appears an odd number of times.

#1 Best Practices Solution by cerealdinner, ynnake, sfr, netpsychosis, VadimPopov, anaskhan96 

def find_it(seq):
    for i in seq:
        if seq.count(i)%2!=0:
            return i

"""


def main():
    """
    main function
    """
    print('whatevs')


def find_it(seq):
    """
    return the odd int in the array
    """
    return max(filter(lambda x: seq.count(x) % 2 != 0, seq))


if __name__ == '__main__':
    main()
