# Hashbrown Casserole
```
Connect here:
nc jh2i.com 50005
```

When we connect we get in output:
`Enter the data required for the first part of the sha1sum to equal hex: 2b695a`

So we will have to bruteforce hashes until the server gives the flag.

Script to solve
```Python
from pwn import *
import hashlib
from itertools import product
from string import ascii_letters, digits

charset = ascii_letters + digits
def calc(alg, target):
    for i in range(0xff):
        for l in product(charset, repeat=i):
            data = ''.join(l).encode()
            if hashlib.__dict__[alg](data).hexdigest()[:len(target)] == target:
                return data

r=remote("jh2i.com", 50005)
context.log_level = 'INFO'
while True:
    line = r.recvline().decode()
    log.info(line)
    target = line.split()[-1]
    alg = line.split()[-5][:-3]
    r.sendline(calc(alg, target))
    log.info(r.recvline())
```
