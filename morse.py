# -*- coding: utf-8 -*-

import time

from RPi import GPIO

from decode_tree import DecodeTree


class Morse(object):
    def __init__(self, pin, text_callback):
        self.text_callback = text_callback
        self.pin = pin

        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

        self.tree = DecodeTree()

        self.cpm_update(30)
        self.last_value = False
        self.lines = []
        self.key_down_time = 0
        self.key_up_time = 0
        self.new_word = False
        self.read_input()

    def cpm_update(self, cpm):
        self.cpmValue = cpm
        self.dit_length = 6.0 / self.cpmValue
        self.dit_dash = 2 * self.dit_length
        self.letter_break = 3 * self.dit_length
        self.word_break = 7 * self.dit_length

    # Call this method as long as the key is up
    def decode_is_up(self, key_up_length):
        if key_up_length >= self.letter_break:
            if self.tree.is_char_available():
                char = self.tree.current_char()
                if not char:
                    char = "�"
                self.text_callback(char)
                self.new_word = True
                self.tree.reset()
        if key_up_length >= self.word_break:
            if self.new_word:
                self.text_callback(" ")
                self.new_word = False

    # Call this method if the key is released
    def decode_was_down(self, key_down_length):
        if key_down_length > self.dit_dash:
            self.tree.dash()
        else:
            self.tree.dot()

    def read_input(self):
        value = not GPIO.input(self.pin)
        if value:
            # key is down
            if not self.last_value:
                # key just went down
                self.key_down_time = time.time()

        if not value:
            # key is up
            if self.last_value:
                # key just went up
                self.key_up_time = time.time()
                key_down_length = self.key_up_time - self.key_down_time
                self.decode_was_down(key_down_length)
            key_up_length = time.time() - self.key_up_time
            self.decode_is_up(key_up_length)

        self.last_value = value
