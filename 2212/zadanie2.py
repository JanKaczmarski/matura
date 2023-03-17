with open("Dane_2212/mecz.txt", "r") as file:
	game = [line for line in file][0]
	a_won = 0
	b_won = 0
	stop = [True, True]
	i = 0
	while a_won < 1000 and b_won < 1000 or abs(a_won - b_won) < 3:
		if game[i] == 'A':
			a_won += 1
		else:
			b_won += 1

		i += 1

	if a_won > b_won:
		winner = 'A'
	else:
		winner = 'B'

	print(winner ,a_won , b_won)