import sys
from time import sleep

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


def match():
    print "Match!"


string_matcher = StringMatcher("CODE", match)


PIN = 3
morse = Morse(PIN, string_matcher.new_char)
while True:
    morse.read_input()
    sleep(0.01)
