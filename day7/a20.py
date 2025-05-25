def is_prime(n):
    if n < 2:
        return False
    for i in range(2,int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

nums = list(range(1,30))
primes = list(filter(is_prime,nums))
print(primes)