import sys
from time import sleep

from RPi import GPIO

from diode import Diode
from morse import Morse


class StringMatcher(object):
    string = ''

    def __init__(self, string_to_match, matching_callback):
        self.string_to_match = string_to_match
        self.matching_callback = matching_callback
        self.max_length = len(string_to_match)

    def new_char(self, char):
        self.string += char
        if len(self.string) > self.max_length:
            self.string = self.string[-self.max_length:]

        if self.string_to_match == self.string:
            self.matching_callback()


READ_PIN = 3
DIODE_PRESS_PIN = 17
DIODE_MATCH_PIN = 15

press_diode = Diode(DIODE_PRESS_PIN)
match_diode = Diode(DIODE_MATCH_PIN)


def match():
    print('\nMatch!')
    match_diode.turn_on()


string_matcher = StringMatcher("CODE", match)


def new_char(char):
    sys.stdout.write(char)
    sys.stdout.flush()
    string_matcher.new_char(char)


morse = Morse(READ_PIN, cpm=30, auto_speed=True, text_callback=new_char,
              pressed_callback=press_diode.turn_on, released_callback=press_diode.turn_off)

try:
    print('Started! Listening for input..')
    while True:
        morse.read_input()
        sleep(0.01)
except KeyboardInterrupt:
    print('\nShutting down..')
finally:
    GPIO.cleanup()
