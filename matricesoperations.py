################################################################################
##### 1. Enter the number of rows and columns for matrix A and matrix B ########
##### 2. The matrices will be filled with random numbers from 1 to 10   ########
##### 3. The required methods will be performed                         ########
################################################################################

import random
import sys

num_rows_A = int(input("Number of rows of matrix A: "))
num_col_A = int(input("Number of columns of matrix A: "))

num_rows_B = int(input("Number of rows of matrix B: "))
num_col_B = int(input("Number of columns of matrix B: "))

scalar = int(input("Enter a number to perform the scalar multiplication: "))

matrix_a = []
matrix_b = []
result = []

######################################################################################
######################## FILLS MATRICES WITH RANDOM NUMBERS  #########################
######################################################################################

def initialize_matrices():
    for i in range(num_rows_A):
        matrix_a.append([])
        for j in range(num_col_A):
            matrix_a[i].append(random.randrange(10))

    for i in range(num_rows_B):
        matrix_b.append([])
        for j in range(num_col_B):
            matrix_b[i].append(random.randrange(10))

######################################################################################
###########################    POPULATES RESULT MATRIX  ##############################
######################################################################################

def populate_result(num_rows, num_col):
    #populates result matrix with 0
    for i in range(num_rows):
        result.append([])
        for j in range(num_col):
            result[i].append(0)
    
if((num_rows_A !=0 and num_rows_A > 1
       and num_col_A !=0 and num_col_A > 1)
   and (num_rows_B !=0 and num_rows_B > 1
       and num_col_B !=0 and num_col_B > 1)):
    initialize_matrices()
    populate_result(num_rows_A, num_col_A)
else:
    print("The number of rows and columns must be greater than 1")
    sys.exit(0)
    
######################################################################################
########################### RE-INITIALIZES RESULT MATRIX #############################
######################################################################################

def initializes_result():
    global result
    result = []

######################################################################################
##############################   PRINTS A MATRIX    ##################################
######################################################################################

def print_matrix(matrix):
    for r in matrix:
        print(*r, sep='\t')
    print()

######################################################################################
###########################  ADDITION of TWO MATRICES  ###############################
######################################################################################

def add_matrices(a,b):
    #iterate rows
    if(len(a) == len(b) and len(a[0]) == len(b[0])):
        for i in range(len(a)):
            #iterate columns
            for j in range(len(a[0])):
                result[i][j] = (matrix_a[i][j] + matrix_b[i][j])
        print_matrix(result)
    else:
       print("Can't add two matrix of different grades")
       
######################################################################################
###########################   TRANSPOSE of A MATRIX    ###############################
######################################################################################

def transpose(matrix):
    num_rows = len(matrix)
    num_col = len(matrix[0])
    
    initializes_result()
    populate_result(num_col, num_rows)
          
    for i in range(num_rows):
        for j in range(num_col):
           result[j][i] = matrix[i][j]
    return result

######################################################################################
###########################    MATRIX MULTIPLICATION   ###############################
######################################################################################

def multiply_matrices(a,b):
    if(len(a[0]) > len(b[0])):
        num_col = len(a[0])
    else:
        num_col = len(b[0])
    num_rows = len(a)

    initializes_result()
    populate_result(num_rows, num_col)

    #if the number of columns of A is equal to the number of rows in B
    if(len(a[0]) == len(b)):
        for i in range(len(a)):
            for j in range(len(b[0])):
                for k in range(len(b)):
                    result[i][j] += a[i][k] * b[k][j]
        print_matrix(result)
    else:
        print("Cant multiply two matrices if the number of columns in A is not equal to the number of rows in B")

######################################################################################
########################### MATRIX SCALAR MULTIPLICATION  ############################
######################################################################################

def scalar_multiplication(matrix, scalar):

    num_rows = len(matrix)
    num_col = len(matrix[0])
    
    initializes_result()
    populate_result(num_rows, num_col)

    for i in range(len(matrix)):
            #iterate columns
            for j in range(len(matrix[0])):
                result[i][j] = (matrix[i][j]*scalar)        
    return result

######################################################################################
################################ MATRIX DETERMINANT ##################################
######################################################################################

from copy import deepcopy

def minor(matrix,i):
    minor = deepcopy(matrix)
    del minor[0] #delete first row
    for b in range(len(matrix)-1): #delete column
        del minor[b][i]
    return minor
    

def det(matrix):
    if len(matrix) == 1: #Base case on which recursion ends
        return matrix[0][0]
    else:
        determinant = 0
        for x in list(range(len(matrix))): #iterates along first row finding cofactors
            determinant += matrix[0][x] * (-1)**(2+x)*det(minor(matrix,x)) #adds successive elements times their cofactors
        return determinant
             
######################################################################################
############################# MATRIX ADJUGATE  #######################################
######################################################################################

