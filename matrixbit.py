#Create a continuous 'rainfall' pattern on the micro:bit LED display

from microbit import *
import random

#set all LED display lines to blank
line1 = "00000"
line2 = "00000"
line3 = "00000"
line4 = "00000"
line5 = "00000"

while True
#ie always

  #collate five lines into image
  matrix = Image(line1 + ":" + line2 + ":" + line3 + ":" + line4 + ":" + line5)
  
  #show image
  display.show(matrix)
  
  #pause for an instant
  sleep(100)
  
  #then shunt everything down a line...
  line5 = line4
  line4 = line3
  line3 = line2
  line2 = line1
  
  #...and introduce a funky new line at the top
  line1 = str(random.randint(1,9) + random.randint(1,9) + random.randint(1,9) + random.randint(1,9) + random.randint(1,9))
