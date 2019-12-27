import random
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
        if i < 3: road_map_str += (str(round(el[i], 2)) + ", ")
        else: road_map_str += (str(round(el[i], 2)))
      else: road_map_str += (el[i] + ", ")

    print(road_map_str)



def compute_total_distance(road_map):

  x1,x2,y1,y2 = 0,0,0,0
  total_distance = 0

  for i in range(0, len(road_map)):
    x1,y1 = road_map[i][2], road_map[i][3]
    if i != len(road_map) -1: x2,y2 = road_map[i+1][2], road_map[i+1][3]
    else: x2,y2 = road_map[0][2], road_map[0][3]
    total_distance = total_distance + (math.sqrt((x1-x2)**2 + (y1-y2)**2))

  return(total_distance)



def swap_cities(road_map, index1, index2):

  first_city, second_city = road_map[index1], road_map[index2]
  new_road_map = []

  for i in range(0, len(road_map)):
    if i == index1: new_road_map.append(second_city)
    elif i == index2: new_road_map.append(first_city)
    else: new_road_map.append(road_map[i])

  new_total_distance = compute_total_distance(new_road_map)

  return((new_road_map, new_total_distance))



def shift_cities(road_map):

  new_road_map = []
  new_road_map.append(road_map[-1])

  for i in range(0, len(road_map)-1): new_road_map.append(road_map[i])

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

  return(best_cycle)



def print_map(road_map):

    distance = str(int(round(compute_total_distance(road_map))))
    first_city = road_map[0][1]
    first_state = road_map[0][0]
    last_city = road_map[len(road_map)-1][1]
    last_state = road_map[len(road_map)-1][0]
    stops = str(len(road_map))

    print("\nYou'll be traveling from " + first_city +
          " in " + first_state + " to " + last_city + " in " + last_state + ".")

    print("The overall distance of your trip is " +
          distance + " miles and you'll visit " +  stops + " cities in total (Yee-haw!!!).")

    print("\nSo you will travel from:")
    print_short_trips(road_map)



def print_short_trips(road_map):

    for i in range(0, len(road_map)):
      if i == (len(road_map)-1):
        print("and finally back to where you've started; " + road_map[i][1] + " to " + road_map[0][1] +
              ".\n" + "\n********** Have a wonderful trip! **************\n")
      else:
        distance = math.sqrt((road_map[i][2]-road_map[i+1][2])**2 + (road_map[i][3]-road_map[i+1][3])**2)
        print(road_map[i][1] + " to " + road_map[i+1][1] +" (it will be " +str(int(distance))+" miles),")



def main():

  road_map = read_cities("city-data.txt")
  print_cities(road_map)
  best_cycle = find_best_cycle(road_map)
  print_map(best_cycle)

if __name__ == "__main__": #keep this in

  main()

