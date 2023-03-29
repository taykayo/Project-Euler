# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from math import sqrt
from math import prod
from collections import Counter
from PEreuse import prime_factorization


# 3
# Satisfied by:
# PEreuse.prime_factorization(1)


def find_largest_palindrome():
    def is_palin(_):
        return str(_) == str(_)[::-1]

    max = 0

    for i in range(100, 999, 1):
        for j in range(100, i, 1):
            prod = j * i
            if is_palin(prod) and prod > max:
                max = prod
    print(max)


# 5

def find_smallest_common_factor(numbers: list):
    prime_numbers = []
    for n in numbers:
        prime_numbers.append(prime_factorization(n))

    prime_counter = {}  # master dict of highest occurences for each prime #
    for primes in prime_numbers:  # for each number 1-20

        occurences = Counter(primes)  # generate list of each prime number occurences
        for num in occurences.keys():  # for each key in that counter list
            try:
                if occurences[num] > prime_counter[num]:  # if the value is higher than the master list value for that key
                    prime_counter[num] = occurences[num]  # set the master list to value
            except KeyError:
                prime_counter[num] = occurences[num]

    prime_prods = []
    for key in prime_counter.keys():
        prime_prods.append(key ** (prime_counter[key]))

    return prod(prime_prods)


# 5/

# 6

def difference_squares(n):
    # Find the difference between the sum of the squares of the first n natural numbers and the square of the sum
    numbers = [x for x in range(n + 1)]
    number_sum = sum(numbers)
    squares = [x ** 2 for x in range(n + 1)]
    square_sum = sum(squares)

    return (square_sum) - (number_sum ** 2)


# 6/

# 7


def is_prime(num):
    factor = 2
    while (factor * factor <= num):
        if num % factor == 0:
            return False
        factor += 1
    return True


def find_nth_prime(n):
    if n == 1:
        return 2
    count = 1
    num = 1
    while (count < n):
        num += 2  # Because even numbers cannot be prime numbers
        if is_prime(num):
            count += 1
    return num


# 7/

# 8

def find_largest_adj_prod(n):
    prod_list = []

    for x in range(len(str(n)) - 13):
        number_list = [int(i) for i in str(n)[x:x + 13]]
        print(number_list)
        print(prod(number_list))
        prod_list.append(prod(number_list))
    return max(prod_list)


# 8/

# 9

# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product abc.

