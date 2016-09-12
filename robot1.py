command = input('Куда идем? ')
step = int(input('Сколько делаем шагов? '))
start = int(input('От куда начинаем? '))

if command == 'вперед':
	finish = step + start
elif command == 'назад':
    finish = start - step

if finish > 99:
   print(99)
elif finish < 0:
   print(0)
else:
    print(finish)
