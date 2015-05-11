## bokehTimer
Using bokeh to produce a countdown timer

_timer.py_ uses bokeh-server to create an HTML timer that counts down from a user-defined time to zero. The script takes a single argument on the command line - the amount of time (in minutes and/or seconds) that the timer counts down from. For example, to set the timer for ten minutes, you can provide this time limit in either of the following ways:

`python timer.py 600`  
`python timer.py 10:00`

There are plans to add a reset button, and a sound notification when the timer depletes, if I can figure out how to do either of these/if they're even possible!
