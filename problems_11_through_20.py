"""
A module that holds the functions that calculate the solutions to Project Euler problems 11 through 20.
"""
#######################################################  Setup  ####################################################################
import numpy as np
import os
my_path = os.path.abspath(os.path.dirname(__file__))
numbers_path = os.path.join(my_path, "numbers.txt")
triangle_path = os.path.join(my_path, "triangle.txt")

import string
lowercase = string.ascii_lowercase
lowercase = lowercase + ' -'

#####################################################  End Setup  #################################################################

#Problem 11
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
    86 56 00 48 35 71 \033[92m89\033[00m 07 05 44 44 37 44 60 21 58 51 54 17 58
    19 80 81 68 05 \033[92m94\033[00m 47 69 28 73 92 13 86 52 17 77 04 89 55 40
    04 52 08 83 \033[92m97\033[00m 35 99 16 07 97 57 32 16 26 26 79 33 27 98 66
    88 36 68 \033[92m87\033[00m 57 62 20 72 03 46 33 67 46 55 12 32 63 93 53 69
    04 42 16 73 38 25 39 11 24 94 72 18 08 46 29 32 40 62 76 36
    20 69 36 41 72 30 23 88 34 62 99 69 82 67 59 85 74 04 36 16
    20 73 35 29 78 31 90 01 74 31 49 71 48 86 81 16 23 57 05 54
    01 70 54 71 83 51 54 69 16 92 33 48 61 43 52 01 89 19 67 48

    The product of these numbers is 26 × 63 × 78 × 14 = 1788696.

    What is the greatest product of four adjacent numbers in the same direction (up, down, left, right, or diagonally) in the 20×20 grid?
    
    Note: The four numbers whose product is the answer have been marked in green.
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
    print("    Answer: The largest product of 4 adjacent numbers is {product}, which is the product of the 4 numbers \
{num1} * {num2} * {num3} * {num4}.".format(product = final_prod, num1 = \
final_key[0], num2 = final_key[1], num3 = final_key[2], num4 = final_key[3]))

#Problem 12
def problem12():
    """
    Project Euler Problem 12.
    https://projecteuler.net/problem=12

    The problem:

    The sequence of triangle numbers is generated by adding the natural numbers. So the 7th triangle number would be 1 + 2 + 3 + 4 + 5 + 6 + 7 = 28. 
    The first ten terms would be:

    1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

    Let us list the factors of the first seven triangle numbers:

        1: 1
        3: 1,3
        6: 1,2,3,6
        10: 1,2,5,10
        15: 1,3,5,15
        21: 1,3,7,21
        28: 1,2,4,7,14,28

    We can see that 28 is the first triangle number to have over five divisors.

    What is the value of the first triangle number to have over five hundred divisors?
    """
    #Here we can use the fact that triangle_number_n is given by n*(n+1)/2
    def num_factors(n: int):
        """
        Finds the number of factors of n.
        """
        factor_list = []
        for i in range(1, int(n ** 0.5 + 1)):
            if n % i == 0:
                if (n/i == i):
                    factor_list.append(i)
                else:
                    factor_list.append(i)
                    factor_list.append(n/i)
        return len(factor_list)
    
    n = 1
    final = 0
    while True:
        triangle_num = (n * (n + 1)) / 2
        if num_factors(triangle_num) > 500:
            final = triangle_num
            break
        n += 1

    print(problem12.__doc__)
    print("    Answer: The first triangle_number with over 500 factors is {num}.".format(num = final))

#Problem 13
def problem13():
    """
    Project Euler Problem 13
    https://projecteuler.net/problem=13

    The problem:

    Work out the first ten digits of the sum of the following one-hundred 50-digit numbers.

    37107287533902102798797998220837590246510135740250
    46376937677490009712648124896970078050417018260538
    74324986199524741059474233309513058123726617309629
    91942213363574161572522430563301811072406154908250
    23067588207539346171171980310421047513778063246676
    89261670696623633820136378418383684178734361726757
    28112879812849979408065481931592621691275889832738
    44274228917432520321923589422876796487670272189318
    47451445736001306439091167216856844588711603153276
    70386486105843025439939619828917593665686757934951
    62176457141856560629502157223196586755079324193331
    64906352462741904929101432445813822663347944758178
    92575867718337217661963751590579239728245598838407
    58203565325359399008402633568948830189458628227828
    80181199384826282014278194139940567587151170094390
    35398664372827112653829987240784473053190104293586
    86515506006295864861532075273371959191420517255829
    71693888707715466499115593487603532921714970056938
    54370070576826684624621495650076471787294438377604
    53282654108756828443191190634694037855217779295145
    36123272525000296071075082563815656710885258350721
    45876576172410976447339110607218265236877223636045
    17423706905851860660448207621209813287860733969412
    81142660418086830619328460811191061556940512689692
    51934325451728388641918047049293215058642563049483
    62467221648435076201727918039944693004732956340691
    15732444386908125794514089057706229429197107928209
    55037687525678773091862540744969844508330393682126
    18336384825330154686196124348767681297534375946515
    80386287592878490201521685554828717201219257766954
    78182833757993103614740356856449095527097864797581
    16726320100436897842553539920931837441497806860984
    48403098129077791799088218795327364475675590848030
    87086987551392711854517078544161852424320693150332
    59959406895756536782107074926966537676326235447210
    69793950679652694742597709739166693763042633987085
    41052684708299085211399427365734116182760315001271
    65378607361501080857009149939512557028198746004375
    35829035317434717326932123578154982629742552737307
    94953759765105305946966067683156574377167401875275
    88902802571733229619176668713819931811048770190271
    25267680276078003013678680992525463401061632866526
    36270218540497705585629946580636237993140746255962
    24074486908231174977792365466257246923322810917141
    91430288197103288597806669760892938638285025333403
    34413065578016127815921815005561868836468420090470
    23053081172816430487623791969842487255036638784583
    11487696932154902810424020138335124462181441773470
    63783299490636259666498587618221225225512486764533
    67720186971698544312419572409913959008952310058822
    95548255300263520781532296796249481641953868218774
    76085327132285723110424803456124867697064507995236
    37774242535411291684276865538926205024910326572967
    23701913275725675285653248258265463092207058596522
    29798860272258331913126375147341994889534765745501
    18495701454879288984856827726077713721403798879715
    38298203783031473527721580348144513491373226651381
    34829543829199918180278916522431027392251122869539
    40957953066405232632538044100059654939159879593635
    29746152185502371307642255121183693803580388584903
    41698116222072977186158236678424689157993532961922
    62467957194401269043877107275048102390895523597457
    23189706772547915061505504953922979530901129967519
    86188088225875314529584099251203829009407770775672
    11306739708304724483816533873502340845647058077308
    82959174767140363198008187129011875491310547126581
    97623331044818386269515456334926366572897563400500
    42846280183517070527831839425882145521227251250327
    55121603546981200581762165212827652751691296897789
    32238195734329339946437501907836945765883352399886
    75506164965184775180738168837861091527357929701337
    62177842752192623401942399639168044983993173312731
    32924185707147349566916674687634660915035914677504
    99518671430235219628894890102423325116913619626622
    73267460800591547471830798392868535206946944540724
    76841822524674417161514036427982273348055556214818
    97142617910342598647204516893989422179826088076852
    87783646182799346313767754307809363333018982642090
    10848802521674670883215120185883543223812876952786
    71329612474782464538636993009049310363619763878039
    62184073572399794223406235393808339651327408011116
    66627891981488087797941876876144230030984490851411
    60661826293682836764744779239180335110989069790714
    85786944089552990653640447425576083659976645795096
    66024396409905389607120198219976047599490197230297
    64913982680032973156037120041377903785566085089252
    16730939319872750275468906903707539413042652315011
    94809377245048795150954100921645863754710598436791
    78639167021187492431995700641917969777599028300699
    15368713711936614952811305876380278410754449733078
    40789923115535562561142322423255033685442488917353
    44889911501440648020369068063960672322193204149535
    41503128880339536053299340368006977710650566631954
    81234880673210146739058568557934581403627822703280
    82616570773948327592232845941706525094512325230608
    22918802058777319719839450180888072429661980811197
    77158542502016545090413245809786882778948721859617
    72107838435069186155435662884062257473692284509516
    20849603980134001723930671666823555245252804609722
    53503534226472524250874054075591789781264330331690
    """
    #For this problem we'll use a little cheat. Since we only need the first 10 digits
    #of the total sum, I'll only add the first 15 digits of each number.
    #The reason one can guarantee this will work is because even though adding only the first 15 digits of each number
    #will lead to an error in the accuracy of the least significant digits of the sum, since we're adding 50 such 
    #numbers the final sum is obviously guaranteed to have more than 10 digits, and thus when taking only the 10
    #most significant digits we will have nullified the effect of the error.
    #Using only the first 15 digits makes our code much more space-efficient, since the amount of memory required to store
    #100 15-digit numbers is obviously much less than the amount required to store 100 50-digit numbers.
    number_list = []
    with open(numbers_path, 'r') as file:
        num = file.readline()
        while num:
            temp = num[:15]
            number_list.append(int(temp))
            num = file.readline()

    final_sum_string = str(sum(number_list))[:10]

    print(problem13.__doc__)
    print("    Answer: The ten most significant digits of the final sum are {num}.".format(num = final_sum_string))

#Problem 14
def problem14():
    """
    Project Euler Problem 14
    https://projecteuler.net/problem=14

    The problem:

    The following iterative sequence is defined for the set of positive integers:

    n → n/2 (n is even)
    n → 3n + 1 (n is odd)

    Using the rule above and starting with 13, we generate the following sequence:
    13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1

    It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms.
    Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.

    Which starting number, under one million, produces the longest chain?

    NOTE: Once the chain starts the terms are allowed to go above one million.
    """

    def collatz_length(num: int):
        """
        Returns the length of the Collatz Sequence of num.
        """
        temp = num
        counter = 1
        if temp == 1:
            return 1
        while temp != 1:
            assert temp > 0, "Something's gone wrong in your calculations"
            counter += 1
            if temp % 2 == 0:
                temp = temp//2
            else:
                temp = 3 * temp + 1
        return counter

    lengths_list = []
    # print("Appending to lengths_list")
    for i in range(1, 1000000):
        # print(i)
        lengths_list.append(collatz_length(i))

    max_length = lengths_list[0]
    max_length_num = 1
    # print("Inside lengths_list")
    for i in range(999998):
        # print(i)
        if lengths_list[i] > max_length:
            max_length = lengths_list[i]
            max_length_num = i + 1

    print(problem14.__doc__)
    print("    Answer: The number with the longest Collatz sequence is {num} with a sequence length of \
{length}.".format(num = max_length_num, length = max_length))

#Problem 15
def problem15():
    """
    Project Euler Problem 15
    https://projecteuler.net/problem=15

    The problem:

    Starting in the top left corner of a 2×2 grid, and only being able to move to the right and down, there are \
exactly 6 routes to the bottom right corner.

    How many such routes are there through a 20×20 grid?
    """
    #This problem can be simplified by a series of inferences.
    #First, we see that the Manhattan Distance of the bottom right corner from the top left corner is 40
    #Secondly, to get from the top left to the bottom right, it will always take us 40 steps (from the above inference)
    #ie 20 steps to the right and 20 steps down.
    #So, this problem then simplifies to "How many permutations of 40 steps such that 20 steps are to the right
    #and 20 steps are downwards exist?", the answer to which is:
    #    
    #                40!
    #           -------------
    #             20! * 20!
    #
    # At this point the program merely serves as a calculator!

    answer = int(fact(40)/(fact(20) ** 2))
    print(problem15.__doc__)
    print("    Answer: The total number of routes in a 20x20 grid is {answer}.".format(answer = answer))

#Problem 16
def problem16():
    """
    Project Euler Problem 16
    https://projecteuler.net/problem=16

    The problem:

    2**15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

    What is the sum of the digits of the number 2**1000?
    """
    num = 2**1000

    sum_of_digits = sum_digits(num)

    print(problem16.__doc__)
    print("    Answer: The sum of the digits of 2**1000 is {num}.".format(num = sum_of_digits))
    

#Problem 17
def problem17():
    """
    Project Euler Problem 17
    https://projecteuler.net/problem=17

    The problem:

    If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

    If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?

    NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two) contains 23 letters and 115 (one hundred and fifteen) contains 20 letters. 
    The use of "and" when writing out numbers is in compliance with British usage.
    """
    def convert_to_words(num: int):
        """
        Converts num to its English representation.

        For example, convert_to_words(5) = 'five'

        //This was such a pain to write. Not because it's difficult, but because it's mind-bogglingly annoying.
        //This function is not perfect. I could've implemented a version where the string for any number
        // 20 <= num < 100 does not have a trailing hyphen ('-') but I didn't bother because it's useless for the 
        //purpose of this problem. 
        """
        number_dict = {
            1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five',
            6: 'six', 7: 'seven', 8: 'eight', 9: 'nine', 10: 'ten',
            11: 'eleven', 12: 'twelve', 13: 'thirteen', 14: 'fourteen', 15: 'fifteen',
            16: 'sixteen', 17: 'seventeen', 18: 'eighteen', 19: 'nineteen'
        }
        if num == 0:
            return ''
        
        elif num == 1000:
            return 'one thousand'
        
        elif num in number_dict:
            return number_dict.get(num)
        
        elif num < 100:
            if (20 <= num) and (num < 30):
                return 'twenty-' + convert_to_words(num % 10)
            elif (30 <= num) and (num < 40):
                return 'thirty-' + convert_to_words(num % 10)
            elif (40 <= num) and (num < 50):
                return 'forty-' + convert_to_words(num % 10)
            elif (50 <= num) and (num < 60):
                return 'fifty-' + convert_to_words(num % 10)
            elif (60 <= num) and (num < 70):
                return 'sixty-' + convert_to_words(num % 10)
            elif (70 <= num) and (num < 80):
                return 'seventy-' + convert_to_words(num % 10)
            elif (80 <= num) and (num < 90):
                return 'eighty-' + convert_to_words(num % 10)
            elif (90 <= num) and (num < 100):
                return 'ninety-' + convert_to_words(num % 10)
        
        elif (num % 100 == 0):
            return convert_to_words(num//100) + ' hundred'
        
        else: #if 100 <= num < 1000
            if (100 < num) and (num < 200):
                return 'one hundred and ' + convert_to_words(num % 100)
            elif (200 < num) and (num < 300):
                return 'two hundred and ' + convert_to_words(num % 100)
            elif (300 < num) and (num < 400):
                return 'three hundred and ' + convert_to_words(num % 100)
            elif (400 < num) and (num < 500):
                return 'four hundred and ' + convert_to_words(num % 100)
            elif (500 < num) and (num < 600):
                return 'five hundred and ' + convert_to_words(num % 100)
            elif (600 < num) and (num < 700):
                return 'six hundred and ' + convert_to_words(num % 100)
            elif (700 < num) and (num < 800):
                return 'seven hundred and ' + convert_to_words(num % 100)
            elif (800 < num) and (num < 900):
                return 'eight hundred and ' + convert_to_words(num % 100)
            elif (900 < num) and (num < 1000):
                return 'nine hundred and ' + convert_to_words(num % 100)


    def count_letters(num_string: str):
        """
        Counts the number of characters in string, without counting spaces or hyphens
        """
        counter = 0
        for i in num_string:
            if i not in lowercase:
                raise ValueError("{string} cannot be processed by the function.".format(string = num_string))
            if i not in [' ', '-']:
                counter += 1
        return counter

    total_letters = 0

    for i in range(1,1001):
        total_letters += count_letters(convert_to_words(i))

    print(problem17.__doc__)
    print("    Answer: If all the numbers from 1 to 1000 were written out, you'd need {num} letters.".format(num = total_letters))

#Problem 18
def problem18():
    """
    Project Euler Problem 18
    https://projecteuler.net/problem=18

    The Problem:



By starting at the top of the triangle below and moving to adjacent numbers on the row below, the maximum total from top to bottom is 23.

                    \033[91m3\033[00m
                   \033[91m7\033[00m 4
                  2 \033[91m4\033[00m 6
                 8 5 \033[91m9\033[00m 3

That is, 3 + 7 + 4 + 9 = 23.

Find the maximum total from top to bottom of the triangle below:

                                                75
                                              95 64
                                            17 47 82
                                           18 35 87 10
                                         20 04 82 47 65
                                        19 01 23 75 03 34
                                      88 02 77 73 07 63 67
                                     99 65 04 28 06 16 70 92
                                    41 41 26 56 83 40 80 70 33
                                  41 48 72 33 47 32 37 16 94 29
                                53 71 44 65 25 43 91 52 97 51 14
                               70 11 33 28 77 73 17 78 39 68 17 57
                             91 71 52 38 17 14 91 43 58 50 27 29 48
                            63 66 04 68 89 53 67 30 73 16 69 87 40 31
                          04 62 98 27 23 09 70 98 73 93 38 53 60 04 23

    """
    triangle = []
    with open(triangle_path, 'r') as file:
        string = file.readline()
        while string:
            string = string[:-1]
            triangle.append(string.split(' '))
            string = file.readline()
    
    newtriangle = []
    for row in triangle:
        rowlist = []
        for numstring in row:
            num = int(numstring)
            rowlist.append(num)
        newtriangle.append(rowlist)
    triangle = newtriangle

    number_list = []
    for i in reversed(range(len(triangle) - 1)):
        for j in range(len(triangle[i])):
            triangle[i][j] += max(triangle[i + 1][j], triangle[i + 1][j + 1])
    largest_sum = triangle[0][0]
    
    print(problem18.__doc__)
    print('    Answer: The max. total from top to bottom is {string} = {totalsum}.'.\
format(string = ' + '.join(number_list), totalsum = largest_sum))

#Problem 19
def problem19():
    """
    Project Euler Problem 19
    https://projecteuler.net/problem=19

    The problem:

    You are given the following information, but you may prefer to do some research for yourself.

        - 1 Jan 1900 was a Monday.

        - Thirty days has September,
          April, June and November.
          All the rest have thirty-one,
          Saving February alone,
          Which has twenty-eight, rain or shine.
        And on leap years, twenty-nine.

        - A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.

    How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?
    """
    #We will map each day of the week to a number from 0 to 6, with 0 being Sunday and 6 being Saturday

    month_dict = { #stores the number of days in every month
        0: 31,
        1: 28,
        2: 31,
        3: 30,
        4: 31,
        5: 30,
        6: 31,
        7: 31,
        8: 30,
        9: 31,
        10: 30,
        11: 31
    }

    counter = 0
    first = 2 #the first of January 1901 was a Tuesday

    for year in range(1901, 2001):
        if year % 4 == 0:
            month_dict[1] = 29
        else:
            month_dict[1] = 28

        for month in range(12):
            if first == 0:
                counter += 1
            first += month_dict[month]
            first = first % 7
    
    print(problem19.__doc__)
    print("    Answer: {num} Sundays fell on the first of the month during 1 Jan 1901 to 31 Dec 2000.".format(num = counter))

#Problem 20
def problem20():
    """
    Project Euler Problem 20
    https://projecteuler.net/problem=20

    The problem:

    n! means n × (n − 1) × ... × 3 × 2 × 1

    For example, 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800,
    and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.

    Find the sum of the digits in the number 100!
    """

    print(problem20.__doc__)
    print("Answer: The sum of the digits of 100! is {num}".format(num = sum_digits(fact(100))))
#------------------------------------------------------------------------------------------------------------------------------------------
#--------------------------------------------------------- Helper functions ---------------------------------------------------------------

def sum_digits(num: int):
    """
    Returns the sum of the digits of num.
    """
    sum_of_digits = 0
    while True:
        if num < 10:
            sum_of_digits += num
            break
        else:
            sum_of_digits += num % 10
            num = num // 10
    return sum_of_digits

def fact(n: int):
    """
    Function to calculate the factorial of n.
    """
    if n == 1:
        return 1
    return n * fact(n - 1)