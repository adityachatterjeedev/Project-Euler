import numpy as np

def problem11():
    """
    Project Euler Problem 11
    https://projecteuler.net/problem=11

    The problem:


    In the 20×20 grid below, four numbers along a diagonal line have been marked in red.

    08 02 22 97 38 15 00 40 00 75 04 05 07 78 52 12 50 77 91 08
    49 49 99 40 17 81 18 57 60 87 17 40 98 43 69 48 04 56 62 00
    81 49 31 73 55 79 14 29 93 71 40 67 53 88 30 03 49 13 36 65
    52 70 95 23 04 60 11 42 69 24 68 56 01 32 56 71 37 02 36 91
    22 31 16 71 51 67 63 89 41 92 36 54 22 40 40 28 66 33 13 80
    24 47 32 60 99 03 45 02 44 75 33 53 78 36 84 20 35 17 12 50
    32 98 81 28 64 23 67 10\033[91m 26\033[00m 38 40 67 59 54 70 66 18 38 64 70
    67 26 20 68 02 62 12 20 95\033[91m 63\033[00m 94 39 63 08 40 91 66 49 94 21
    24 55 58 05 66 73 99 26 97 17\033[91m 78\033[00m 78 96 83 14 88 34 89 63 72
    21 36 23 09 75 00 76 44 20 45 35\033[91m 14\033[00m 00 61 33 97 34 31 33 95
    78 17 53 28 22 75 31 67 15 94 03 80 04 62 16 14 09 53 56 92
    16 39 05 42 96 35 31 47 55 58 88 24 00 17 54 24 36 29 85 57
    86 56 00 48 35 71 89 07 05 44 44 37 44 60 21 58 51 54 17 58
    19 80 81 68 05 94 47 69 28 73 92 13 86 52 17 77 04 89 55 40
    04 52 08 83 97 35 99 16 07 97 57 32 16 26 26 79 33 27 98 66
    88 36 68 87 57 62 20 72 03 46 33 67 46 55 12 32 63 93 53 69
    04 42 16 73 38 25 39 11 24 94 72 18 08 46 29 32 40 62 76 36
    20 69 36 41 72 30 23 88 34 62 99 69 82 67 59 85 74 04 36 16
    20 73 35 29 78 31 90 01 74 31 49 71 48 86 81 16 23 57 05 54
    01 70 54 71 83 51 54 69 16 92 33 48 61 43 52 01 89 19 67 48

    The product of these numbers is 26 × 63 × 78 × 14 = 1788696.

    What is the greatest product of four adjacent numbers in the same direction (up, down, left, right, or diagonally) in the 20×20 grid?
    """
    #the products from left to right will be the same as the products from right to left.
    #similarly the products from up to down will be the same as the products from down to up
    #so matrix traversal is only done once in the vertical direction and once in the horizontal direction 
    #instead of doing so twice.
    #it's the same for products in diagonal directions
    
    row_1 = np.array([8, 2, 22, 97, 38, 15, 00, 40, 00, 75, 4, 5, 7, 78, 52, 12, 50, 77, 91, 8])
    row_2 = np.array([49, 49, 99, 40, 17, 81, 18, 57, 60, 87, 17, 40, 98, 43, 69, 48, 4, 56, 62, 00])
    row_3 = np.array([81, 49, 31, 73, 55, 79, 14, 29, 93, 71, 40, 67, 53, 88, 30, 3, 49, 13, 36, 65])
    row_4 = np.array([52, 70, 95, 23, 4, 60, 11, 42, 69, 24, 68, 56, 1, 32, 56, 71, 37, 2, 36, 91])
    row_5 = np.array([22, 31, 16, 71, 51, 67, 63, 89, 41, 92, 36, 54, 22, 40, 40, 28, 66, 33, 13, 80])
    row_6 = np.array([24, 47, 32, 60, 99, 3, 45, 2, 44, 75, 33, 53, 78, 36, 84, 20, 35, 17, 12, 50])
    row_7 = np.array([32, 98, 81, 28, 64, 23, 67, 10, 26, 38, 40, 67, 59, 54, 70, 66, 18, 38, 64, 70])
    row_8 = np.array([67, 26, 20, 68, 2, 62, 12, 20, 95, 63, 94, 39, 63, 8, 40, 91, 66, 49, 94, 21])
    row_9 = np.array([24, 55, 58, 5, 66, 73, 99, 26, 97, 17, 78, 78, 96, 83, 14, 88, 34, 89, 63, 72])
    row_10 = np.array([21, 36, 23, 9, 75, 00, 76, 44, 20, 45, 35, 14, 00, 61, 33, 97, 34, 31, 33, 95])
    row_11 = np.array([78, 17, 53, 28, 22, 75, 31, 67, 15, 94, 3, 80, 4, 62, 16, 14, 9, 53, 56, 92])
    row_12 = np.array([16, 39, 5, 42, 96, 35, 31, 47, 55, 58, 88, 24, 00, 17, 54, 24, 36, 29, 85, 57])
    row_13 = np.array([86, 56, 00, 48, 35, 71, 89, 7, 5, 44, 44, 37, 44, 60, 21, 58, 51, 54, 17, 58])
    row_14 = np.array([19, 80, 81, 68, 5, 94, 47, 69, 28, 73, 92, 13, 86, 52, 17, 77, 4, 89, 55, 40])
    row_15 = np.array([4, 52, 8, 83, 97, 35, 99, 16, 7, 97, 57, 32, 16, 26, 26, 79, 33, 27, 98, 66])
    row_16 = np.array([88, 36, 68, 87, 57, 62, 20, 72, 3, 46, 33, 67, 46, 55, 12, 32, 63, 93, 53, 69])
    row_17 = np.array([4, 42, 16, 73, 38, 25, 39, 11, 24, 94, 72, 18, 8, 46, 29, 32, 40, 62, 76, 36])
    row_18 = np.array([20, 69, 36, 41, 72, 30, 23, 88, 34, 62, 99, 69, 82, 67, 59, 85, 74, 4, 36, 16])
    row_19 = np.array([20, 73, 35, 29, 78, 31, 90, 1, 74, 31, 49, 71, 48, 86, 81, 16, 23, 57, 5, 54])
    row_20 = np.array([1, 70, 54, 71, 83, 51, 54, 69, 16, 92, 33, 48, 61, 43, 52, 1, 89, 19, 67, 48])

    matrix = np.array([row_1, row_2, row_3, row_4, row_5, row_6, row_7, row_8, row_9, row_10, row_11, row_12, row_13, row_14, row_15, row_16, row_17, row_18, row_19, row_20])

    products_list = [] #main list of products
    keys_list = [] #main list of keys
    
    #row products
    for i in range(20):
        row  = matrix[i]
        temp_prod_list = []
        temp_key_list = []

        for j in range(17):
            a = row[j]
            b = row[j+1]
            c = row[j+2]
            d = row[j+3]
            prod = a*b*c*d
            key = np.array([a, b, c, d])
            temp_prod_list.append(prod)
            temp_key_list.append(key)
        
        max_prod = temp_prod_list[0]
        max_key = temp_key_list[0]
        for i in range(len(temp_prod_list)):
            if temp_prod_list[i] > max_prod:
                max_prod = temp_prod_list[i]
                max_key = temp_key_list[i]
        #we now have the max product in each row.
        products_list.append(max_prod)
        keys_list.append(max_key)

    #column products

    for j in range(20):     #iterating over columns
        temp_prod_list = []
        temp_key_list = []

        for i in range(17): #iterating for each row
            a = matrix[i][j]
            b = matrix[i+1][j]
            c = matrix[i+2][j]
            d = matrix[i+3][j]
            key = np.array([a,b,c,d])
            product = a*b*c*d
            temp_key_list.append(key)
            temp_prod_list.append(product)

        max_prod = temp_prod_list[0]
        max_key = temp_key_list[0]
        for i in range(len(temp_prod_list)):
            if temp_prod_list[i] > max_prod:
                max_prod = temp_prod_list[i]
                max_key = temp_key_list[i]
        #we now have the max product in each column.
        products_list.append(max_prod)
        keys_list.append(max_key)

    #we're now done with rows and columns
    #now to start with diagonals. 
    #first we deal with diagonals going in the direction parallel to bottom-left to top-right

    temp_prod_list = []
    temp_key_list = []

    #start code to traverse matrix

    for i in range(3, 20):
        rownum = i
        colnum = 0

        while (rownum - 3 >= 0):
            a = matrix[rownum][colnum]
            b = matrix[rownum - 1][colnum + 1]
            c = matrix[rownum - 2][colnum + 2]
            d = matrix[rownum - 3][colnum + 3]
            key = np.array([a,b,c,d])
            product = a*b*c*d
            temp_key_list.append(key)
            temp_prod_list.append(product)
            rownum -= 1
            colnum += 1   

    for i in range(1,17):
        rownum = 19
        colnum = i

        while (20 - colnum > 3):
            a = matrix[rownum][colnum]
            b = matrix[rownum - 1][colnum + 1]
            c = matrix[rownum - 2][colnum + 2]
            d = matrix[rownum - 3][colnum + 3]
            key = np.array([a,b,c,d])
            product = a*b*c*d
            temp_key_list.append(key)
            temp_prod_list.append(product)
            rownum -= 1
            colnum += 1 
    
    #end code to traverse matrix

    max_prod = temp_prod_list[0]
    max_key = temp_key_list[0]
    for i in range(len(temp_prod_list)):
        if temp_prod_list[i] > max_prod:
            max_prod = temp_prod_list[i]
            max_key = temp_key_list[i]

    products_list.append(max_prod)
    keys_list.append(max_key)

    #next we deal with diagonals going in the direction parallel to bottom-right to top-left

    temp_prod_list = []
    temp_key_list = []

    #start code to traverse matrix

    for i in range(3,20):
        rownum = i
        colnum = 19

        while (rownum - 3 >= 0):
            a = matrix[rownum][colnum]
            b = matrix[rownum - 1][colnum - 1]
            c = matrix[rownum - 2][colnum - 2]
            d = matrix[rownum - 3][colnum - 3]
            key = np.array([a,b,c,d])
            product = a*b*c*d
            temp_key_list.append(key)
            temp_prod_list.append(product)
            rownum -= 1
            colnum -= 1

    for i in range(18, 2, -1):
        rownum = 19
        colnum = i

        while (colnum - 3 >= 0):
            a = matrix[rownum][colnum]
            b = matrix[rownum - 1][colnum - 1]
            c = matrix[rownum - 2][colnum - 2]
            d = matrix[rownum - 3][colnum - 3]
            key = np.array([a,b,c,d])
            product = a*b*c*d
            temp_key_list.append(key)
            temp_prod_list.append(product)
            rownum -= 1
            colnum -= 1            

    max_prod = temp_prod_list[0]
    max_key = temp_key_list[0]
    for i in range(len(temp_prod_list)):
        if temp_prod_list[i] > max_prod:
            max_prod = temp_prod_list[i]
            max_key = temp_key_list[i]

    products_list.append(max_prod)
    keys_list.append(max_key)

    final_prod = products_list[0]
    final_key = keys_list[0]
    for i in range(len(products_list)):
        if products_list[i] > final_prod:
            final_prod = products_list[i]
            final_key = keys_list[i]


    print(problem11.__doc__)
    print("    Answer: The largest product of 4 adjacent numbers is {product}, which is the product of the 4 numbers {num1} * {num2} * {num3} * {num4}.".format(product = final_prod, num1 = final_key[0], num2 = final_key[1], num3 = final_key[2], num4 = final_key[3]))