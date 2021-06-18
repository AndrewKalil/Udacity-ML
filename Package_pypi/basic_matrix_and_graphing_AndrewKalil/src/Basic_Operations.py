import numpy as np
from numpy.matrixlib.defmatrix import matrix


class Basic_Operations:
    """Basic Matrix Operations on two np.Arrays
    """

    def __init__(self, matrix1=None, matrix2=None):
        """Instantiation method
        Args:
            matrix1: first matrix to be added
            matrix2: second matrix to be added
        """
        self.matrix1 = self.verify_numpy_type(matrix1)
        self.matrix2 = self.verify_numpy_type(matrix2)


    def verify_numpy_type(self, matrix):
        """Ensures types are kept same throughout the class

        Args:
            matrix: matrix to be converted to np.ndarray if not
            already converted

        Returns:
            np.ndarray: returns an np.ndarray
        """
        if type(matrix) != np.ndarray and matrix != None:
            return np.asfarray(matrix)
        elif type(matrix) == np.ndarray and matrix != None:
            return matrix

    def addition(self):
        """Performs addition opperation on two matrices

        Returns:
            np.Array: a new array which is the result of adding the
            two arrays
        """
        try:
            addition = self.matrix1 + self.matrix2
        except Exception as e:
            return "Error: {}".format(e)

        return addition

    def substraction(self):
        """Performs substraction opperation on two matrices

        Returns:
            np.Array: a new array which is the result of substracting
            the two arrays
        """
        try:
            substraction = self.matrix1 - self.matrix2
        except Exception as e:
            return "Error: {}".format(e)

        return substraction

    def multiplication(self):
        """Performs multiplication opperation on two matrices

        Returns:
            np.Array: a new array which is the result of multiplying
            the two arrays
        """
        try:
            multiplication = self.matrix1 * self.matrix2
        except Exception as e:
            return "Error: {}".format(e)

        return multiplication

    def division(self):
        """Performs divison opperation on two matrices

        Returns:
            np.Array: a new array which is the result of dividing the
            two arrays
        """
        try:
            division = self.matrix1 / self.matrix2
        except Exception as e:
            return "Error: {}".format(e)

        return division

    def dot(self):
        """Performs dot multiplication opperation on two matrices

        Returns:
            np.Array: a new array which is the result of the dot product of
            the two arrays
        """
        try:
            dot = np.dot(self.matrix1, self.matrix2)
        except Exception as e:
            return "Error: {}".format(e)

        return dot


# arr1 = [[1.4, 2.5, 3.7]]
# arr2 = [[7, 8.4, 9]]
# arr3 = [[7, 8], [9, 10], [11, 12]]

# operations = Basic_Operations(arr1)
# print(operations.addition())
# print(operations.substraction())
# print(operations.multiplication())
# print(operations.division())
# print(operations.dot())
