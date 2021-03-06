## Basic Linear Algebra
This package performs basic linear algebra operations and matrix manipulations

### Intallation
In your command line or command prompnt, you can install the package using the following command:
```
pip install basicLinalgAKO
```

### Usage
Once the package is installed locally, open up a python script file (name it whatever you want) and test it out with the following:

##### 1) For operations between two matrices
```
import basicLinalgAKO as BLA

matrix1 = [[1, 3, 5],[2, 4, 6]]
matrix2 = [[7, 9, 11],[8, 10, 12]]

operations = BLA(matrix1, matrix2)
print("addition: \n", operations.addition(), "\n")
print("substraction: \n", operations.substraction(), "\n")
print("multiplication: \n", operations.multiplication(), "\n")
print("division: \n", operations.division(), "\n")
print("dot product: \n", operations.dot(), "\n")
```
##### Output:

##### 2) For matrix manipulations
```
import basicLinalgAKO as BLA

matrix1 = [[1, 3, 5],[2, 4, 6]]

manipulations = BLA(matrix1)
print("array transpose: \n", manipulations.transpose(), "\n")
print("array determinant: \n", manipulations.determinant(), "\n")
print("array invertion: \n", manipulations.invertion(), "\n")
print("array scalar: \n", manipulations.scalar(5), "\n")
print("array matrix shape: \n", manipulations.matrix_shape(), "\n")
print("array matrix: \n", manipulations.show_matrix(), "\n")
```
##### Output:


###### Author: Andrew Kalil