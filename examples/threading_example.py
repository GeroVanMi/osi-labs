import threading
import time


def hello():
    print("Hello \n")
    time.sleep(2)
    print("World")


t = threading.Thread(target=hello)
t.start()

print("Reached end of script.")
