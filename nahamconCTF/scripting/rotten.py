from pwn import *

alphabet = [chr(x) for x in range(ord('a'), ord('z')+1)]

rott = lambda text, num : ''.join(x if x not in alphabet 
                                else alphabet[(ord(x)-ord('a')+num)%26]
                                for x in text)
context.log_level = 'INFO'
conn = remote('jh2i.com',50034)


flag = ['' for _ in range(100)]
while True:
    line = conn.recvline().decode().strip()
    log.info(f"received : {line}")
    for i in range(26):
        answer = rott(line, i).split()
        if 'flag' in answer:
            if answer[-1] == 'filler.':
                conn.sendline(' '.join(answer))
                log.info(f"sent {' '.join(answer)}")
            else:
                index = int(answer[6])
                flag[index] = answer[-1]
                conn.sendline(' '.join(answer))
                log.info(f"sent {' '.join(answer)}")
    log.info(''.join(''.join(flag).split("'")))    
