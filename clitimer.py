# -*- coding: utf-8 -*-
"""
Created on Fri Jul 29 16:31:08 2016

@author: hodges
"""

from sys import argv, stdout
from time import sleep

# Functions
def display_time(rtime):
    remaining_mins = int(rtime/60)
    remaining_secs = int(rtime%60)
    stdout.write('\u001b[5D%02d:%02d' % (remaining_mins, remaining_secs))
    stdout.flush()

def countdown(rtime):
    while rtime > 0:
        sleep(1)
        rtime -= 1
        display_time(rtime)

def run_timer(stime):
    display_time(stime)
    countdown(stime)
    stdout.write('\u001b[5D00:00\a\n')

if __name__ == "__main__":
# Get input time, or prompt user for input if argument not provided
    try:
        input_time = argv[1]
    except IndexError:
        input_time = input(
        'Please provide a length of time to countdown (seconds or mm:ss):  ')
# Process input time
    if ':' in input_time:
        minutes, seconds = input_time.split(':')
        minutes = int(minutes)
        seconds = int(seconds)
        start_time = minutes*60 + seconds
    else:
        start_time = int(input_time)
    
# run countdown
    run_timer(start_time)
        