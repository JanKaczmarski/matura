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
	to_swap_id = writting.find(x)
	new_letter = following_letter[writting[to_swap_id]]
	return f'{writting[:to_swap_id]}{new_letter}{writting[to_swap_id+1:]}'


inst_to_func = {'DOPISZ': dopisz, 'ZMIEN': zmien, 'USUN': usun, 'PRZESUN': przesun}

def ex1():
	solution = ''

	for instrucion in instructions:
		solution = inst_to_func[instrucion[0]](solution, instrucion[1])

	return len(solution)

def ex2():
	last_inst = instructions[0][0]
	solution = ('', 0)
	current_len = 1
	for instrucion in instructions:
		if instrucion[0] != last_inst:
			if current_len > solution[1]:
				solution = (last_inst, current_len)
			current_len = 1
			last_inst = instrucion[0]
		else:
			current_len += 1
	if current_len > solution[1]:
		solution = (last_inst, current_len)

	return solution

def ex3():
	dopisz_args = {}
	for instruction in instructions:
		key_word = instruction[0]
		arg = instruction[1]
		if key_word == 'DOPISZ':
			try:
				dopisz_args[arg] += 1
			except KeyError:
				dopisz_args[arg] = 1

	return [(key, value) for key, value in dopisz_args.items() if max(dopisz_args.values()) == value][0]

def ex4():
	solution = ''

	for instrucion in instructions:
		solution = inst_to_func[instrucion[0]](solution, instrucion[1])

	return solution

#print(ex3())

print(f'Zadanie 1: {ex1()}\nZadanie 2: {ex2()}\nZadanie 3: {ex3()}\nZadanie 4: {ex4()}')