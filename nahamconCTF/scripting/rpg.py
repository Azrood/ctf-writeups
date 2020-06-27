from pwn import *

context.log_level = 'INFO'

conn = remote('jh2i.com', 50031)
log.info(conn.recvuntil('>').decode())
conn.sendline('6')
conn.sendline('1')
while True:
    log.info(conn.recv().decode())
    for i in range(4):
        conn.sendline('6')
        conn.sendline(str(i+1))
        log.info(str(i+1))
        for _ in range(1000 if i != 3 else 3000 ):
            log.info(conn.recvuntil('>').decode())
            conn.sendline(str(5-i))
            log.info(str(5-i))
    conn.interactive()



