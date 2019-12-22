# -*- coding: utf-8 -*-
import random
import codecs
import unicodedata


def read_cities(file_name):
  infile = open(file_name, "r")
  line = infile.readline()
  road_map = []

  while line:
    value = tuple(line.rstrip('\n').split("\t"))
    value = (value[0],value[1],float(value[2]),float(value[3]))
    road_map.append(value)
    line = infile.readline()

  return(road_map)
  """
  Read in the cities from the given `file_name`, and return
  them as a list of four-tuples:

    [(state, city, latitude, longitude), ...]

  Use this as your initial `road_map`, that is, the cycle

  Alabama -> Alaska -> Arizona -> ... -> Wyoming -> Alabama.
  """

def print_cities(road_map):

  for el in road_map:
    road_map_str = ""
    for i in range(0, len(el)):
      if type(el[i]) == float:
        if i < 3:
          road_map_str += (str(round(el[i], 2)) + ", ")
        else:
          road_map_str += (str(round(el[i], 2)))
      else:
        road_map_str += (el[i] + ", ")

    return(road_map_str)

  """
  Prints a list of cities, along with their locations.
  Print only one or two digits after the decimal point.
  """


def compute_total_distance(road_map):
    """
    Returns, as a floating point number, the sum of the distances of all
    the connections in the `road_map`. Remember that it's a cycle, so that
    (for example) in the initial `road_map`, Wyoming connects to Alabama...
    """
    pass


def swap_cities(road_map, index1, index2):
    """
    Take the city at location `index` in the `road_map`, and the
    city at location `index2`, swap their positions in the `road_map`,
    compute the new total distance, and return the tuple

        (new_road_map, new_total_distance)

    Allow for the possibility that `index1=index2`,
    and handle this case correctly.
    """
    pass

def shift_cities(road_map):
    """
    For every index i in the `road_map`, the city at the position i moves
    to the position i+1. The city at the last position moves to the position
    0. Return the new road map.
    """
    pass

def find_best_cycle(road_map):
    """
    Using a combination of `swap_cities` and `shift_cities`,
    try `10000` swaps/shifts, and each time keep the best cycle found so far.
    After `10000` swaps/shifts, return the best cycle found so far.
    Use randomly generated indices for swapping.
    """
    pass

def print_map(road_map):
    """
    Prints, in an easily understandable format, the cities and
    their connections, along with the cost for each connection
    and the total cost.
    """
    pass

def main():
    """
    Reads in, and prints out, the city data, then creates the "best"
    cycle and prints it out.
    """
    pass

if __name__ == "__main__": #keep this in

    # read_cities("test-city-data.txt")
    # print_cities([("Alabama", "Montgomery", 32.361538, -86.279118),\
    #           ("Alaska", "Juneau", 58.301935, -134.41974),\
    #           ("Arizona", "Phoenix", 33.448457, -112.073844 )])
    main()

