import sys
from time import sleep

from morse import Morse


def callback(char):
    sys.stdout.write(char)
    sys.stdout.flush()


PIN = 3
morse = Morse(PIN, callback)
while True:
    morse.read_input()
    sleep(0.01)
