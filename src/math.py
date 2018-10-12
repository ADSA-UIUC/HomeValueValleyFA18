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
        if bottom_barrier <= y <= top_barrier:
            return True
    elif m == 0:
        if left_barrier <= x <= right_barrier:
            return True
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