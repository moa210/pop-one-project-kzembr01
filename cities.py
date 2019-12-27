import random
import codecs
import unicodedata
import math


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


def compute_total_distance(road_map):

  x1,x2,y1,y2 = 0,0,0,0
  total_distance = 0

  for i in range(0, len(road_map)):
    x1,y1 = road_map[i][2], road_map[i][3]

    if i != len(road_map) -1:
      x2,y2 = road_map[i+1][2], road_map[i+1][3]
    else:
      x2,y2 = road_map[0][2], road_map[0][3]

    total_distance = total_distance + (math.sqrt((x1-x2)**2 + (y1-y2)**2))

  return(total_distance)


def swap_cities(road_map, index1, index2):

  first_city, second_city = road_map[index1], road_map[index2]
  new_road_map = []

  for i in range(0, len(road_map)):
    if i == index1:
      new_road_map.append(second_city)
    elif i == index2:
      new_road_map.append(first_city)
    else:
      new_road_map.append(road_map[i])

  new_total_distance = compute_total_distance(new_road_map)

  return((new_road_map, new_total_distance))


def shift_cities(road_map):

  new_road_map = []
  new_road_map.append(road_map[-1])

  for i in range(0, len(road_map)-1):
    new_road_map.append(road_map[i])

  return(new_road_map)


def find_best_cycle(road_map):

  count = 0
  shortest_distance = compute_total_distance(road_map)
  best_cycle = road_map
  N = (len(road_map)-1)

  while (count <=10000):
    number_1 = random.randint(1, N)
    number_2 = random.randint(1, N)
    road_map_tested = shift_cities(road_map)
    distance_tested = compute_total_distance(road_map_tested)

    if (distance_tested < shortest_distance):
      shortest_distance = distance_tested
      best_cycle = road_map_tested

    elif (swap_cities(road_map_tested, number_1, number_2)[1] < shortest_distance):
      shortest_distance = swap_cities(road_map_tested, number_1, number_2)[1]
      best_cycle = swap_cities(road_map_tested, number_1, number_2)[0]

    road_map = best_cycle
    count = count + 1
    # print(type(best_cycle))
  return(best_cycle)


def print_map(road_map):

    """
    no test needed  >>>>>>>>>>>>>>>>>>

    Prints, in an easily understandable format, the cities and
    their connections, along with the cost for each connection
    and the total cost.
    """
    pass

def main():

    """
    no test needed    >>>>>>>>>>>>>>>>>>>>>>>


    Reads in, and prints out, the city data, then creates the "best"
    cycle and prints it out.
    """
    pass

if __name__ == "__main__": #keep this in

    # read_cities("test-city-data.txt")
    # print_cities([("Alabama", "Montgomery", 32.361538, -86.279118),\
    #           ("Alaska", "Juneau", 58.301935, -134.41974),\
    #           ("Arizona", "Phoenix", 33.448457, -112.073844 )])

    # compute_total_distance([("Alabama", "Montgomery", 32.361538, -86.279118),\
    #   ("Alaska", "Juneau", 58.301935, -134.41974),\
    #   ("Arizona", "Phoenix", 33.448457, -112.073844 )])

    # shift_cities([("Alabama", "Montgomery", 32.361538, -86.279118),\
    #   ("Alaska", "Juneau", 58.301935, -134.41974),\
    #   ("Arizona", "Phoenix", 33.448457, -112.073844 )])

    # swap_cities([("Alabama", "Montgomery", 32.361538, -6.279118),\
    #     ("Alaska", "Juneau", 8.301935, -134.41974),\
    #     ("Alabama", "Montgomery", 87.361538, -16.279118),\
    #     ("Alaska", "Juneau", 78.301935, -14.41974),\
    #     ("Alaska", "Juneau", 8.301935, -134.41974),\
    #     ("Alabama", "Montgomery", 87.361538, -0.279118),\
    #     ("Alaska", "Juneau", 52.301935, -90.41974),\
    #     ("Arizona", "Phoenix", 33.448457, -112.073844 )], 1, 5)

    find_best_cycle(read_cities("test-city-data.txt"))

    main()

