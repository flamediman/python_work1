rate = 74
euro = 1
print(euro * rate)


area_t = 0.09
area_f = 10
quantity = area_f // area_t
if quantity % 10 > 0:
    print(int(quantity) + 1)
else:
	print(quantity)


stripes = 2
collors = 3
print(collors ** stripes)


rate = 74.544
euro = 1
rub = euro * rate
kop = ((int(rub * 10) % 10) * 10 + (int(rub * 100) % 10)) / 100
print(int(rub) + kop)


import math
rad = 5
size = (4 * math.pi * (rad ** 3)) / 3
print(size)


