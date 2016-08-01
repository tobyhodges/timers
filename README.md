# timers
## A collection of countdown timers, written in Python

### clitimer.py - A command line countdown timer

_clitimer.py_ takes a single argument - the start time to count down from - shows a countdown and rings the system bell when finished. Usage below:

```Bash
python clitimer.py 60
# or
python clitimer.py 1:00
```

#### Requirements
As the script uses the `\a` notation to ring the system bell, this script won't work on the windows command line.

### browsertimer.py - Using bokeh to produce a countdown timer

_browsertimer.py_ uses the bokeh server to create an HTML timer that counts down from a user-defined time to zero. To run the script, call it with the bokeh server e.g. as below:

```Bash
bokeh server --show browsertimer.py
```

When the timer launches in the browser, you can use the sliders to adjust the limit on the timer, and the buttons to start, stop/pause, and reset the timer.

#### Requirements
- [bokeh](http://bokeh.pydata.org/en/latest/index.html) 0.12 or above

#### Issues - Help/Advice Welcome!
- I'm troubled by the inclusion of `global` statements in the code. I think that there must be a way to achieve the same behavious without these statements. If you have advice on how I might do this, please get in touch!
- (Possibly related to the above point.) I suspect that could be a way to achieve the countdown behaviour of the timer entirely on the browser side i.e. by using BokehJS callbacks instead of `bokeh server`. As above, if you have advice on how I might achieve this, your input is very welcome.

