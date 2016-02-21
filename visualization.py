"""Bokeh graph to display advanced statistics comparisions of players"""
from collections import OrderedDict
from math import log, sqrt 

import numpy as np
import pandas 
from six.moves import cStringIO as StringIO

from bokeh.plotting import figure, show, output_file

# advanced player data
adv_player_data = """
Player, True Shooting Percentage, Effective FG Percentage,Turnover Percent, Assist to Turnover Ratio, Free Throw Rate, 3 Pointer Rate, 2 Pointer Rate
Stephen Curry, 67.64, 63.25, 13.11, 1.98, 0.28, 0.55, 0.45
James Harden, 59.37, 50.1, 15.98, 1.57, 0.54, 0.42, 0.58
Kevin Durant, 63.69, 57.36, 12.57, 1.45, 0.38, 0.33, 0.67
Demarcus Cousins, 53.68, 47.39, 12.99, 0.85, 0.5, 0.17, 0.83
Lebron James, 57.19, 53.27, 12.27 ,2.15, 0.36, 0.2, 0.8    
"""

stat_color = OrderedDict([
	("True Shooting Percentage", "orange"),
	("Effective FG Percentage", "black"),
	("Turnover Percent", "#c64787"),
	("Assist to Turnover Ratio", "purple"),
	("Free Throw Rate", "yellow"),
	("3 Pointer Rate", "green"),
	("2 Pointer Rate", "red"),
])

player_color = {
	"Stephen Curry" : "#aeaeb8",
	"James Harden" : "#e69584",
	"Kevin Durant" : "indigo",
	"Demarcus Cousins" : "#0d3362",
	"Lebron James" : "#c64737",
}

data = pandas.read_csv(StringIO(adv_player_data),
					skiprows = 1,
					skipinitialspace=True,
					engine="python")


width = 800
height = 800
inner_radius = 120 
outer_radius = 350 - 10

minr = sqrt(log(.001 * 1E4))
maxr = sqrt(log(1000000 * 1E4))
a = (outer_radius - inner_radius) / (minr - maxr)
b = inner_radius - a * maxr 

def rad(mic):
	return a * np.sqrt(np.log(mic * 1E4)) + b 

big_angle = 2.0 * np.pi / (len(data))
small_angle = big_angle / 7

p = figure(plot_width=width, plot_height=height, title="MVP Canidate Comparison",
	x_axis_type=None, y_axis_type=None,
	x_range=(-420, 420), y_range = (-420,420),
	min_border=0, outline_line_color="black",
	background_fill="#f0e1d2", border_fill="#f0e1d2"
)

p.xgrid.grid_line_color= None
p.ygrid.grid_line_color= None 

#annular weges
angles = np.pi/2 - big_angle - data.index.to_series()*big_angle
colors = [player_color[player] for player in data.Player]
p.annular_wedge(
	0, 0, inner_radius, outer_radius, -big_angle+angles, angles, color=colors
)

#small wedges 
p.annular_wedge(0, 0, inner_radius, rad(data["True Shooting Percentage"]),
                -big_angle+angles+5*small_angle, -big_angle+angles+7*small_angle,
                color=stat_color['True Shooting Percentage'])
p.annular_wedge(0, 0, inner_radius, rad(data['Effective FG Percentage']),
                -big_angle+angles+3*small_angle, -big_angle+angles+6*small_angle,
                color=stat_color['Effective FG Percentage'])

p.annular_wedge(0, 0, inner_radius, rad(data['Turnover Percent']),
                -big_angle+angles+1*small_angle, -big_angle+angles+5*small_angle,
                color=stat_color['Turnover Percent'])

p.annular_wedge(0, 0, inner_radius, rad(data['Assist to Turnover Ratio']),
                -big_angle+angles+1*small_angle, -big_angle+angles+4*small_angle,
                color=stat_color['Assist to Turnover Ratio'])

p.annular_wedge(0, 0, inner_radius, rad(data['Free Throw Rate']),
                -big_angle+angles+(2)*small_angle, -big_angle+angles+3*small_angle,
                color=stat_color['Free Throw Rate'])

p.annular_wedge(0, 0, inner_radius, rad(data['3 Pointer Rate']),
                -big_angle+angles+(1)*small_angle, -big_angle+angles+2*small_angle,
                color=stat_color['3 Pointer Rate'])

p.annular_wedge(0, 0, inner_radius, rad(data['2 Pointer Rate']),
                -big_angle+angles+(.10)*small_angle, -big_angle+angles+(1)*small_angle,
                color=stat_color['2 Pointer Rate'])




# circular axes and lables
labels = np.power(10.0, np.arange(-3, 4))
radii = a * np.sqrt(np.log(labels * 1E4)) + b
p.circle(0, 0, radius=radii, fill_color=None, line_color="white")
p.text(0, radii[:-1], [str(r) for r in labels[:-1]],
       text_font_size="8pt", text_align="center", text_baseline="middle")

p.circle([-40, -40, -40, -40, -40], [-370, -390, -410, -430,-450], color=list(player_color.values()), radius=5)
p.text([-30, -30, -30,-30,-30], [-370, -390,-410,-430,-450], text=["Player: " + gr for gr in player_color.keys()],
       text_font_size="7pt", text_align="left", text_baseline="middle")

p.rect([-70, -70, -70,-70,-70,-70,-70], [68,48,28,8,-12,-32,-52], width=30, height=13,
       color=list(stat_color.values()))
p.text([-44, -40, -40,-40,-40,-40,-40], [68,48,28,8,-12,-32,-52], text=list(stat_color),
       text_font_size="9pt", text_align="left", text_baseline="middle")

output_file("MVPGraph.html", title="graph")

show(p)







