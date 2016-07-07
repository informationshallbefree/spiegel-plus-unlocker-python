# -*- coding: utf-8 -*-
#  Spiegel Plus decoder/unblocker
output = open('output.txt','w', -1, 'utf-8')
input = open('input.txt','r', -1 , 'utf-8')
input_string = input.read()
chars = list(input_string)
output_string = ""
for i in chars:
    if ord(i) == 32:
        output_string += " "
    elif ord(i) == 10:
        output_string += '\n'
    else:
        output_string += chr(ord(i)-1)
output.write(output_string)
output.close()
input.close()