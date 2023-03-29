import os

with file('bla.txt') as input:
  for count, line in enumerate(input):
    if count > 10000:
      break
    if re.search('foo bar', line):
      print (line)
