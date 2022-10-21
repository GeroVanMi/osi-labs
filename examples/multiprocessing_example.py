import multiprocessing
import time


def hello():
    print("Hello \n")
    time.sleep(1)
    print("World")


p = multiprocessing.Process(target=hello)
p.start()

print("Reached end of file.")
