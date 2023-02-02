import numpy as np


def sum_of_cubes(n):
    """Return the sum (1^3 + 2^3 + 3^3 + ... + n^3)

    Precondition: n > 0, type(n) == int

    >>> sum_of_cubes(3)
    36
    >>> sum_of_cubes(1)
    1
    """
    res = 0

    if (n > 0 and type(n) == int):
        for i in range(n+1):
            res += i**3

        return res
    else:
        print("Invalid Input")
        return -1


def word_lengths(sentence):
    """Return a list containing the length of each word in
    sentence.

    >>> word_lengths("welcome to APS360!")
    [7, 2, 7]
    >>> word_lengths("machine learning is so cool")
    [7, 8, 2, 2, 4]
    """

    splitSent = sentence.split(" ")
    print(splitSent)

    resLst = []
    for i in splitSent:
        resLst.append(len(i))

    return resLst


def all_same_length(sentence):
    """Return True if every word in sentence has the same
    length, and False otherwise.

    >>> all_same_length("all same length")
    False
    >>> word_lengths("hello world")
    True
    """

    check = word_lengths(sentence)

    for i in check:
        for j in check:
            if i != j:
                return "They are not all the same Length"

    return "They are the all the same length"


print(all_same_length("i i i i"))


# 2a.) <NumpyArray>.size represents the number of elements in the matrix
#      and <NumpyArray>.shape represent the size of a matrix (n x n)

matrix = np.array([[1., 2., 3., 0.5],
                   [4., 5., 0., 0.],
                   [-1., -2., 1., 1.]])
vector = np.array([2., 0., 1., -2.])

matrix.size
matrix.shape
vector.size
vector.shape


matMult = []
for i in range(matrix[0]):
    for j in range(len(vector)):
        temp = 0
        temp += matrix[i]*vector[j]
    matMult.append(temp)

print(matMult)

