# Description
Alice sent over a couple of images with sensitive information to Bob, encrypted with a pre-shared key. It is the most secure encryption scheme, theoretically...

# Solution

the pre-shared key hints that maybe the 2 images got xored with same key.

If P1 xor K = C1
	P2 xor K = C2
we can leak the plaintext because :
C1 xor C2 = P1 xor P2

simple script to xor images :
```
from PIL import Image, ImageChops
im1 = Image.open("image1.png").convert("1")
im2 = Image.open("image2.png").convert("1")
im3 = ImageChops.logical_xor(im1, im2)
im3.show()
```

## flag
flag{0n3_t1m3_P@d!}
