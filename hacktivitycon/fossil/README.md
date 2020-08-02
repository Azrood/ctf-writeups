# Fossil

We're given a file [fossil](fossil/fossil)

What happens is that the flag is base64 encoded, and then each byte is xored with the next one and then converted to hex.
```Python
e = b(f)
    z = []
    i = 0
    while i < len(e):
        z += [ e[i] ^ e[((i + 1) % len(e))]]
        i = i + 1
c = h(bytearray(z))
```

The ciphertext is `c = b'37151032694744553d12220a0f584315517477520e2b3c226b5b1e150f5549120e5540230202360f0d20220a376c0067'`
Let's hex decode it. and covnert it to a list we get
```
c = [55, 21, 16, 50, 105, 71, 68, 85, 61, 18, 34, 10,
    15, 88, 67, 21, 81, 116, 119, 82, 14, 43, 60, 34,
    107, 91, 30, 21, 15, 85, 73, 18, 14, 85, 64, 35,
    2, 2, 54, 15, 13, 32, 34, 10, 55, 108, 0, 103]
```
We know the length of our base64 encoded text which is `48`
We notice that `c[-2]` is `0`, that means `e[46]^e[47] = 0` which means `e[46] = e[47] `those are the 2 last chars, they are very likely to be `==` from the padding.

We have `c[-1] = 103` so `e[47] ^ e[0] = 103` then `e[0]=e[47]^103` we have `e[47]= b'='` after converting it to int we can recover `e[0]` `e[0]=90`

Now that we hae e[0] we can recover the flag with this simple script.
```Python
from base64 import b64decode
f=[0]*48
for i in range(48):
    f[i] = f[i-1] ^ c[i-1]
b64decode(''.join(chr(x) for x in f).encode())
```

## flag
flag{tyrannosauras_xor_in_reverse}
