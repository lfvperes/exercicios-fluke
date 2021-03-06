"""
Processo seletivo Fluke - Back-end Developer
Exercício 1
Luís Peres
"""
# this module will be used to generate more complex examples
import random

def create_matrix(size):
    """
    - this function creates a matrix shaped 1x99 (max).
    its 99 numbers vary from 1 to 99, being 48 random pairs and a
    random unique number. 
    - if the specified size is smaller than 100, the numbers still vary
    between 1 and 99, but the length of the matrix is given by (n = size-1),
    with 0.5*(size-1) pairs and one random unique number.
    """

    # this guarantees the required restrictions are met
    if (size % 2) != 0:
        # size must be even for n to be odd (n = size-1)
        size += 1
    if size > 100:
        # n must always be less than or equal to 99
        size = 100

    # the list is initialized empty
    y = []
    for element in range(int(size / 2)):
        # when size=100, this adds 50 random numbers between 1 and 99 to the list
        y.append(random.randint(1, 99))

    # this duplicates every number, now being a 100-lengthed list (when size=100)
    y = y * 2
    # the list is then scrambled once more
    random.shuffle(y)
    # one number from a random pair is removed
    y.pop(random.randint(0, size - 1))

    return y

def find_unique(matrix):
    """
    this function stores all possible candidates for the unique number
    in a list. any candidate will be removed when the loop iterates
    through the same number. only one loop is required.
    """

    # the storing list is initialized empty
    candidate = []

    # the matrix received as an argument is iterated
    for element in matrix:
        # every element is analyzed
        if element in candidate:
            # repetition yelds removal
            candidate.remove(element)
        else:
            # uniqueness yelds temporary storing
            candidate.append(element)
    
    # after the loop, the list contains only the unique number
    return candidate

# simple example matrix entered by hand
x = [1, 1, 2, 3, 4, 5, 3, 5, 2]
# small random matrix generated by the function
y = create_matrix(6)
# longer random matrix (1x100) generated by the function
z = create_matrix(50)

# showing the lists
print(x, "-> o único número sem repetição é", find_unique(x))
print(y, "-> o único número sem repetição é", find_unique(y))
print(z, "-> o único número sem repetição é", find_unique(z))
