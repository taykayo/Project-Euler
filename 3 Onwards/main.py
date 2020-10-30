# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from numpy import multiply
from math import sqrt
from math import prod
from collections import Counter

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.

# 3
def prime_factorization(n: int):
    primes = []
    while n % 2 == 0:
        primes.append(2)
        n = n / 2

    for i in range(3, int(sqrt(n))+1, 2):

        while n % i == 0:
            primes.append(i)
            n = n / i
    if n > 2:
        primes.append(n)
    return primes
    # print(primes)
# 3/

# 4

def find_largest_palindrome():

    def is_palin(i):
        return str(i) == str(i)[::-1]

    max = 0

    for i in range(100, 999, 1):
        for j in range(100, i, 1):
            prod = j*i
            if is_palin(prod) and prod > max:
                max = prod
    print(max)

# 4/

# 5

def find_smallest_common_factor(numbers: list):
    prime_numbers = []
    for n in numbers:
        prime_numbers.append(prime_factorization(n))

    prime_counter = {} # master dict of highest occurences for each prime #
    for primes in prime_numbers: # for each number 1-20

        occurences = Counter(primes)  # generate list of each prime number occurences
        for num in occurences.keys(): # for each key in that counter list
            try:
                if occurences[num] > prime_counter[num]: # if the value is higher than the master list value for that key
                    prime_counter[num] = occurences[num] # set the master list to value
            except KeyError:
                prime_counter[num] = occurences[num]

    prime_prods = []
    for key in prime_counter.keys():
        prime_prods.append(key**(prime_counter[key]))

    return(prod(prime_prods))

# 5/

# 6

def difference_squares(n):
    #Find the difference between the sum of the squares of the first n natural numbers and the square of the sum
    numbers = [x for x in range(n+1)]
    number_sum = sum(numbers)
    squares = [x**2 for x in range(n+1)]
    square_sum = sum(squares)


    return((square_sum) -(number_sum**2))

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

    for x in range(len(str(n))-13):
        number_list = [int(i) for i in str(n)[x:x+13]]
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

    for a in range(1, (sum//3)+1):
        for b in range(a, (sum//2), 1):
            c = sum - a - b
            if (a**2)+(b**2) == (c**2):
                return f"a: {a}, b: {b}, c: {c}"
    return "idk man"

# 9/


# 10

def sum_all_primes_until(n):

    # we don't bother checking 1, 2, or any even number
    # these are all numbers to test, going to sieve through them
    numbers = set(range(3, n+1, 2))

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





# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
    #get_primes_beneath_limit(int(600851475143))
    # print(find_smallest_common_factor(list(range(1, 20))))
    # print(difference_squares(100))
    # print (find_nth_prime(10001))
    # print(find_largest_adj_prod(7316717653133062491922511967442657474235534919493496983520312774506326239578318016984801869478851843858615607891129494954595017379583319528532088055111254069874715852386305071569329096329522744304355766896648950445244523161731856403098711121722383113622298934233803081353362766142828064444866452387493035890729629049156044077239071381051585930796086670172427121883998797908792274921901699720888093776657273330010533678812202354218097512545405947522435258490771167055601360483958644670632441572215539753697817977846174064955149290862569321978468622482839722413756570560574902614079729686524145351004748216637048440319989000889524345065854122758866688116427171479924442928230863465674813919123162824586178664583591245665294765456828489128831426076900422421902267105562632111110937054421750694165896040807198403850962455444362981230987879927244284909188845801561660979191338754992005240636899125607176060588611646710940507754100225698315520005593572972571636269561882670428252483600823257530420752963450))
    # print(find_pythagorean_triplet())
    print(sum_all_primes_until(2000000))
