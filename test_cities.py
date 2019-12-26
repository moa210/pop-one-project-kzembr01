import pytest
import math
from cities import *

# ### Required tests (file `test_cities.py`)


# In this assignment `main`, `read_cities`, `print_cities`, and
# `print_map` result in input or output, so you do not need to
# write unit tests for these. Also, you do not need to test `find_best_cycle`
# because of random results.
# Provide unit tests for all the  other functions, as well as any additional
# computational functions you might write.
# ****************************

def test_compute_total_distance():
    road_map1 = [("Kentucky", "Frankfort", 38.197274, -84.86311),\
                ("Delaware", "Dover", 39.161921, -75.526755),\
                ("Minnesota", "Saint Paul", 44.95, -93.094)]

    assert compute_total_distance(road_map1)==\
           pytest.approx(9.386+18.496+10.646, 0.01)

# ****************************

def test_swap_cities():
    road_map = [("Kentucky", "Frankfort", 38.197274, -84.86311),\
                ("Delaware", "Dover", 39.161921, -75.526755),\
                ("Minnesota", "Saint Paul", 44.95, -93.094)]

    new_road_map = [("Delaware", "Dover", 39.161921, -75.526755),\
                    ("Kentucky", "Frankfort", 38.197274, -84.86311),\
                    ("Minnesota", "Saint Paul", 44.95, -93.094)]

    x1,y1 = new_road_map[0][2], new_road_map[0][3]
    x2,y2 = new_road_map[1][2], new_road_map[1][3]
    x3,y3 = new_road_map[2][2], new_road_map[2][3]

    distance = (math.sqrt((x1-x2)**2 + (y1-y2)**2)) + (math.sqrt((x2-x3)**2 + (y2-y3)**2)) + (math.sqrt((x3-x1)**2 + (y3-y1)**2))

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

# ****************************

def test_shift_cities():
    '''add your tests'''
    road_map3 = [("Kentucky", "Frankfort", 38.197274, -84.86311),\
                ("Delaware", "Dover", 39.161921, -75.526755),\
                ("Minnesota", "Saint Paul", 44.95, -93.094)]

    new_road_map3 = [("Minnesota", "Saint Paul", 44.95, -93.094),\
                    ("Kentucky", "Frankfort", 38.197274, -84.86311),\
                    ("Delaware", "Dover", 39.161921, -75.526755)]

    assert shift_cities(road_map3) == new_road_map3, "********** Shifting did not take place **********"

# ****************************

def test_read_cities():

  road_map4 = [("Alabama", "Montgomery", 32.361538, -86.279118),\
              ("Alaska", "Juneau", 58.301935, -134.41974),\
              ("Arizona", "Phoenix", 33.448457, -112.073844 )]

  inputfilepath="test-city-data.txt"

  assert read_cities(inputfilepath) == road_map4, "********** Road map reading did not take place **********"

# ****************************

# def test_print_cities():

#   road_map5 = [("Alabama", "Montgomery", 32.361538, -86.279118),\
#               ("Alaska", "Juneau", 58.301935, -134.41974),\
#               ("Arizona", "Phoenix", 33.448457, -112.073844 )]

#   road_map5_printed = "Alabama, Montgomery, 32.36, -86.28\nAlaska, Juneau, 58.3, -134.42\nArizona, Phoenix, 33.45, -112.07\n"

#   assert print_cities(road_map5) == road_map5_printed, "********** Road map printing did not take place **********"
