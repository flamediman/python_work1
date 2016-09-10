import math
s_river = float(input('введите скорость реки '))
s_boat = float(input('введите скорость лодки '))
width = float(input('введите ширину реки '))
time = width / s_boat
way_r = time * s_river
all_way = math.sqrt((width ** 2) + (way_r ** 2))
print(all_way)
