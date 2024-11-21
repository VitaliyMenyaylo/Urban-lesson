numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
# может быть любая последовательность, в любом порядке...
primes = []
not_primes = []
for i in numbers :
    if (i > 0) and (i < 3) : #отсеем отрицательные числа и 0, если они попали по ошибке в список
        primes.append(i)
    elif i > 2 :
        is_prime = True
        for j in range(2, i - 1) :
            if i % j == 0 :
                is_prime = False
                break
        if is_prime :
            primes.append(i)
        else :
            not_primes.append(i)
print ("простые числа",primes)
print("не простые числа",not_primes)
