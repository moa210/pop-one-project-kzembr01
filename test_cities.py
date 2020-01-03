import pytest
import math
from cities import *


def test_compute_total_distance():

  	assert type(compute_total_distance(road_map_1)) == float, \
  		"* Compute total distance return type not correct *"

  	assert compute_total_distance(road_map_1) == \
      pytest.approx(9.386 + 18.496 + 10.646, 0.01), \
  		"* Compute total distance 1: did not take place *"

  	assert compute_total_distance(road_map_3) == (0), \
  		"* Compute total distance 2: did not take place *"

  	assert compute_total_distance(road_map_0) == pytest.approx(9.386 + 9.386, 0.01), \
  		"* Compute total distance for 2 elements return not correct *"


def test_swap_cities():

  	assert swap_cities(road_map_1, 0, 1) == \
      (new_road_map_1, pytest.approx(distance, 0.01)), \
  		"* Swaping index 0 and 1 did not take place *"

  	assert swap_cities(road_map_2, 0, 1) != \
      (new_road_map_1, pytest.approx(distance, 0.01)), \
  		"* Swaping wrong value asssertion test *"

  	assert swap_cities(road_map_2, 0, 1) == \
  	  (new_road_map_2, pytest.approx(distance2, 0.01)), \
  		"* Swaping index 0 and 1 did not take place *"

  	assert swap_cities(road_map_3, 1, 3) == \
  	  (new_road_map_3, 0), \
  		"* Swaping index 1 and 3 with 0 distance did not take place *"

  	assert swap_cities(road_map_3, 3, 3) == \
  	  (road_map_3, 0), \
  		"* Swaping same index 'no swap' did not work *"

  	assert swap_cities(road_map_3, 0, 0) == \
  	  (road_map_3, 0), \
  		"* Swaping index ZERO 'no swap' did not wwork *"


def test_shift_cities():

  	assert type(shift_cities(road_map_1)) == type(new_road_map_1_1), \
  		"* Shifting did not return correct type *"

  	assert shift_cities(road_map_1) == new_road_map_1_1, \
  		"* Shifting did not take place *"

  	assert (shift_cities(road_map_5))[0] == ("Arizona", "Phoenix", 33.448457, -112.073844), \
  		"* Shifting index check/ looping (last to first) not working *"

  	assert shift_cities(road_map_4) == road_map_4, \
  		"* Shifting method wwhere one element only did not work *"


def test_find_params():

  	assert find_params(road_map_6)[0] == pytest.approx(58.301935 - 32.361538, 0.01), \
  		"* Height value not calculated - 1st test *"

  	assert find_params(road_map_6)[1] == pytest.approx(134.41974 - 86.279118, 0.01), \
  		"* Width value not calculated - 1st test *"

  	assert find_params(road_map_3)[0] == pytest.approx(0), \
  		"* Height value not calculated - 2nd test *"

  	assert find_params(road_map_3)[0] == pytest.approx(0), \
  		"* Width value not calculated - 2nd test *"

  	assert find_params(road_map_6)[2] == pytest.approx(32.361, 0.01), \
  		"* Min_x value not calculated - 2nd test *"

  	assert find_params(road_map_6)[4] == pytest.approx(58.301, 0.01), \
  		"* Max_x value not calculated - 2nd test *"

  	assert find_params(road_map_6)[3] == pytest.approx(-134.419, 0.01), \
  		"* Min_y value not calculated - 2nd test *"

  	assert find_params(road_map_6)[5] == pytest.approx(-86.279, 0.01), \
  		"* Max_y value not calculated - 2nd test *"


def test_read_cities():

    assert type(read_cities(inputfilepath)) == type(road_map_6), \
    	"* Road map reading not returning the correct type *"

    assert read_cities(inputfilepath) == road_map_6, \
    	"* Road map reading did not take place *"


def test_find_best_cycle():

    assert type(find_best_cycle(road_map_6)) == list, \
    	"* Finding cycle returns wrong type *"

    assert find_best_cycle(road_map_6) == new_road_map_6, \
      "* Finding cycle returns wrong data *"



inputfilepath = "test-city-data.txt"

road_map_0 = [("Kentucky", "Frankfort", 38.197274, -84.86311), \
            ("Delaware", "Dover", 39.161921, -75.526755)]

road_map_1 = [("Kentucky", "Frankfort", 38.197274, -84.86311), \
            ("Delaware", "Dover", 39.161921, -75.526755), \
            ("Minnesota", "Saint Paul", 44.95, -93.094)]

new_road_map_1 = [("Delaware", "Dover", 39.161921, -75.526755), \
                ("Kentucky", "Frankfort", 38.197274, -84.86311), \
                ("Minnesota", "Saint Paul", 44.95, -93.094)]

