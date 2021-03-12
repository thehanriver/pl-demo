import os
import random

print('rando generator')

file = open('rando.txt','w')

for i in range(20):
    line = str(random.randrange(0,900)) + "\n"
    file.write(line)

file.close()

