import pytest
import math
from cities import *

# ****************************

def test_compute_total_distance():
  road_map1 = [("Kentucky", "Frankfort", 38.197274, -84.86311),\
              ("Delaware", "Dover", 39.161921, -75.526755),\
              ("Minnesota", "Saint Paul", 44.95, -93.094)]

  road_map3 = [("Delaware", "Dover", 0, 0),\
              ("Minnesota", "Saint Paul", 0, 0),\
              ("Alabama", "Montgomery", 0, 0),\
              ("Alaska", "Juneau", 0, 0),\
              ("Arizona", "Phoenix", 0, 0 )]

  assert type(compute_total_distance(road_map1))== float,\
         "*********** Compute total distance return type not correct ************"

  assert compute_total_distance(road_map1)==\
         pytest.approx(9.386+18.496+10.646, 0.01),\
         "*********** Compute total distance 1: did not take place ************"

  assert compute_total_distance(road_map3)==(0),\
         "*********** Compute total distance 2: did not take place ************"

# ****************************


def test_swap_cities():
  road_map = [("Kentucky", "Frankfort", 38.197274, -84.86311),\
              ("Delaware", "Dover", 39.161921, -75.526755),\
              ("Minnesota", "Saint Paul", 44.95, -93.094)]

  new_road_map = [("Delaware", "Dover", 39.161921, -75.526755),\
                  ("Kentucky", "Frankfort", 38.197274, -84.86311),\
                  ("Minnesota", "Saint Paul", 44.95, -93.094)]

  road_map2 = [("Delaware", "Dover", 39.161921, -75.526755),\
              ("Minnesota", "Saint Paul", 44.95, -93.094)]

  new_road_map2 = [("Minnesota", "Saint Paul", 44.95, -93.094),\
                  ("Delaware", "Dover", 39.161921, -75.526755)]

  road_map3 = [("Delaware", "Dover", 0, 0),\
              ("Minnesota", "Saint Paul", 0, 0),\
              ("Alabama", "Montgomery", 0, 0),\
              ("Alaska", "Juneau", 0, 0),\
              ("Arizona", "Phoenix", 0, 0 )]

  new_road_map3 = [("Delaware", "Dover", 0, 0),\
                  ("Alaska", "Juneau", 0, 0),\
                  ("Alabama", "Montgomery", 0, 0),\
                  ("Minnesota", "Saint Paul", 0, 0),\
                  ("Arizona", "Phoenix", 0, 0)]

  x1,y1 = new_road_map[0][2], new_road_map[0][3]
  x2,y2 = new_road_map[1][2], new_road_map[1][3]
  x3,y3 = new_road_map[2][2], new_road_map[2][3]
  x4,y4 = new_road_map2[0][2], new_road_map2[0][3]
  x5,y5 = new_road_map2[1][2], new_road_map2[1][3]

  distance = (math.sqrt((x1-x2)**2 + (y1-y2)**2)) + (math.sqrt((x2-x3)**2 + (y2-y3)**2)) + (math.sqrt((x3-x1)**2 + (y3-y1)**2))
  distance2 = (math.sqrt((x4-x5)**2 + (y4-y5)**2)) + (math.sqrt((x4-x5)**2 + (y4-y5)**2))

  assert swap_cities(road_map, 0, 1) ==\
              (new_road_map, pytest.approx(distance, 0.01)),\
              "*********** Swaping index 0 and 1 did not take place ************"

  assert swap_cities(road_map2, 0, 1) !=\
              (new_road_map, pytest.approx(distance, 0.01)),\
              "*********** Swaping wrong value asssertion test ************"

  assert swap_cities(road_map2, 0, 1) ==\
              (new_road_map2, pytest.approx(distance2, 0.01)),\
              "*********** Swaping index 0 and 1 did not take place ************"

  assert swap_cities(road_map3, 1,3) ==\
              (new_road_map3, 0),\
              "*********** Swaping index 1 and 3 with 0 distance did not take place ************"

  assert swap_cities(road_map3, 3, 3) ==\
              (road_map3, 0),\
               "*********** Swaping same index 'no swap' did not work ************"

  assert swap_cities(road_map3, 0, 0) ==\
              (road_map3, 0),\
               "*********** Swaping index ZERO 'no swap' did not wwork ************"

# ****************************


