
import Threading as th
import time
from subprocess import Popen, PIPE

p = Popen(["bc", "-i"], stdout=PIPE, stderr=PIPE, stdin=PIPE)

while p.poll() is None:
    print(p.stdout.readline().decode())

def read_Target(p):
    while p.poll() is None:
        print(p.stdout.readline())

t=th.Thread(target=read_Target, args=(p,))
t.start()

while p.poll() is None:
    quary = str(input())
    if quary == 'quit':
            print(quary)
            p.communicate(quary,timeout=1)

    if p.poll() is not None:
        break

p.stdin.write(quary.encode().strip())
p.stdin.flush()
