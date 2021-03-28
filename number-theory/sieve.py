from itertools import repeat

def len_range(start, stop, step=1):
  return (stop - start) // step + 1

def sieve(n):
  if n < 2:
    return []

  primes = [2]
  is_prime = [True] * n
  for k in range(3, n, 2):
    if is_prime[k]:
      primes.append(k)
      is_prime[3*k : n : 2*k] = repeat(False, len_range(3*k, n, 2*k))

  return primes

def seg_sieve(n):
  if n < 2:
    return []

  primes = [2]
  is_prime = [True] * n
  for k in range(3, n, 2):
    if is_prime[k]:
      primes.append(k)
      is_prime[3*k : n : 2*k] = repeat(False, len_range(3*k, n, 2*k))

  return primes

if __name__ == '__main__':
  for p in sieve(100):
    print(p)
