command = input('Куда идем? ')
step = int(input('Сколько делаем шагов? '))
start = int(input('От куда начинаем? '))

if command == 'вперед':
	finish = step + start
elif command == 'назад':
    finish = start - step

print(finish % 100)
