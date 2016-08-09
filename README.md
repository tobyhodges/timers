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

_browsertimer.py_ uses JavaScript callbacks with `bokeh.plotting` to create an HTML timer that counts down from a user-defined time to zero.

```Bash
python browsertimer.py
```

When the timer launches in the browser, you can use the sliders to adjust the limit on the timer, and the buttons to start, stop/pause, and reset the timer.

#### Requirements
- [bokeh](http://bokeh.pydata.org/en/latest/index.html) 0.12 or above

#### Acknowledgements
- Thanks to my colleagues Grischa Toedt & Holger Dinkel for advice on how to remove `global` statements and dependency on the `bokeh server`.

