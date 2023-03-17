with open("Dane_2212/mecz.txt", "r") as file:
	game = [line for line in file][0]

	# n of strikes, number, longest

	strikes = {'A': [0, 'A', 0], 'B': [0, 'B', 0]}

	current_score = game[0]


	for score in game[1:]:
		last_score = current_score[0]
		if score != last_score and len(current_score) >= 10:
			strikes[last_score][0] += 1
			if strikes[last_score][2] < len(current_score):
				strikes[last_score][2] = len(current_score)

		if score != last_score:
			current_score = score

		else:
			current_score += score

	if len(current_score) >= 10:
		score = current_score[0]
		strikes[score][0] += 1
		if len(current_score) > strikes[score][2]:
			strikes[score][2] = len(current_score)

print(strikes)