new_road_map_1_1 = [("Minnesota", "Saint Paul", 44.95, -93.094), \
                  ("Kentucky", "Frankfort", 38.197274, -84.86311), \
                  ("Delaware", "Dover", 39.161921, -75.526755)]

road_map_2 = [("Delaware", "Dover", 39.161921, -75.526755), \
            ("Minnesota", "Saint Paul", 44.95, -93.094)]

new_road_map_2 = [("Minnesota", "Saint Paul", 44.95, -93.094), \
                ("Delaware", "Dover", 39.161921, -75.526755)]

road_map_3 = [("Delaware", "Dover", 0, 0), \
            ("Minnesota", "Saint Paul", 0, 0), \
            ("Alabama", "Montgomery", 0, 0), \
            ("Alaska", "Juneau", 0, 0), \
            ("Arizona", "Phoenix", 0, 0)]

new_road_map_3 = [("Delaware", "Dover", 0, 0), \
              ("Alaska", "Juneau", 0, 0), \
              ("Alabama", "Montgomery", 0, 0), \
              ("Minnesota", "Saint Paul", 0, 0), \
              ("Arizona", "Phoenix", 0, 0)]

road_map_4 = [("Kentucky", "Frankfort", 38.197274, -84.86311)]

road_map_5 = [("Alabama", "Montgomery", 32.361538, -6.279118), \
            ("Alaska", "Juneau", 8.301935, -134.41974), \
            ("Alabama", "Montgomery", 0.361538, -16.279118), \
            ("Alaska", "Juneau", 78.301935, -14.41974), \
            ("Alaska", "Juneau", 8.301935, -134.41974), \
            ("Alabama", "Montgomery", 87.361538, -0.279118), \
            ("Alaska", "Juneau", 52.301935, -90.41974), \
            ("Arizona", "Phoenix", 33.448457, -112.073844), \
            ("Alabama", "Montgomery", 32.361538, -6.279118), \
            ("Alaska", "Juneau", 8.301935, -134.41974), \
            ("Alabama", "Montgomery", 87.361538, -16.279118), \
            ("Alaska", "Juneau", 78.301935, -14.41974), \
            ("Alaska", "Juneau", 8.301935, -134.41974), \
            ("Alabama", "Montgomery", 87.361538, -0.279118), \
            ("Alaska", "Juneau", 529.301935, -0.41974), \
            ("Arizona", "Phoenix", 303.448457, -112.073844), \
            ("Alaska", "Juneau", 8.301935, -134.41974), \
            ("Alabama", "Montgomery", 87.361538, -16.279118), \
            ("Alaska", "Juneau", 78.301935, -14.41974), \
            ("Alaska", "Juneau", 8.301935, -14.41974), \
            ("Alabama", "Montgomery", 8.361538, -0.279118), \
            ("Alaska", "Juneau", 52.301935, -90.41974), \
            ("Arizona", "Phoenix", 33.448457, -112.073844), \
            ("Alabama", "Montgomery", 32.361538, -6.279118), \
            ("Alaska", "Juneau", 8.301935, 134.41974), \
            ("Alabama", "Montgomery", 87.361538, -16.279118), \
            ("Alaska", "Juneau", 0.301935, -14.41974), \
            ("Alaska", "Juneau", 8.301935, -134.41974), \
            ("Alabama", "Montgomery", 87.361538, 0.279118), \
            ("Alaska", "Juneau", 52.301935, -90.41974), \
            ("Arizona", "Phoenix", 33.448457, -112.073844)]

road_map_6 = [("Alabama", "Montgomery", 32.361538, -86.279118), \
            ("Alaska", "Juneau", 58.301935, -134.41974), \
            ("Arizona", "Phoenix", 33.448457, -112.073844)]

new_road_map_6 = [("Arizona", "Phoenix", 33.448457, -112.073844),\
                ("Alabama", "Montgomery", 32.361538, -86.279118), \
                ("Alaska", "Juneau", 58.301935, -134.41974)]

x1, y1 = new_road_map_1[0][2], new_road_map_1[0][3]
x2, y2 = new_road_map_1[1][2], new_road_map_1[1][3]
x3, y3 = new_road_map_1[2][2], new_road_map_1[2][3]
x4, y4 = new_road_map_2[0][2], new_road_map_2[0][3]
x5, y5 = new_road_map_2[1][2], new_road_map_2[1][3]

distance = (math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)) + (math.sqrt((x2 - x3) \
  ** 2 + (y2 - y3) ** 2)) + ( math.sqrt((x3 - x1) ** 2 + (y3 - y1) ** 2))
distance2 = (math.sqrt((x4 - x5) ** 2 + (y4 - y5) ** 2)) + (math.sqrt((x4 - x5) \
  ** 2 + (y4 - y5) ** 2))


