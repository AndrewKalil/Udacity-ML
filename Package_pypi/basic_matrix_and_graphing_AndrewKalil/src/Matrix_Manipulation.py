import numpy as np
from .Basic_Operations import Basic_Operations


class Matrix_Manipulation(Basic_Operations):

    def __init__(self, matrix1=None, matrix2=None):
        super().__init__(matrix1, matrix2)

    def transpose(self):
        """Finds the transpose of a matrix

        Returns:
            np.Array: a new array which is the transpose of a matrix
        """
        try:
            inverse = self.matrix1.T
        except Exception as e:
            return "Error: {}".format(e)

        return inverse

    def determinant(self):
        """Finds the determinant of a matrix

        Returns:
            np.Array: a new array which is the determinant of the array
        """
        try:
            determinant = np.linalg.det(self.matrix1)
        except Exception as e:
            return "Error: {}".format(e)

        return determinant

    def invertion(self):
        """Finds the determinant of a matrix

        Returns:
            np.Array: a new array which is the determinant of the array
        """

        try:
            if (self.matrix_shape()[0] == self.matrix_shape()[1]) and self.determinant() != 0:
                invert = np.linalg.inv(self.matrix1)
                return invert
        except Exception as e:
            return "Error: {}".format(e)


    def matrix_shape(self):
        """Output the shape of array

        Returns:
            np.Array: a new array which is the shape of the array
        """
        try:
            shape = self.matrix1.shape
        except Exception as e:
            return "Error: {}".format(e)

        return shape

    def scalar(self, constant):
        """Output a new array scaled to the constant

        Returns:
            np.Array: a new array which is the result of scaling the array
        """
        try:
            new_array = self.matrix1 * constant
        except Exception as e:
            return "Error: {}".format(e)

        return new_array

    def show_matrix(self):
        """Shows a matrix

        Returns:
            np.ndarray: The inputter matrix
        """
        return self.matrix1

arr1 = Matrix_Manipulation([[1, 2, 3, 4], [4, 5, 6, 10], [7, 8, 9, 10]])
arr2 = Matrix_Manipulation([[1, 2, 3], [4, 5, 6]])

mat1 = [[1, 2],[3, 4]]
mat2 = [[5, 6],[7, 8]]
operations = Matrix_Manipulation(mat1, mat2)

# print("arr1 transpose: \n", arr1.transpose())
# print("arr1 determinant: \n", arr1.determinant())
# print("arr1 invertion: \n", arr1.invertion())
# print("arr1 scalar: \n", arr1.scalar(5))
# print("arr1 matrix shape: \n", arr1.matrix_shape())
# print("arr1 matrix: \n", arr1.show_matrix())
# print()
# print("arr2 transpose: \n", arr2.transpose())
# print("arr2 determinant: \n", arr2.determinant())
# print("arr2 invertion: \n", arr2.invertion())
# print("arr2 scalar: \n", arr2.scalar(3))
# print("arr2 matrix shape: \n", arr2.matrix_shape())
# print("arr2 matrix: \n", arr2.show_matrix())
# print()
print("addition: \n", operations.addition())