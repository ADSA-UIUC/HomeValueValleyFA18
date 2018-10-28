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
def parse_file(file_path, raw_columns, processed_columns):
    raw_sf_data = pd.read_csv(filepath_or_buffer=file_path, usecols=raw_columns, low_memory=True, index_col=False)
    sunset_regex = re.compile(".*Sunset.*")
    neighborhood = raw_sf_data["Analysis Neighborhood"]
    use_regex = re.compile(".*Residential.*")
    use = raw_sf_data["Use Definition"]

    # The na=false flag will skip over any entry that is none
    raw_sf_data = raw_sf_data[neighborhood.str.match(sunset_regex, na=False)]
    raw_sf_data = raw_sf_data[use.str.match(use_regex, na=False)]

    #TODO: Return a processed form of the data
    return raw_sf_data

def write_file(file_path, processed_info):
    processed_info.to_csv(file_path, index=False)


'''Think of this as your main() method when running the file'''
def parsing_main():

    # Make sure CSV file is in the correct file_path
    # NOTE IF MAC CHANGE '\' TO '/' (MAC = '/') (OTHER = '/')
    file_path = "..\data\processeddata\San_Francisco_Assessments.csv"

    raw_data_columns = ["Use Code", "Number of Units", "Assessed Improvement Value",
                       "Analysis Neighborhood", "the_geom", "Use Definition"]

    processed_data_columns = ["Lot Number", "Center", "Radius", "Total Assessed Value",
                         "Assessed Value Per Unit", "On Line", "Line Number"]

    parsed_data = parse_file(file_path, raw_data_columns, processed_data_columns)

    write_file(file_path, parsed_data)
    print(parsed_data)

'''The code that's actually run'''
parsing_main()
