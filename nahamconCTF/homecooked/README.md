# Homecooked

![img](https://raw.githubusercontent.com/ret2basic/ret2basic.github.io/master/img/NahamCon_CTF_2020/Crypto/Homecooked.png)

We get the challenge file `decrypt.py`:

In the file given, this function checks if a number is prime.

```Python
def a(num):
    if (num > 1):
        for i in range(2,num):
            if (num % i) == 0:
                return False
                break
        return True
    else:
        return False

```


This function checks if a number is a palindrome
```Python
def b(num):
    my_str = str(num)
    rev_str = reversed(my_str)
    if list(my_str) == list(rev_str):
       return True
    else:
       return False

```

This block of code decrypts the cipher by xoring each character with a palindromic prime, but it takes too long to compute. 

```Python
while(count < len(cipher)):
    if (a(num)):
        if (b(num)):
            print(chr(int(cipher[count]) ^ num), end='', flush=True)
            count += 1
            if (count == 13):
                num = 50000
            if (count == 26):
                num = 500000
    else:
        pass
    num+=1
```
So we can just retrieve the primes needed since we know the length of the cipher. Notice that at 13th index, we jump to 50000 and at 26th index we jump to 500000.
List of palindromic primes can be found at : https://oeis.org/A002385/b002385.txt.

```Python
primes = [2,3,5,7,11,101,131,151,181,191,313,353,373,70207,
70507,
70607,
71317,
71917,
72227,
72727,
73037,
73237,
73637,
74047,
74747,
75557,
1003001,
1008001,
1022201,
1028201,
1035301,
1043401,
1055501,
1062601,
1065601,
1074701,
1082801,
1085801,
1092901,
1093901,  
       ]

for i, num in enumerate(primes):
    print(chr(int(cipher[i]) ^ num), end='', flush=True)

```

## flag

flag{pR1m3s_4re_co0ler_Wh3n_pal1nDr0miC}
