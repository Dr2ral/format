from time import sleep
from threading import Thread

letters = ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j')
def func():
    for i in letters:
        print(i)
        sleep(1)

th = Thread(target=func)
th.start()
for i in range(1, 11):
    print(i)
    sleep(1)
th.join()

