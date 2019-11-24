import pytest
import math
from cities import *


def test_compute_total_distance():
    road_map1 = [("Kentucky", "Frankfort", 38.197274, -84.86311),\
                ("Delaware", "Dover", 39.161921, -75.526755),\
                ("Minnesota", "Saint Paul", 44.95, -93.094)]

    assert compute_total_distance(road_map1)==\
           pytest.approx(9.386+18.496+10.646, 0.01)

def test_swap_cities():
    road_map = [("Kentucky", "Frankfort", 38.197274, -84.86311),\
                ("Minnesota", "Saint Paul", 44.95, -93.094)]

    new_road_map = [("Minnesota", "Saint Paul", 44.95, -93.094),\
                    ("Kentucky", "Frankfort", 38.197274, -84.86311)]

    distance = math.sqrt((44.95-38.197274)**2 + (93.094 - 84.86311)**2)

    assert swap_cities(road_map, 0, 1) ==\
          (new_road_map, pytest.approx(distance, 0.01)), "Swaping did not take place"
    """
    Take the city at location `index` in the `road_map`, and the
    city at location `index2`, swap their positions in the `road_map`,
    compute the new total distance, and return the tuple

        (new_road_map, new_total_distance)

    Allow for the possibility that `index1=index2`,
    and handle this case correctly.
    """

def test_shift_cities():
    '''add your tests'''
    road_map3 = [("Kentucky", "Frankfort", 38.197274, -84.86311),\
                ("Delaware", "Dover", 39.161921, -75.526755),\
                ("Minnesota", "Saint Paul", 44.95, -93.094)]

    new_road_map3 = [("Minnesota", "Saint Paul", 44.95, -93.094),\
                    ("Kentucky", "Frankfort", 38.197274, -84.86311),\
                    ("Delaware", "Dover", 39.161921, -75.526755)]

    assert shift_cities(road_map3) == new_road_map3, "Shifting did not take place"

def test_read_cities():

  road_map4 = [("Alabama", "Montgomery", 32.361538, -86.279118),\
              ("Alaska", "Juneau", 58.301935, -134.41974),\
              ("Arizona", "Phoenix", 33.448457, -112.073844 )]

  inputfilepath="test_city_data.txt"

  assert read_cities(inputfilepath) == road_map4, "Roaad map reading did not take place"


def test_print_cities():

  road_map5 = [("Alabama", "Montgomery", 32.361538, -86.279118),\
              ("Alaska", "Juneau", 58.301935, -134.41974),\
              ("Arizona", "Phoenix", 33.448457, -112.073844 )]

  road_map5_printed = ("Alabama, Montgomery, 32.36, -86.27"),\
              ("Alaska, Juneau, 58.30, -134.41"),\
              ("Arizona, Phoenix, 33.44, -112.07")

  assert print_cities(road_map5) == road_map5_printed, "Roaad map printing did not take place"
