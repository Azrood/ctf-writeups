# 4k-RSA
```
Only n00bz use 2048-bit RSA. True gamers use keys that are at least 4k bits long, no matter how many primes it takes...
```

We are given a text file `4k-rsa-public-key.txt` where we can find `e` `n` and `c`.

From the description challenge we can deduce that multiple primes are used to calculate `n`. So [alpertron go brrrr.](https://www.alpertron.com.ar/ECM.HTM).

Since `n` is a product of multiple primes, we can factorize it quickly even if it's a 4096-bit integer, and alpertron gives us the Euler's totien `phi`. After that, it's basic RSA decryption.

Calculate the private exponent `d`

```Python

d = inverse(e, phi)
```
And decrypt the message
```Python
m = pow(c, d, n)
print(long_to_bytes(m))
```

### Flag
flag{t0000_m4nyyyy_pr1m355555}
