'''Import statements: DO NOT TOUCH'''
import scipy
import matplotlib
import pyglet
import pandas as pd
import plotly
import plotly.plotly as py
import plotly.graph_objs as go

''' This is the master function that will be called at the end of the project. '''
def visualize(city_name):
    # Retrieving the information of the city itself for Layout()
    city_info_fp = "../data/processeddata/City_Info.csv"
    city_info = pd.read_csv(city_info_fp)

    #city_info.set_index("Name")

    print(city_info)

    city_lat = city_info.iloc[0]["Center-Lat"]
    city_long = city_info.iloc[0]["Center-Long"]

    # This grabs the property data for the city
    data_filepath = "../data/processeddata/" + city_info.iloc[0]["Filename"]
    city_housing_data = pd.read_csv(data_filepath, low_memory=False)

    data = [
        go.Scattermapbox(
            lat=city_housing_data["Center-Lat"],
            lon=city_housing_data["Center-Long"],
            mode="markers",
            marker=dict(
                size=10
            ),
        )
    ]

    layout = go.Layout(
        autosize=True,
        hovermode="closest",
        mapbox=dict(
            bearing=0,
            center=dict(
                lat=city_lat,
                lon=city_long
            ),
            pitch=0,
            zoom=10
        ),
    )

    fig = dict(data=data, layout=layout)

    py.iplot(fig, filename="San_Francisco_Visualization")


''' The main file for this file. '''
def visualize_main():
    visualize("San Francisco")

''' All code below this comment will be run when file is run '''
visualize_main()