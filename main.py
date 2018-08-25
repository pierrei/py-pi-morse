from morse import Morse

def callback(char):
  print char

PIN = 3
Morse(PIN, callback).read_input()
