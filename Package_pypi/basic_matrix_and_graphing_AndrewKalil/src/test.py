import unittest
import numpy as np

from Matrix_Manipulation import Matrix_Manipulation

class TestGaussianClass(unittest.TestCase):
    def setUp(self):
        matrix1 = [[1, 2],[3, 4]]
        matrix2 = [[5, 6],[7, 8]]
        matrix3 = [[1, 2, 3],[4, 5, 6]]
        matrix4 = [[7, 8, 9],[10, 11, 12]]
        matrix5 = [[1, 2, 3],[4, 5, 6], [7, 8, 9]]

        self.operations1 = Matrix_Manipulation(matrix1, matrix2)
        self.operations2 = Matrix_Manipulation(matrix3, matrix4)
        self.manipulation1 = Matrix_Manipulation(matrix4)
        self.manipulation2 = Matrix_Manipulation(matrix5)

    def test_type_basic_operations(self):
        self.assertEqual(type(self.operations1.addition()), np.ndarray, 'sum incorrect type')
        self.assertEqual(type(self.operations1.substraction()), np.ndarray, 'diff incorrect type')
        self.assertEqual(type(self.operations1.multiplication()), np.ndarray, 'product incorrect type')
        self.assertEqual(type(self.operations1.division()), np.ndarray, 'quotient incorrect type')

        self.assertEqual(type(self.operations2.addition()), np.ndarray, 'sum incorrect type')
        self.assertEqual(type(self.operations2.substraction()), np.ndarray, 'diff incorrect type')
        self.assertEqual(type(self.operations2.multiplication()), np.ndarray, 'product incorrect type')
        self.assertEqual(type(self.operations2.division()), np.ndarray, 'quotient incorrect type')

    def test_type_basic_manipulations(self):
        self.assertEqual(type(self.manipulation1.transpose()), np.ndarray, 'transpose incorrect type')
        self.assertEqual(type(self.manipulation1.matrix_shape()), tuple, 'matrix_shape incorrect type')
        self.assertEqual(type(self.manipulation1.scalar(4)), np.ndarray, 'scalar incorrect type')
        self.assertEqual(type(self.manipulation1.show_matrix()), np.ndarray, 'show_matrix incorrect type')

        self.assertEqual(type(self.manipulation2.transpose()), np.ndarray, 'transpose incorrect type')
        self.assertEqual(type(self.manipulation2.matrix_shape()), tuple, 'matrix_shape incorrect type')
        self.assertEqual(type(self.manipulation2.scalar(4)), np.ndarray, 'scalar incorrect type')
        self.assertEqual(type(self.manipulation2.show_matrix()), np.ndarray, 'show_matrix incorrect type')

if __name__ == '__main__':
    unittest.main()