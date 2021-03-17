print("Q1")
my_list = [1,3,5,7,9]
print(my_list)
my_list = [1,3,5,7,9]
print(my_list[1:])
my_list = [1,3,5,7,9]
print(my_list[2:4])
my_list = [1,3,5,7,9]
print(my_list[1:4])
my_list = [1,3,5,7,9]
print(my_list[1:-1])

print("Q2")
print([1])
print((1))
print((1,))
print(tuple([1]))

print("Q3")
my_list = [1, 3, 5, 7, 9]
my_list.reverse()
print(my_list.reverse())

fib =[0,1]
for num in range(20):
    fib.append(fib[num] + fib[num+1])
    print(num, fib[-1])

"""
Implement the Sieve of Eratosthenes
https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes
"""
print("Q5")
def compute_primes(bound):
    """
    Return a list of the prime numbers in range(2, bound)
    """
    count=0
    answer = list(range(2, bound))
    for divisor in range(2, bound):
        #print(divisor,answer)
        for i in range(2,(divisor//2+1)):
            if (divisor % i ==0):
                if divisor in answer:
                    answer.remove(divisor)
                
    return answer

print(len(compute_primes(30)))
print(len(compute_primes(200)))
print(len(compute_primes(2000)))
