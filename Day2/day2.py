sum = 0
trigger = 0

with open('input.txt', 'r') as file:
	for line in file:
		trigger = 0
		game = line.strip().split(':')
		sets = game[1].strip().split(';')
		for i in range(len(sets)):
			colour = sets[i].strip().split(',')
			for j in range(len(colour)):
				if colour[j].strip().split(' ')[1].strip() == 'red':
					if int(colour[j].strip().split(' ')[0].strip()) > 12:
						trigger = 1
						break
				if colour[j].strip().split(' ')[1].strip() == 'green':
					if int(colour[j].strip().split(' ')[0].strip()) > 13:
						trigger = 1
						break
				if colour[j].strip().split(' ')[1].strip() == 'blue':
					if int(colour[j].strip().split(' ')[0].strip()) > 14:
						trigger = 1
						break
		if trigger == 0:
			print(game[0].strip().split(' ')[1])
			sum += int(game[0].strip().split(' ')[1])

print(sum)
