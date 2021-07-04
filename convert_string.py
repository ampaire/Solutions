import re

def convert_string(sentence):
  pattern = r'\d+'
  new_sentence = re.sub(pattern, repl="", string=sentence)
  
  return new_sentence

my_string1 = "The Quick Blue Bird1234 Flew Over the Fast River"
my_string2 = "The Quick Blue Bird76521212 Flew Over the Fast River"


convert_string(my_string1)
convert_string(my_string2)
