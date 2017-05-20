"""
Kata: The Hidden Words - Write a function that will take a number
between 100 and 999999 and return a string with the word.
The input is always a number, contains only the numbers in the key. 
The output should be always a string with one word, all lowercase.

#1 Best Practices Solution by GiacomoSorbi

hidden=lambda n: "".join("oblietadnm"[int(d)] for d in str(n))

"""

def main():
    """
    main function
    """
    print('whatevs')


def hidden(num):
    """
    decoded a message from the number passed in 
    """
    num_to_letter = {
        0: 'o', 1: 'b', 2: 'l', 3: 'i', 4: 'e',
        5: 't', 6: 'a', 7: 'd', 8: 'n', 9: 'm'
      }
    words = ''
    for number in str(num):
        words += num_to_letter[int(number)]
    return words


if __name__ == '__main__':
    main()