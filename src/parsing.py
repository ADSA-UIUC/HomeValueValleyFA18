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
    sf_data = pd.read_csv(filepath_or_buffer=file_path, usecols=desired_columns, low_memory=True)
    sunset_regex = re.compile(".*Sunset.*")
    neighborhood = sf_data["Analysis Neighborhood"]
    use_regex = re.compile(".*Residential.*")
    use = sf_data["Use Definition"]

    # The na=false flag will skip over any entry that is none
    sf_data = sf_data[neighborhood.str.match(sunset_regex, na=False)]
    sf_data = sf_data[use.str.match(use_regex, na=False)]
    return sf_data

'''Think of this as your main() method when running the file'''
def parsing_main():

    # Make sure CSV file is in the correct file_path
    # NOTE IF MAC CHANGE '\' TO '/' (MAC = '/') (OTHER = '/')
    file_path = "..\OriginalCSV\Assessor_Historical_Secured_Property_Tax_Rolls.csv"

    desired_columns = ["Use Code", "Number of Units", "Assessed Improvement Value",
                       "Analysis Neighborhood", "the_geom", "Use Definition"]
    original_value_filtered = parse_file(file_path, desired_columns)
    intermediate_columns = ["Use Code", "Number of Units", "Assessed Improvement Value",
                      "the_geom"]

    #TODO: Implement the line below in math.py
    # output_columns = calculate(original_value_filtered, intermediate_columns)
    # print(output_columns)

    print(original_value_filtered)

'''The code that's actually run'''
parsing_main()