def find_pythagorean_triplet():
    # Pythagorean triplets exist in a triangle with side rations 3:4:5

    # base values
    sum = 1000

    for a in range(1, (sum // 3) + 1):
        for b in range(a, (sum // 2), 1):
            c = sum - a - b
            if (a ** 2) + (b ** 2) == (c ** 2):
                return f"a: {a}, b: {b}, c: {c}"
    return "idk man"


# 9/


# 10

def sum_all_primes_until(n):
    # we don't bother checking 1, 2, or any even number
    # these are all numbers to test, going to sieve through them
    numbers = set(range(3, n + 1, 2))

    for number in range(3, int(sqrt(n)), 1):

        if number not in numbers:
            # skip rest of loop iteration
            continue

        num = number
        while num < n:
            num += number
            if num in numbers:
                numbers.remove(num)

    return 2 + sum(numbers)


# 11 Largest Product in a grid
# Given the following 20x20 grid: What is the greatest product of four adjacent numbers in the same direction
# (up, down, left, right, or diagonally) in the 20×20 grid?
listOfStr = ("08 02 22 97 38 15 00 40 00 75 04 05 07 78 52 12 50 77 91 08 "
             "49 49 99 40 17 81 18 57 60 87 17 40 98 43 69 48 04 56 62 00 "
             "81 49 31 73 55 79 14 29 93 71 40 67 53 88 30 03 49 13 36 65 "
             "52 70 95 23 04 60 11 42 69 24 68 56 01 32 56 71 37 02 36 91 "
             "22 31 16 71 51 67 63 89 41 92 36 54 22 40 40 28 66 33 13 80 "
             "24 47 32 60 99 03 45 02 44 75 33 53 78 36 84 20 35 17 12 50 "
             "32 98 81 28 64 23 67 10 26 38 40 67 59 54 70 66 18 38 64 70 "
             "67 26 20 68 02 62 12 20 95 63 94 39 63 08 40 91 66 49 94 21 "
             "24 55 58 05 66 73 99 26 97 17 78 78 96 83 14 88 34 89 63 72 "
             "21 36 23 09 75 00 76 44 20 45 35 14 00 61 33 97 34 31 33 95 "
             "78 17 53 28 22 75 31 67 15 94 03 80 04 62 16 14 09 53 56 92 "
             "16 39 05 42 96 35 31 47 55 58 88 24 00 17 54 24 36 29 85 57 "
             "86 56 00 48 35 71 89 07 05 44 44 37 44 60 21 58 51 54 17 58 "
             "19 80 81 68 05 94 47 69 28 73 92 13 86 52 17 77 04 89 55 40 "
             "04 52 08 83 97 35 99 16 07 97 57 32 16 26 26 79 33 27 98 66 "
             "88 36 68 87 57 62 20 72 03 46 33 67 46 55 12 32 63 93 53 69 "
             "04 42 16 73 38 25 39 11 24 94 72 18 08 46 29 32 40 62 76 3 " 
             "20 69 36 41 72 30 23 88 34 62 99 69 82 67 59 85 74 04 36 16 "
             "20 73 35 29 78 31 90 01 74 31 49 71 48 86 81 16 23 57 05 54 "
             "01 70 54 71 83 51 54 69 16 92 33 48 61 43 52 01 89 19 67 48 ").split()


listOfInts = list(map(int, listOfStr))
numberGrid = [listOfInts[20*x:20*x+20] for x in range(20)]
prodMaxLength = 5

def largestGridProd(grid_list, prodmaxlength):
    gridSequences = []

    #  Product directions are going to be referred to by cardinal directions (right = E, down = S)

    # E prod
    gridSequences.extend([grid_list[y][x:x + prodmaxlength] for x in range(len(grid_list)-prodmaxlength+1)
                          for y in range(len(grid_list))])
    # S prod
    for y in range(len(grid_list)-prodmaxlength+1):
        for x in range(len(grid_list)):
            gridSequences.append([grid_list[y][x], grid_list[y+1][x], grid_list[y+2][x], grid_list[y+3][x]])

    # SE prod
    for y in range(len(grid_list)-prodmaxlength+1):
        for x in range(len(grid_list)-prodmaxlength+1):
            gridSequences.append([grid_list[y][x], grid_list[y+1][x+1], grid_list[y+2][x+2], grid_list[y+3][x+3]])


    # SW prod
    for y in range(len(grid_list)-prodmaxlength+1):
        for x in range(prodmaxlength-1, len(grid_list)):
            gridSequences.append([grid_list[y][x], grid_list[y+1][x-1], grid_list[y+2][x-2], grid_list[y+3][x-3]])

    maxProduct = 0
    for _ in gridSequences:
        maxProduct = prod(_) if prod(_) > maxProduct else maxProduct
    return maxProduct

# 12
# The sequence of triangle numbers is generated by adding the natural numbers. So the 7th triangle number would be 1 + 2 + 3 + 4 + 5 + 6 + 7 = 28. The first ten terms would be:
#
# 1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...
#
# Let us list the factors of the first seven triangle numbers:
#
#  1: 1
#  3: 1,3
#  6: 1,2,3,6
# 10: 1,2,5,10
# 15: 1,3,5,15
# 21: 1,3,7,21
# 28: 1,2,4,7,14,28
# We can see that 28 is the first triangle number to have over five divisors.
#
# What is the value of the first triangle number to have over five hundred divisors?

def find_first_integer_500_divisors(starting_number: int):
    # This works by utilizing the divisor formula. To use an example, the number 24 has a prime factorization of
    # 2x2x2x3 = 24   2 appears 3 times, and 3 appears once. We can rewrite this as 24 = 2^3 x 3^1
    # the equation for finding the number of divisors is: d(n) = (a+1)(b+1)(c+1)....where the equation is extended for
    # unique prime factor, n is the number, and a,b,c,... are the exponents of the prime factors.  For n = 24, this is:
    # d(24) = (3+1)(1+1) = (4)(2) = 8
    divisors = 0
    i = starting_number
    triangle_number = 0
    while divisors < 500:
        triangle_number = int(i*(i+1)/2) # Triangle number formula for finding the ith triangle number
        primefactorlist = prime_factorization(triangle_number)
        counterlist = []
        res = []
        for x in primefactorlist:
            if x not in res:
                counterlist.append(primefactorlist.count(x))
                res.append(x)
        counterlist = [x + 1 for x in counterlist]
        divisors = prod(counterlist)
        print(divisors)
        i += 1
    return triangle_number






# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    # get_primes_beneath_limit(int(600851475143))
    # print(find_smallest_common_factor(list(range(1, 20))))
    # print(difference_squares(100))
    # print (find_nth_prime(10001))
    # print(find_largest_adj_prod(7316717653133062491922511967442657474235534919493496983520312774506326239578318016984801869478851843858615607891129494954595017379583319528532088055111254069874715852386305071569329096329522744304355766896648950445244523161731856403098711121722383113622298934233803081353362766142828064444866452387493035890729629049156044077239071381051585930796086670172427121883998797908792274921901699720888093776657273330010533678812202354218097512545405947522435258490771167055601360483958644670632441572215539753697817977846174064955149290862569321978468622482839722413756570560574902614079729686524145351004748216637048440319989000889524345065854122758866688116427171479924442928230863465674813919123162824586178664583591245665294765456828489128831426076900422421902267105562632111110937054421750694165896040807198403850962455444362981230987879927244284909188845801561660979191338754992005240636899125607176060588611646710940507754100225698315520005593572972571636269561882670428252483600823257530420752963450))
    # print(find_pythagorean_triplet())
    # print(sum_all_primes_until(2000000))
    # print(largestGridProd(numberGrid, prodMaxLength))
    # print(find_first_integer_500_divisors(1))