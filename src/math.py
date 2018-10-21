'''Import statements: DO NOT TOUCH'''
import scipy
import matplotlib
import pyglet
import pandas as pd
import plotly

'''This is the master function that will be called at the end of the project.'''
def create_line(file_path):
    return 0

# Returns True if a line of slop m through point (x,y) goes
# through the plot defined by plot_points.
# Horizontal Lines: m = 0
# Vertical Lines: m = None
def line_goes_through_plot(plot_points, x, y, m):
    left_barrier = min(plot_points, key=lambda k: k[0])
    right_barrier = max(plot_points, key=lambda k: k[0])
    bottom_barrier = min(plot_points, key=lambda k: k[1])
    top_barrier = max(plot_points, key=lambda k: k[1])

    if m == None:
        return bottom_barrier <= y <= top_barrier
    elif m == 0:
        return left_barrier <= x <= right_barrier
    elif intersects_points(plot_points, x, y, m):
        return True

    line_left_y = calc_y(y, m, x, left_barrier)
    line_right_y = calc_y(y, m, x, right_barrier)
    line_top_x = calc_x(x, m, y, top_barrier)
    line_bottom_x = calc_x(x, m, y, bottom_barrier)

    if line_left_y >= bottom_barrier and line_right_y <= top_barrier:
        return True
    elif line_left_y <= bottom_barrier and line_right_y >= top_barrier:
        return True
    elif line_bottom_x >= left_barrier and line_top_x <= right_barrier:
        return True
    elif line_bottom_x <= left_barrier and line_top_x >= right_barrier:
        return True

    return False


# Returns True if a line of slope m through point (x,y) goes
# through points.
def intersects_points(points, x, y, m):
    for point in points:
        point_x = point[0]
        point_y = point[1]

        if y - point_y == m * (x - point_x):
            return True

    return False


# Calculates y at x1 based on a line of slope m through (x,y)
def calc_y(y, m, x, x1):
    return y - m * (x - x1)


# Calculates x at y1 based on a line of slope m through (x,y)
def calc_x(x, m, y, y1):
    return x - (1 / m) * (y - y1)

# Returns list of indecies of all troughs in vals
def locate_lowest_trough(vals):
    if len(vals) == 1:
        return [0]

    troughs = []
    if vals[0] < vals[1]:
        troughs += 0

    for i in range(len(vals)):
        if i != 0 and i < len(vals) - 1:
            if vals[i-1] < vals[i] < vals[i+1]:
                troughs += i

    if vals[len(vals) - 1] < vals[len(vals) - 2]:
        troughs += len(vals) - 1

    return troughs

''' Accepts a list of coordinates and returns the boundary of the city '''
def calc_city_coords(coords):
    city_coords = []
    left_barrier = min(coords, key=lambda k: k[0])
    right_barrier = max(coords, key=lambda k: k[0])
    bottom_barrier = min(coords, key=lambda k: k[1])
    top_barrier = max(coords, key=lambda k: k[1])

    city_coords += (left_barrier, top_barrier)
    city_coords += (right_barrier, top_barrier)
    city_coords += (right_barrier, bottom_barrier)
    city_coords += (left_barrier, bottom_barrier)

    return city_coords

#TODO: Implement calc_plot_corners which takes a plot's center coordinate (x,y)
#TODO: and the frontage of the plot, and returns a list of the 4 corners of the recctangular plot
def calc_plot_corners(center_coord, frontage):
    return 0

#TODO: Implement calc_city_center which takes the data parsed in parsing and
#TODO: determines the center of the city, be it geographic or financial
#TODO: this is up for discussion among the math team
#TODO: this should return a set of coordinates (x,y)
def calc_city_center(city_data):
    return 0

'''The main method of the file. Use this for running'''
def math_main():
    return 0

'''All code below this line will be run when you run the file'''
math_main()