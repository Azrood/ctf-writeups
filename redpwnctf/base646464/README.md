# Base646464
## Challenge
Encoding something multiple times makes it exponentially more secure!

We're given 2 files `cipher.txt` and `generate.js`

We notice in the file `generate.js` those lines of code

```js
const btoa = str => Buffer.from(str).toString('base64');
```
```js
let ret = flag;
for(let i = 0; i < 25; i++) ret = btoa(ret);
```

Which means that the flag was encoded in base64 25 times. So in order to recover the flag, we only have to decode in base64 the cipher 25 times.

We can solve this with bash.

```bash
for i in {1..25}; do echo "$(cat cipher.txt | base64 -d)" > cipher.txt; done
```

## flag

flag{l00ks_l1ke_a_l0t_of_64s}
