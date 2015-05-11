#! /usr/bin/env python

import time
import sys
from bokeh import plotting as bkplt
from bokeh.models import TapTool

input_time = sys.argv[1]

# get minutes and seconds from input
if ':' in input_time:
	input_minutes, input_seconds = input_time.split(':')
	input_minutes = int(input_minutes)
	input_seconds = int(input_seconds)
else:
	input_minutes = int(input_time) / 60
	input_seconds = int(input_time) % 60
minutes = [input_minutes]
seconds = [input_seconds]

# calculate total seconds remaining
seconds_left = seconds[0] + minutes[0]*60
# set color of timer background - green if >1 minute, red if =<1 minute
if seconds_left > 60:
	color = ['78c400']
else:
	color = ['ff0000']
text_color = ['%ffffff']

# set initial timer text
time_remaining = ['%02d:%02d' % (minutes[0], seconds[0])]
print time_remaining[0]

bkplt.output_server('timer')
tools = 'reset, tap'

p1 = bkplt.figure(x_range=(-8, 8), y_range=(-5, 5), plot_width=800, plot_height=600, title=None, tools=tools)
p1.rect(x=[0], 
		y=[0], 
		width=16, 
		height=10, 
		fill_color=color, 
		line_color=None, 
		name='block')
p1.text(x=[0], 
		y=[0], 
		text=time_remaining, 
		text_color=text_color, 
		alpha=0.75, 
		text_font_size='128pt', 
		text_baseline='middle', 
		text_align='center', 
		name='timer')

taptool = p1.select(dict(type=TapTool))[0]
taptool.names.append('block')
taptool.names.append('timer')

# def reset_block(block_source, input_mins, input_secs):
# 	seconds_left = input_secs + input_mins*60
# 	color = block_source.data['fill_color']
# 	if seconds_left > 60:
# 		color = ['78c400']
# 	else:
# 		color = ['ff0000']
# 	block_source.data['fill_color'] = color
# 
# def reset_timer(timer_source, input_mins, input_secs):
# 	time_remaining = timer_source.data['text']
# 	time_remaining = ['%02d:%02d' % (input_mins, input_secs)]
# 	timer_source.data['text'] = time_remaining

renderer = p1.select('block')
ds = renderer[0].data_source
labeller = p1.select('timer')
txt = labeller[0].data_source

# ds.on_change('selected', reset_block(ds, int(input_minutes), int(input_seconds)))
# txt.on_change('selected', reset_timer(txt, int(input_minutes), int(input_seconds)))

p1.ygrid.grid_line_color = None
p1.xgrid.grid_line_color = None
p1.axis.axis_line_color  = None
p1.axis.major_label_text_color = None
p1.axis.major_tick_line_color = None
p1.axis.minor_tick_line_color = None
bkplt.show(p1)

while seconds_left > 0:
	time.sleep(1)
	time_remaining = txt.data['text']
	seconds_left -= 1
	minutes_left = seconds_left / 60
	remainder = seconds_left % 60
	time_remaining = ['%02d:%02d' % (minutes_left, remainder)]
	txt.data['text'] = time_remaining
	bkplt.cursession().store_objects(txt)
	color = ds.data['fill_color']
	if seconds_left > 60:
		color = ['78c400']
	else:
		color = ['ff0000']
	ds.data['fill_color'] = color
	bkplt.cursession().store_objects(ds)
