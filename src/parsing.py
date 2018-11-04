'''Import statements: DO NOT TOUCH'''
import scipy
import matplotlib
import pyglet
import pandas as pd
import plotly
import re
# This lets us use all of math's defined functions
from src.math import *

'''Think of this as your main() method when running the file'''
def parsing_main():
    # Make sure CSV file is in the correct file_path
    # NOTE IF MAC CHANGE '\' TO '/' (MAC = '/') (OTHER = '/')
    processed_file_path = "../data/processeddata/San_Francisco_Assessments.csv"
    raw_file_path = "../data/rawdata/Assessor_Historical_Secured_Property_Tax_Rolls.csv"

    raw_data_columns = ["Use Code", "Number of Units", "Assessed Improvement Value",
                       "Analysis Neighborhood", "the_geom", "Use Definition", "Lot Frontage"]

    # This is a sample for data that we'll write to a file
    # But we're going to overwrite all of them later on
    # The data is all lists because Pandas says so
    # This is the format we're going to use
    # Center is now split into X and Y because Pandas hates tuples
    processed_data_initial = {
        "Lot Number": [1000],
        "Center-Lat": [37.75],
        "Center-Long": [-122.48],
        "Radius": [25],
        "Total Assessed Value": [750000],
        "Assessed Value Per Unit": [600000],
        "On Line": [True],
        "Line Number": [1]
    }

    parsed_data = parse_file(raw_file_path, raw_data_columns, processed_data_initial)

    write_file(processed_file_path, parsed_data)
    print(parsed_data)

'''This is the master function that will be called at the end of the project.'''
def parse_file(file_path, raw_columns, processed_data_init):
    # Create raw dataframe
    # Filter out useless data
    raw_sf_data = pd.read_csv(filepath_or_buffer=file_path, usecols=raw_columns, low_memory=True, index_col=False)
    sunset_regex = re.compile(".*Sunset.*")
    neighborhood = raw_sf_data["Analysis Neighborhood"]
    use_regex = re.compile(".*Residential.*")
    use = raw_sf_data["Use Definition"]

    # The na=false flag will skip over any entry that is none
    raw_sf_data = raw_sf_data[neighborhood.str.match(sunset_regex, na=False)]
    raw_sf_data = raw_sf_data[use.str.match(use_regex, na=False)]

    # Create processed_sf_data with columns from processed_columns
    # Calculate processed_columns (except for lines) with MATH
    # Fill processed_sf_data with data that can be calculated

    # Calculate what points are on what line (and whether or not they ARE on a line)

    sf_data = pd.DataFrame(processed_data_init)

    #TODO: Return a processed form of the data
    return sf_data

def write_file(file_path, processed_info):
    processed_info.to_csv(file_path, index=False)

'''The code that's actually run'''
parsing_main()