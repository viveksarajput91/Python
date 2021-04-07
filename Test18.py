""""
This is testing application for exception check
"""

from time import *
from threading import *
class Greeting1(Thread):
    def run(self):
        for i in range(5):
            print("Hello")
            sleep(2)

class Greeting2(Thread):
    def run(self):
        for i in range(5):
            print("Hi")
            sleep(2)


G1=Greeting1()
G2=Greeting2()
G1.start()
G2.start()
G1.join()
G2.join()
print("bye")