def test_shift_cities():

  road_map3 = [("Kentucky", "Frankfort", 38.197274, -84.86311),\
              ("Delaware", "Dover", 39.161921, -75.526755),\
              ("Minnesota", "Saint Paul", 44.95, -93.094)]

  new_road_map3 = [("Minnesota", "Saint Paul", 44.95, -93.094),\
                  ("Kentucky", "Frankfort", 38.197274, -84.86311),\
                  ("Delaware", "Dover", 39.161921, -75.526755)]

  road_map4 = [("Kentucky", "Frankfort", 38.197274, -84.86311)]

  road_map5 = [("Alabama", "Montgomery", 32.361538, -6.279118),\
              ("Alaska", "Juneau", 8.301935, -134.41974),\
              ("Alabama", "Montgomery", 0.361538, -16.279118),\
              ("Alaska", "Juneau", 78.301935, -14.41974),\
              ("Alaska", "Juneau", 8.301935, -134.41974),\
              ("Alabama", "Montgomery", 87.361538, -0.279118),\
              ("Alaska", "Juneau", 52.301935, -90.41974),\
              ("Arizona", "Phoenix", 33.448457, -112.073844 ),\
              ("Alabama", "Montgomery", 32.361538, -6.279118),\
              ("Alaska", "Juneau", 8.301935, -134.41974),\
              ("Alabama", "Montgomery", 87.361538, -16.279118),\
              ("Alaska", "Juneau", 78.301935, -14.41974),\
              ("Alaska", "Juneau", 8.301935, -134.41974),\
              ("Alabama", "Montgomery", 87.361538, -0.279118),\
              ("Alaska", "Juneau", 529.301935, -0.41974),\
              ("Arizona", "Phoenix", 303.448457, -112.073844),\
              ("Alaska", "Juneau", 8.301935, -134.41974),\
              ("Alabama", "Montgomery", 87.361538, -16.279118),\
              ("Alaska", "Juneau", 78.301935, -14.41974),\
              ("Alaska", "Juneau", 8.301935, -14.41974),\
              ("Alabama", "Montgomery", 8.361538, -0.279118),\
              ("Alaska", "Juneau", 52.301935, -90.41974),\
              ("Arizona", "Phoenix", 33.448457, -112.073844 ),\
              ("Alabama", "Montgomery", 32.361538, -6.279118),\
              ("Alaska", "Juneau", 8.301935, 134.41974),\
              ("Alabama", "Montgomery", 87.361538, -16.279118),\
              ("Alaska", "Juneau", 0.301935, -14.41974),\
              ("Alaska", "Juneau", 8.301935, -134.41974),\
              ("Alabama", "Montgomery", 87.361538, 0.279118),\
              ("Alaska", "Juneau", 52.301935, -90.41974),\
              ("Arizona", "Phoenix", 33.448457, -112.073844)]

  assert type(shift_cities(road_map3)) == type(new_road_map3),\
              "********** Shifting did not return correct type **********"

  assert shift_cities(road_map3) == new_road_map3,\
              "********** Shifting did not take place **********"

  assert (shift_cities(road_map5))[0] == ("Arizona", "Phoenix", 33.448457, -112.073844),\
              "********** Shifting index check/ looping (last to first) not working **********"

  assert shift_cities(road_map4) == road_map4,\
              "********** Shifting method wwhere one element only did not work **********"

# ****************************


def test_read_cities():

  road_map6 = [("Alabama", "Montgomery", 32.361538, -86.279118),\
              ("Alaska", "Juneau", 58.301935, -134.41974),\
              ("Arizona", "Phoenix", 33.448457, -112.073844 )]

  inputfilepath="test-city-data.txt"

  assert type(read_cities(inputfilepath)) == type(road_map6),\
              "********** Road map reading not returning the correct type **********"

  assert read_cities(inputfilepath) == road_map6,\
              "********** Road map reading did not take place **********"

# ****************************


def test_print_cities():

  road_map7 = [("Alabama", "Montgomery", 32.361538, -86.279118),\
              ("Alaska", "Juneau", 58.301935, -134.41974),\
              ("Arizona", "Phoenix", 33.448457, -112.073844 )]


  # road_map7_printed = "Alabama, Montgomery, 32.36, -86.28\nAlaska, Juneau, 58.3, -134.42\nArizona, Phoenix, 33.45, -112.07\n"

  assert type(print_cities(road_map7)) == str,\
              "********** Cities printing returns wrong type **********"
# ****************************


def test_print_map():

  road_map7 = [("Alabama", "Montgomery", 32.361538, -86.279118),\
                ("Alaska", "Juneau", 58.301935, -134.41974),\
                ("Arizona", "Phoenix", 33.448457, -112.073844 )]

  assert type(print_map(road_map7)) == str,\
              "********** Map printing returns wrong type **********"
# ****************************


def test_find_best_cycle():

  road_map7 = [("Alabama", "Montgomery", 32.361538, -86.279118),\
                ("Alaska", "Juneau", 58.301935, -134.41974),\
                ("Arizona", "Phoenix", 33.448457, -112.073844 )]

  assert type(find_best_cycle(road_map7)) == list,\
              "********** Finding cycle returns wrong type **********"
