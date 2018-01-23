'''
Backwards Read Primes are primes that when read backwards in base 10 (from right to left) are a different prime. (This rules out primes which are palindromes.)

Find all Backwards Read Primes between two positive given numbers (both inclusive), the second one being greater than the first one. The resulting array or the resulting string will be ordered following the natural order of the prime numbers.
'''

def backwards_primes(a, b):
    def backward(n):
        n = list(str(n));
        n.reverse()
        return int(''.join(n))

    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2,int(n**0.5)+1):
            if n % i == 0:
                return False
        return True

    def is_backward_prime(n):
        bwn = backward(n)
        return is_prime(n) and is_prime(bwn) and (n != bwn)

    return sorted([num for num in range(a, b+1) if is_backward_prime(num)])
