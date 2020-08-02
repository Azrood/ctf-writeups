# PolyRSA

We're given a file [`out.txt`](out.txt) where we're given `p` a prime number. `n` a polynome, and m^65537, a polynome (the ciphertext).

Anyway, after searching we can find this paper that talks about the specifications of polynomial RSA.

https://laur.lau.edu.lb:8443/xmlui/bitstream/handle/10725/5497/Modified.pdf


We can see the algorithm for key generation in the paper:
```
Algorithm 4: (RSA polynomials key generation).
1. Generate a random odd prime integer p.
2. Generate two irreducible polynomial h(x) and g(x)
in Zp[x].
3.Reduce the polynomial f(x) = h(x)g(x) in Zp[x].
4.Compute φ(f(x)) = (p^s− 1)(p^r− 1) the order of U(Zp[x]/<f(x)>).
5. Select an integer e in the interval [2, φ(f(x))−1]
such that (e, φ(f(x))) = 1.
6. Use the extended Euclidean algorithm to determine
its inverse d modulo φ(f(x)).
7.A's public-key is (p, f(x), e), A's private-key is
(p, d, g(x), h(x)). 
```

We already have the prime integer `p`. Our `n` is the polynome, we need to factorize it to get 2 irreducible polynomes `h(x)` and `g(x)`.

Using Sage:
```Sage
sage: p=2470567871
sage: R.<x> = PolynomialRing(Zp(p,1))
sage: n = #too long, retrieve it from the file out.txt
sage: n.factor()
```

We find 2 irreducible polynomes, with degree 127 and the other with degree 128.

Going on with the next step, we can calculate phi(n) which is (p^r -1)(p^s-1), `s` and `r` are the degree of the 2 irreducible polynome respectively.

In our case `s=127` and `r=128`, after calculating phi, we can compute the inverse of `e` (which is 65537) modulo phi.

```Python
from Crypto.Util.number import inverse
phi = (p**r - 1) * (p**s - 1)
d = inverse(e,phi)
```

Now that we have the private exponent `d`, we can decrypt the cipher. (let's consider c =  m^65537)

We can recover the plaintext (or more like, the plaintext-polynome ?) by computing `c^d mod n`

With Sage, we can recover the polynome. (It takes a lot of time to compute)
```Sage
sage: p=2470567871
sage: R.<x> = PolynomialRing(Zp(p,1))
sage: RES = pow(c, d, n)
```

We find the original polynome, and we can notice that the coefficients are < 255, so each coefficient is a character of the flag.

```Sage
sage: RES.coefficients()
[105, 110, 99, 116, 102, 123, 97, 110, 100, 95, 105, 95, 52, 109, 95, 105, 114, 48, 110, 95, 109, 52, 110,125]
```

We can then get the flag
```Py
print(''.join(chr(c) for c in coefficients))
```

### flag
`inctf{and_i_4m_ir0n_m4n}`


