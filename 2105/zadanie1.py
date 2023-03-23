from string import ascii_uppercase



instructions = []
with open('DANE_2105/instrukcje.txt', "r") as file:
	for line in file:
		splitted_line = line[:-1].split(' ')
		instructions.append( (splitted_line[0], splitted_line[1]) )

def create_following_letter():
	alphabeth = list(ascii_uppercase)
	following_letter = {alphabeth[i]: alphabeth[i+1] for i in range(len(alphabeth)-1)}
	following_letter['Z'] = 'A'
	return following_letter

following_letter = create_following_letter()

def zmien(writting, x):
	return f'{writting[:-1]}{x}'

def dopisz(writting, x):
	return f'{writting}{x}'

def usun(writting, x):
	return writting[:-1]

def przesun(writting, x):
	new_letter = following_letter[writting[-1]]
	return f'{writting[:-1]}{new_letter}'


inst_to_func = {'DOPISZ': dopisz, 'ZMIEN': zmien, 'USUN': usun, 'PRZESUN': przesun}

def ex1():
	solution = ''

	for instrucion in instructions:
		solution = inst_to_func[instrucion[0]](solution, instrucion[1])

	return len(solution)

def ex2():
	pass

print(f'Zadanie 1: {ex1()}\nZadanie 2: TODO')