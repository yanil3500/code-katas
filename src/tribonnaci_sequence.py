"""
Kata: Tribonacci Sequence - it works basically like a Fibonacci,
but summing the last 3 (instead of 2) numbers of the sequence
to generate the next.

#1 Best Practices Solution by MiraliN, Cptnprice,
# FranzSchubert92, Chris_Rands, Mr.Child, gallione11

def find_short(s):
    return min(len(x) for x in s.split())
"""


def main():
    """
    Adds a main function
    """
    print('Whatevs')


def tribonnaci(seed_values, n_th_number):
    """
    calculates the n-th-fibonacci-numbers given the seed values
    """
    if n_th_number == 1:
        for index in range(len(seed_values)):
            if index < len(seed_values) and index < n_th_number:
                return [seed_values[index]]
    elif n_th_number == 0:
        return []
    numbers = []
    numbers.extend(seed_values)
    for index in range(len(numbers), n_th_number):
        numbers.append(numbers[index-1] + numbers[index - 2] + numbers[index - 3])
    print(numbers)
    return numbers


if __name__ == '__main__':
    main()
