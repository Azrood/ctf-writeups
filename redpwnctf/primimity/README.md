# Primimity

## Challenge

```
People claim that RSA with two 1024-bit primes is secure. But I trust no one. That's why I use three 1024-bit primes.

I even created my own prime generator to be extra cautious!
```

We're given two files, the source code `primimity.py` and `primimity-public-key.txt` where there is a public key (n, e and c)

let's check the source code. We notice two functions.

This function returns the next prime number.

```Python
def find_next_prime(n):
    if n <= 1:
        return 2
    elif n == 2:
        return 3
    else:
        if n % 2 == 0:
            n += 1
        else:
            n += 2
        while not isPrime(n):
            n += 2
        return n
```
This function generates 3 primes

```Python
def prime_gen():
    i = getRandomNBitInteger(1024)
    d = getRandomNBitInteger(8)
    for _ in range(d):
        i = find_next_prime(i)
    p = find_next_prime(i)
    d = getRandomNBitInteger(8)
    for _ in range(d):
        i = find_next_prime(i)
    q = find_next_prime(i)
    d = getRandomNBitInteger(8)
    for _ in range(d):
        i = find_next_prime(i)
    r = find_next_prime(i)
    return (p,q,r)
```

Okay, let's take a closer look at what we have in this function.
```Python
 i = getRandomNBitInteger(1024)
 d = getRandomNBitInteger(8)
 for _ in range(d):
     i = find_next_prime(i)
 p = find_next_prime(i)
```
We start with a 1024-bit `i = getRandomNBitInteger(1024)` random integer and 8-bit random integer `d = getRandomNBitInteger(8)`.

Since `d` is a 8-bit integer, its maximum value is `2**8` which is `256`. Let's consider a worst-case scenario and assume that all the 8-bit integer generated are 256.

Same is done for `q` and `r`
```Python
d = getRandomNBitInteger(8)
for _ in range(d):
    i = find_next_prime(i)
q = find_next_prime(i)
```
We notice that the primes are pretty close. (at most an order of `10**5`) and that `p < q < r`. In the public key `n` is a product of primes, so in our case, `n = p * q * r`.
Since `p` ≈ `q` ≈ `r` and `n = p * q * r`. Then `∛n ≈ p`.

Let's calculate the cube root of n using this function.
```Python
def root3rd(x):
    y, y1 = None, 2
    while y!=y1:
        y = y1
        y3 = y**3
        d = (2*y3+x)
        y1 = (y*(y3+2*x)+d//2)//d
    return y
```
`root = root3rd(n)` We have an approximation of `p`. We can do `root = root - 300000` to be under p. So now that we are close to `p` we just have to find it, and from there find the other primes.
If we find a number `i` such that `gcd(i,n)!=1` then `i` is a divisor of `n`. We know that `n = p * q * r` so using this function, we can find the first divisor of `n` which will be `p`.

```Python

def calculate_prime_divisor(p,mod):
    while True:
        p=find_next(p)
        if gcd(p,mod) != 1:
            return p
```

```Python
p = calculate_prime_divisor(root,n)
```
Since we found p, we wll start iterating from `p` and find a divisor of `n//p = q*r`

```Python
q = calculate_prime_divisor(p, n//p)
```

Now that we found `q` we can calculate `r`.
```Python
r = n//(p*q)
```

Now that we found the primes, it's pretty straightforward, we calculate Euler's totien phi.
```Python
phi = (p-1) * (q-1) * (r-1)
```
We calculate the private exponent and decrypt the cipher.
```Python
d = inverse(e,phi)
m=pow(c, d, n)
print(long_to_bytes(m))
```
## Flag
flag{pr1m3_pr0x1m1ty_c4n_b3_v3ry_d4ng3r0u5}

