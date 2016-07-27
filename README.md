# timer.py
## Using bokeh to produce a countdown timer

_timer.py_ uses the bokeh server to create an HTML timer that counts down from a user-defined time to zero. To run the script, call it with the bokeh server e.g. as below:

```Bash
bokeh server --show timer.py
```

When the timer launches in the browser, you can use the sliders to adjust the limit on the timer, and the buttons to start, stop/pause, and reset the timer.

#### Requirements
- [bokeh](http://bokeh.pydata.org/en/latest/index.html) 0.12 or above

#### Issues - Help/Advice Welcome!
- I'm troubled by the inclusion of `global` statements in the code. I think that there must be a way to achieve the same behavious without these statements. If you have advice on how I might do this, please get in touch!
- (Possibly related to the above point.) I suspect that could be a way to achieve the countdown behaviour of the timer entirely on the browser side i.e. by using BokehJS callbacks instead of `bokeh server`. As above, if you have advice on how I might achieve this, your input is very welcome.
