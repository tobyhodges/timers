# -*- coding: utf-8 -*-
"""
Created on Fri Jul 29 16:31:08 2016

@author: hodges
"""

from sys import argv, stdout
from time import sleep

try:
    input_time = argv[1]
except IndexError:
    input_time = input('Please provide a length of time to countdown (seconds or mm:ss):  ')

if ':' in input_time:
    minutes, seconds = input_time.split(':')
    minutes = int(minutes)
    seconds = int(seconds)
    start_time = remaining_time = minutes*60 + seconds
else:
    start_time = remaining_time = int(input_time)

remaining_mins = int(remaining_time/60)
remaining_secs = int(remaining_time%60)
stdout.write('%02d:%02d' % (remaining_mins, remaining_secs))
while remaining_time > 0:
    sleep(1)
    remaining_time -= 1
    remaining_mins = int(remaining_time/60)
    remaining_secs = int(remaining_time%60)
    stdout.write('\u001b[5D%02d:%02d' % (remaining_mins, remaining_secs))
    stdout.flush()

stdout.write('\u001b[5D00:00\a\n')
    