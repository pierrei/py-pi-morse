from time import sleep

from morse import Morse
from diode import Diode


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
DIODE_PRESS_PIN = 15
DIODE_MATCH_PIN = 17

press_diode = Diode(DIODE_PRESS_PIN)
match_diode = Diode(DIODE_MATCH_PIN)
string_matcher = StringMatcher("CODE", match_diode.turn_on)

morse = Morse(READ_PIN, string_matcher.new_char, press_diode.turn_on, press_diode.turn_off)
while True:
    morse.read_input()
    sleep(0.01)
