# play.py
from mydecs import my_logger, my_timer

import time

@my_logger
@my_timer
def simple(msg):
    time.sleep(1)
    print('hello {}'.format(msg))


simple("Eshan")

def powSet(items):
    N = len(items)
    # enumerate the 2**N possible combinations
    for i in range(2**N):
        combo = []
        for j in range(N):
            # test bit jth of integer i
            if (i >> j) % 2 == 1:
                combo.append(items[j])
        yield combo


its = [1,2,3]
# it = powSet(its)
# for e in it:
#     print(e)

def powBags(items):
    N = len(items)
    for L in range(2**N):
        for R in range(2**N):
            if (L & R) == 0:
                bagL = []
                bagR = []
                for j in range(N):
                    if (L >> j) % 2 == 1:
                        bagL.append(items[j])
                    if (R >> j) % 2 == 1:
                        bagR.append(items[j])
                yield (bagL, bagR)

# it = powBags(its)
# for e in it:
#     print(e)

