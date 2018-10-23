'''Import statements: DO NOT TOUCH'''
import scipy
import matplotlib
import pyglet
import pandas as pd
import plotly
import re
# This lets us use all of math's defined functions
from src.math import *

'''This is the master function that will be called at the end of the project.'''
def parse_file(file_path, desired_columns):
    sf_data = pd.read_csv(filepath_or_buffer=file_path, usecols=desired_columns, low_memory=True, index_col=False)
    sunset_regex = re.compile(".*Sunset.*")
    neighborhood = sf_data["Analysis Neighborhood"]
    use_regex = re.compile(".*Residential.*")
    use = sf_data["Use Definition"]

    # The na=false flag will skip over any entry that is none
    sf_data = sf_data[neighborhood.str.match(sunset_regex, na=False)]
    sf_data = sf_data[use.str.match(use_regex, na=False)]
    return sf_data

def write_file(file_path, processed_info):
    processed_info.to_csv(file_path, index=False)


'''Think of this as your main() method when running the file'''
def parsing_main():

    # Make sure CSV file is in the correct file_path
    # NOTE IF MAC CHANGE '\' TO '/' (MAC = '/') (OTHER = '/')
    file_path = "..\data\processeddata\San_Francisco_Assessments.csv"

    desired_columns = ["Use Code", "Number of Units", "Assessed Improvement Value",
                       "Analysis Neighborhood", "the_geom", "Use Definition"]
    original_value_filtered = parse_file(file_path, desired_columns)
    # Why have a copy of the exact information when you can use the original as an arg?
    # intermediate_columns = ["Use Code", "Number of Units", "Assessed Improvement Value", "the_geom"]

    write_file(file_path, original_value_filtered)

    #TODO: Implement the line below in math.py
    # output_columns = calculate(original_value_filtered, intermediate_columns)
    # print(output_columns)

    print(original_value_filtered)

'''The code that's actually run'''
parsing_main()
