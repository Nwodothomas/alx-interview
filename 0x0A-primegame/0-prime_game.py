#!/usr/bin/python3

def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def calculate_primes_sieve(n):
    sieve = [True] * (n + 1)
    sieve[0] = sieve[1] = False

    for current in range(2, int(n**0.5) + 1):
        if sieve[current]:
            for multiple in range(current * current, n + 1, current):
                sieve[multiple] = False

    primes = [i for i, is_prime in enumerate(sieve) if is_prime]
    return primes

def isWinner(x, nums):
    if x <= 0 or not nums:
        return None

    max_num = max(nums)
    primes = calculate_primes_sieve(max_num)
    
    maria_wins = 0
    ben_wins = 0

    for num in nums:
        prime_count = sum(1 for p in primes if p <= num)
        if prime_count % 2 == 0:
            ben_wins += 1
        else:
            maria_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
