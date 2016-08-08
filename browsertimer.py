#! /usr/bin/env python
'''
A script to create a simple, browser-based countdown timer.

usage: bokeh serve --show timer.py
'''
# Imports
from bokeh.layouts import column, row
from bokeh import plotting as bkplt
from bokeh.models import ColumnDataSource, Button, Slider
from bokeh.driving import count

# Functions
@count()
def countdown(step):
    '''Count down the time remaining'''
    global seconds_left
    global text_color
    if seconds_left > 0:
        seconds_left -= 1
        update_timer(seconds_left, start_time)
    # make the timer text flash if time has run out
    if seconds_left == 0:
        if 'ff0000' in text_color:
            text_color = ['%ffffff']
            source.data['text_color'] = text_color
            source.trigger('data', source.data, source.data)
        else:
            text_color = ['ff0000']
            source.data['text_color'] = text_color
            source.trigger('data', source.data, source.data)

def update_timer(seconds_remaining, start_time):
    '''Update the appearance of the timer'''
    global seconds_left
    seconds_left = seconds_remaining
    minutes_remaining = int(seconds_remaining/60)
    remainder = seconds_remaining%60
    time_string = ['%02d:%02d' % (minutes_remaining, remainder)]
    source.data['time_remaining'] = [time_string]
# change background colour if remaining time <10% of initial value
    if seconds_remaining <= start_time/10:
        fill_color = 'ff0000'
    else:
        fill_color = '78c400'
    source.data['text_color'] = ['%ffffff']
    source.data['fill_color'] = [fill_color]
    source.trigger('data', source.data, source.data)
    return True

def run_timer():
    '''(Re)Set the timer running;
    disable start button and sliders;
    enable stop button'''
    start_button.disabled = True
    stop_button.disabled = False
    minutes_slider.disabled = True
    minutes_slider.disabled = True
    # set timer running, by calling countdown() every 1000 millisecs
    bkplt.curdoc().add_periodic_callback(countdown, 1000)
    return True

def reset_timer():
    '''Reset the timer to the specified start time'''
    global seconds_left
    # check if the timer is running, and stop it if it is
    if start_button.disabled == True:
        start_button.disabled = False
        stop_button.disabled = True
        minutes_slider.disabled = False
        minutes_slider.disabled = False
        # stop calling countdown()
        bkplt.curdoc().remove_periodic_callback(countdown)
    update_timer(start_time, start_time)
    seconds_left = start_time

def stop_timer():
    '''Stop the timer'''
    stop_button.disabled = True
    start_button.disabled = False
    minutes_slider.disabled = False
    minutes_slider.disabled = False
    # stop calling countdown()
    bkplt.curdoc().remove_periodic_callback(countdown)
    
def set_start_time(attrname, old, new):
    '''Set the start time of the timer'''
    global start_time
    start_mins = minutes_slider.value
    start_secs = seconds_slider.value
    start_time = start_mins*60 + start_secs
    # only update timer text if the timer isn't running
    if not minutes_slider.disabled:
        update_timer(start_time, start_time)

# Set default/starting values
default_minutes = 5
default_seconds = 0
seconds_left = default_minutes*60 + default_seconds
# ColumnDataSource data values must be iterable, 
# so the values below are placed inside single-element lists
color = ['78c400']
text_color = ['%ffffff']
start_time = [default_minutes*60 + default_seconds]
time_remaining = ['%02d:%02d' % (default_minutes, default_seconds)]

# Create data source for timer plot
source=ColumnDataSource(data=dict(start_time=start_time,
                                  time_remaining=time_remaining,
                                  fill_color=color,
                                  text_color=text_color))

# No tools required for this one
tools = ''

# Create plot: a color block, with text centered inside
p1 = bkplt.figure(x_range=(-8, 8), y_range=(-5, 5), 
                  plot_width=900, plot_height=600, 
                  title=None, tools=tools)
p1.rect(x=[0], 
        y=[0], 
        width=16, 
        height=10, 
        fill_color='fill_color', 
        line_color=None, 
        name='block',
        source=source)
p1.text(x=[0], 
        y=[0], 
        text='time_remaining', 
        text_color='text_color', 
        alpha=0.75, 
        text_font_size='128pt', 
        text_baseline='middle', 
        text_align='center', 
        name='timer',
        source=source)

# Remove axes, labels & tick lines
p1.ygrid.grid_line_color = None
p1.xgrid.grid_line_color = None
p1.axis.axis_line_color  = None
p1.axis.major_label_text_color = None
p1.axis.major_tick_line_color = None
p1.axis.minor_tick_line_color = None

# Sliders
minutes_slider = Slider(start=0, end=99, 
                        value=default_minutes, step=1, 
                        title="Minutes")
minutes_slider.on_change("value", set_start_time)
seconds_slider = Slider(start=0, end=59, 
                        value=default_seconds, step=1, 
                        title="Seconds")
seconds_slider.on_change("value", set_start_time)

# Buttons
start_button = Button(label="Start")
start_button.on_click(run_timer)
stop_button = Button(label="Stop")
stop_button.on_click(stop_timer)
reset_button = Button(label="Reset")
reset_button.on_click(reset_timer)

# Layout plot & widgets
bkplt.curdoc().add_root(column(row(minutes_slider, seconds_slider), 
                               row(start_button, stop_button, reset_button), 
                               p1))
