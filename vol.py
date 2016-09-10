import math
rad_1 = float(input('введите радиус первой сферы '))
rad_2 = float(input('введите радиус второй сферы '))
vol_1 = (4 * math.pi * (rad_1 ** 3)) / 3
vol_2 = (4 * math.pi * (rad_2 ** 3)) / 3
if vol_1 > vol_2:
	print(vol_1 - vol_2)
else:
	print(vol_2 - vol_1)