def adjugate(matrix):
    adj = 0
    if(len(matrix) == len(matrix[0])):
        if(len(matrix) == 2):
            adj = adjugate_two(matrix)
        elif(len(matrix) == 3):
            adj = adjugate_three(matrix)
        else:
            print("A method to calculate the adjugate of a matrix greater than 3x3 hasnt been implemented yet")
    else:
        print("The adjugate of a non square matrix cannot be calculated")
    return adj
        
def adjugate_two(matrix):
    adj_two = [[matrix[1][1],-matrix[1][0]],
            [-matrix[0][1],matrix[0][0]]]
    result = transpose(adj_two)
    return result

def adjugate_three(matrix):
    #calculate the cofactors
    first = det([[matrix[1][1],matrix[1][2]],[matrix[2][1],matrix[2][2]]])
    second = det([[matrix[1][0],matrix[1][2]],[matrix[2][0],matrix[2][2]]])
    third = det([[matrix[1][0],matrix[1][1]],[matrix[2][0],matrix[2][1]]])
    fourth = det([[matrix[0][1],matrix[0][2]],[matrix[2][1],matrix[2][2]]])
    fifth = det([[matrix[0][0],matrix[0][2]],[matrix[2][0],matrix[2][2]]])
    sixth = det([[matrix[0][0],matrix[0][1]],[matrix[2][0],matrix[2][1]]])
    seventh = det([[matrix[0][1],matrix[0][2]],[matrix[1][1],matrix[1][2]]])
    eight = det([[matrix[0][0],matrix[0][2]],[matrix[1][0],matrix[1][2]]])
    ninth = det([[matrix[0][0],matrix[0][1]],[matrix[1][0],matrix[1][1]]])

    cofactors_matrix = [[first,-fourth,seventh],[-second,fifth,-eight],[third,-sixth,ninth]]

    return cofactors_matrix
 
######################################################################################
#############################    INVERSE MATRIX    ###################################
######################################################################################

def inverse(matrix):    
    if(len(matrix) == len(matrix[0])):
        if(len(matrix) < 4):
            determinant = det(matrix)
            adj = adjugate(matrix)
            #transp = transpose(adj)
            if(determinant != 0 and adj != 0):
                result = divide_by_determinant(adj,determinant)
                print_matrix(result)
            else:
                print("Cannot calculate the inverse of a matrix of determinant 0")
        else:
            print("A method to calculate the inverse of a matrix greater than 3x3 hasnt been implemented yet")

def divide_by_determinant(matrix, det):
    for i in range(len(matrix)):
        #iterate columns
        for j in range(len(matrix[0])):
            result[i][j] = round(matrix[i][j]/det, 2)        
    return result

######################################################################################
##############################   PRINTS ROWS OF MATRIX   #############################
######################################################################################

def print_matrix_rows(matrix, *argv):
    for arg in argv:
        print("This is row " + str(arg) + ": ")
        print(*matrix[arg], sep='\t')
    print()

######################################################################################
##############################   PRINTS COLS OF MATRIX   #############################
######################################################################################

def print_matrix_cols(matrix, *argv):
    for arg in argv:
        print("This is column " + str(arg) + ": ")
        for i in range(len(matrix)):
            print(matrix[i][arg])
    print()
 
######################################################################################
##############################   PRINTS COLS OF MATRIX   #############################
######################################################################################

def print_matrix_from_cols(matrix,col):
    initializes_result()
    result = deepcopy(matrix)

    for i in range(col):
        all(map(lambda x: x.pop(0), result))
    print_matrix(result)

######################################################################################
##############################    METHOD CALLS     #############################
################################################################################
    
print("MATRIX A")
print_matrix(matrix_a)

print("MATRIX B")
print_matrix(matrix_b)

print("MATRIX A + B")
add_matrices(matrix_a,matrix_b)

print("TRANSPOSE MATRIX A")
print_matrix(transpose(matrix_a))

print("TRANSPOSE MATRIX B")
print_matrix(transpose(matrix_b))

print("MULTIPLICATION OF MATRIX A * B")
multiply_matrices(matrix_a, matrix_b)

print("SCALAR MULTIPLICATION OF MATRIX n * A")
print_matrix(scalar_multiplication(matrix_a, scalar))

print()
print("DETERMINANT A: " + str(det(matrix_a)))
print("DETERMINANT B: " + str(det(matrix_b)))
print()

print("ADJUGATE MATRIX A")
if(adjugate(matrix_a) != 0): 
    print_matrix(adjugate(matrix_a))
print("ADJUGATE MATRIX B")
if(adjugate(matrix_b) != 0): 
    print_matrix(adjugate(matrix_b))

print("INVERSE MATRIX A")
inverse(matrix_a)
print("INVERSE MATRIX B")
inverse(matrix_b)

print("SELECTED ROWS OF MATRIX A")
print_matrix_rows(matrix_a, 0,2)
print("SELECTED COLUMNS OF MATRIX A")
print_matrix_cols(matrix_a, 0,1)

print("MATRIX A")
print_matrix(matrix_a)

print("MATRIX A FROM COLUMN 2")
print_matrix_from_cols(matrix_a, 2)
