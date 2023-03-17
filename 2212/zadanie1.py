file = open("Dane_2212/mecz.txt", "r")

game = [line for line in file][0][:-1]
last_score = game[0]
sol = 0

for score in game[1:]:
	if score != last_score:
		sol += 1
		last_score = score
	
file.close()

print(sol)
