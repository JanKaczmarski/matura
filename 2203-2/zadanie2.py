with open("Dane_2203-2/statki.txt", "r") as file:
	ships = {} # nr_imo : (name, capacity)
	for line in file:
		line = line[:-1].split(';')
		nr_imo, nazwa_statku, capacity = line[0], line[1], line[2]
		ships[nr_imo] = (nazwa_statku, capacity)

for item in ships.items():
	print(item)
