'''Import statements: DO NOT TOUCH'''
import scipy
import matplotlib
import pyglet
import pandas as pd
import plotly
import math

''' This is the master function that will be called at the end of the project.'''
def create_line(file_path):
    return 0

''' Returns True if a line of slop m through point (x,y) goes
    through the plot defined by plot_points.
    Horizontal Lines: m = 0
    Vertical Lines: m = None '''
def line_goes_through_plot_rectangle(plot_points, x, y, m):
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

''' Due to lack of positioning available, plots may have to be circles
    Code from https://www.geeksforgeeks.org/check-line-touches-intersects-circle/ '''
def line_goes_through_plot_circle(line_x, line_y, line_m, circ_x, circ_y, radius):
    if line_m == None:
        return (circ_x - radius) <= line_x <= (circ_x + radius)
    if line_m == 0:
        return (circ_y - radius) <= line_y <= (circ_y + radius)

    line_a = line_m
    line_b = -1
    line_c = -1 * (line_m * line_x) + line_y

    dist = ((abs(line_a * circ_x + line_b * circ_y + line_c)) /
            math.sqrt(line_a ** 2 + line_b ** 2))

    return dist <= radius

''' Returns True if a line of slope m through point (x,y) goes
    through points. '''
def intersects_points(points, x, y, m):
    for point in points:
        point_x = point[0]
        point_y = point[1]

        if y - point_y == m * (x - point_x):
            return True

    return False


''' Calculates y at x1 based on a line of slope m through (x,y)'''
def calc_y(y, m, x, x1):
    return y - m * (x - x1)


''' Calculates x at y1 based on a line of slope m through (x,y)'''
def calc_x(x, m, y, y1):
    return x - (1 / m) * (y - y1)

''' Returns list of indecies of all troughs in vals'''
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

''' Returns radius of circle based on the frontage of the lot and area
    Min() is used to reduce number of collisions between lots in circular form '''
def calc_radius(frontage, area):
    return min(frontage / 2, math.sqrt(area / math.pi))

''' Accepts coordinates of the city center and a point. Returns the distance between these points'''
def calc_distance_from_center(city_x_coord, city_y_coord, point_x_coord, point_y_coord):
    dif_x = abs(point_x_coord-city_x_coord)
    dif_y = abs(point_y_coord-point_y_coord)
    dif_x *= dif_x
    dif_y *= dif_y
    total = dif_x + dif_y
    return total ** .5

''' Accepts x coordinates of the city center and a point. Returns the difference in x. (pos/neg follows
 normal cartesian plane)'''
def get_relative_x(city_x_coords, point_x_coords):
    return point_x_coords - city_x_coords

''' Accepts y coordinates of the city center and a point. Returns the difference in y. (pos/neg follows
 normal cartesian plane)'''
def get_relative_y(city_y_coords, point_y_coords):
    return point_y_coords - city_y_coords

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