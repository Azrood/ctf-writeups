import enchant
from pwn import *

d = enchant.Dict("en_US")

conn = remote('jh2i.com', 50012)
context.log_level = 'INFO'
while True:
    question = conn.recvuntil("\n").decode()
    log.info(question)
    words = conn.recvline().decode().strip()
    log.info(words)
    if "NOT real" in question :
        answers = [ word for word in words.split() if not d.check(word)]
        answr = ' '.join(answers)
        if "CHRONOLOGICAL ORDER" in question:
            conn.sendline(answr)
            log.info(f"sending {answr}")

        elif "ALPHABETICAL" in question:
            answers.sort()
            answr = ' '.join(answers)
            log.info(f"Sending {answr}")
            conn.sendline(answr)
        else:
            log.info(f"Sending {len(answers)}")
            conn.sendline(str(len(answers)))
    elif "ARE real":
        answers = [ word for word in words.split() if d.check(word)]
        answr = ' '.join(answers)
        if "CHRONOLOGICAL ORDER" in question:
            conn.sendline(answr)
            log.info(f"sending {answr}")

        elif "ALPHABETICAL" in question:
            answers.sort()
            answr = ' '.join(answers)
            log.info(f"Sending {answr}")
            conn.sendline(answr)
        else:
            log.info(f"Sending {len(answers)}")
            conn.sendline(str(len(answers)))


    resp = conn.recvline().decode().strip()
    log.info(resp)
    if "flag" in resp:
        log.success(f"FOUND FLAG : {resp}")




