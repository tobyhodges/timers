#! /usr/bin/env python
'''
A script to create a simple, browser-based countdown timer.

usage: python browsertimer.py
'''
# Imports
from bokeh.layouts import column, row
from bokeh import plotting as bkplt
from bokeh.models import ColumnDataSource, Button, Slider, CustomJS

# Set default/starting values
default_minutes = 5
default_seconds = 0
seconds_left = default_minutes*60 + default_seconds
# ColumnDataSource data values must be iterable, 
# so the values below are placed inside single-element lists
color = ['#78c400']
text_color = ['#ffffff']
start_time = [default_minutes*60 + default_seconds]
time_remaining = list(start_time)
time_string = ['%02d:%02d' % (default_minutes, default_seconds)]
# Create data source for timer plot
source=ColumnDataSource(data=dict(x=[0],
                                  y=[0],
                                  start_time=start_time,
                                  start_mins=[default_minutes],
                                  start_secs=[default_seconds],
                                  time_remaining=time_remaining,
                                  time_string=time_string,
                                  fill_color=color,
                                  text_color=text_color,
                                  interval_id=[0]))

# No tools required for this one
tools = ''

# JS Callbacks
run_timer_JS = CustomJS(args=dict(source=source), code="""
    function disable_button(button) {
        button_id = button.get('id');
        button_element = document.querySelector('#modelid_' + button_id + '>button');
        button_element.setAttribute('disabled',true);
    }
    function enable_button(button) {
        button_id = button.get('id');
        button_element = document.querySelector('#modelid_' + button_id + '>button');
        button_element.removeAttribute('disabled');
    }
    var data = source.get('data');
    interval_id = data['interval_id'];
    function countdown() {
        start_time = data['start_time'];
        time_remaining = data['time_remaining'];
        time_string = data['time_string'];
        text_color = data['text_color'];
        fill_color = data['fill_color'];
        if (time_remaining[0] == 0) {
            if (text_color[0] == '#ffffff') {
                text_color[0] = '#ff0000';
            }else {
                text_color[0] = '#ffffff';
            }
        }else{
            time_remaining[0]--;
            time_string[0] = ('0' + Math.floor(time_remaining[0] / 60)).slice(-2) + ':' + ('0' + Math.floor(time_remaining[0] % 60)).slice(-2);
            if (time_remaining[0] <= start_time[0]/10) {
                fill_color[0] = '#ff0000';
            }
        }
        source.trigger('change');
    }
    disable_button(start_button);
    enable_button(stop_button);
    enable_button(reset_button);
    if (interval_id[0] == 0) {
        interval_id[0] = setInterval(countdown, 1000);
        source.trigger('change');
    }
""")

stop_timer_JS = CustomJS(args=dict(source=source), code="""
    function disable_button(button) {
        button_id = button.get('id');
        button_element = document.querySelector('#modelid_' + button_id + '>button');
        button_element.setAttribute('disabled',true);
    }
    function enable_button(button) {
        button_id = button.get('id');
        button_element = document.querySelector('#modelid_' + button_id + '>button');
        button_element.removeAttribute('disabled');
    }
    var data = source.get('data');
    interval_id = data['interval_id'];
    if (interval_id[0] != 0){
        clearInterval(interval_id[0]);
        interval_id[0] = 0;
    }
    enable_button(start_button);
    disable_button(stop_button);
    enable_button(reset_button);
    source.trigger('change');
""")

reset_timer_JS = CustomJS(args=dict(source=source), code="""
    function disable_button(button) {
        button_id = button.get('id');
        button_element = document.querySelector('#modelid_' + button_id + '>button');
        button_element.setAttribute('disabled',true);
    }
    function enable_button(button) {
        button_id = button.get('id');
        button_element = document.querySelector('#modelid_' + button_id + '>button');
        button_element.removeAttribute('disabled');
    }
    var data = source.get('data');
    interval_id = data['interval_id'];
    start_time = data['start_time'];
    time_remaining = data['time_remaining'];
    time_string = data['time_string'];
    text_color = data['text_color'];
    fill_color = data['fill_color'];
    text_color[0] = '#ffffff';
    fill_color[0] = '#78c400';
    if (interval_id[0] != 0) {
        clearInterval(interval_id[0]);
        interval_id[0] = 0;
    }
    time_remaining[0] = start_time[0];
    time_string[0] = ('0' + Math.floor(time_remaining[0] / 60)).slice(-2) + ':' + ('0' + Math.floor(time_remaining[0] % 60)).slice(-2);
    enable_button(start_button);
    disable_button(stop_button);
    source.trigger('change');
""")

set_start_time_JS = CustomJS(args=dict(source=source), code="""
    var data = source.get('data');
    var input_mins = mins_slider.get('value');
    var input_secs = secs_slider.get('value');
    time_string = data['time_string'];
    time_remaining = data['time_remaining'];
    start_button_id = start_button.get('id');
    start_button_element = document.querySelector('#modelid_' + start_button_id + '>button');
    start_time = data['start_time'];
    start_time[0] = (input_mins * 60) + (input_secs);
    if (start_button_element.hasAttribute('disabled')) {
    } else {
        time_remaining[0] = start_time[0];
        time_string[0] = ('0' + Math.floor(time_remaining[0] / 60)).slice(-2) + ':' + ('0' + Math.floor(time_remaining[0] % 60)).slice(-2);
    }
    source.trigger('change');
""")

# Create plot: a color block, with text centered inside
p1 = bkplt.figure(x_range=(-8, 8), y_range=(-5, 5), 
                  plot_width=900, plot_height=600, 
                  title=None, tools=tools)
p1.rect(x='x', y='y', 
        width=16, height=10, 
        fill_color='fill_color', 
        line_color=None, 
        name='block',
        source=source)
p1.text(x='x', y='y', 
        text='time_string', 
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
                        title="Minutes", 
                        callback=set_start_time_JS)
seconds_slider = Slider(start=0, end=59, 
                        value=default_seconds, step=1, 
                        title="Seconds", 
                        callback=set_start_time_JS)
set_start_time_JS.args['mins_slider'] = minutes_slider
set_start_time_JS.args['secs_slider'] = seconds_slider

# Buttons
start_button = Button(label="Start", callback=run_timer_JS)
run_timer_JS.args['start_button'] = stop_timer_JS.args['start_button'] = reset_timer_JS.args['start_button'] = set_start_time_JS.args['start_button'] = start_button
stop_button = Button(label="Stop", disabled=True, callback=stop_timer_JS)
run_timer_JS.args['stop_button'] = stop_timer_JS.args['stop_button'] = reset_timer_JS.args['stop_button'] = stop_button
reset_button = Button(label="Reset", callback=reset_timer_JS)
run_timer_JS.args['reset_button'] = stop_timer_JS.args['reset_button'] = reset_timer_JS.args['reset_button'] = reset_button

# Layout plot & widgets
layout = column(row(minutes_slider, seconds_slider), 
                row(start_button, stop_button, reset_button), 
                p1)

# Show figure
bkplt.output_file('browsertimer.html', title="Countdown Timer")
bkplt.show(layout)
