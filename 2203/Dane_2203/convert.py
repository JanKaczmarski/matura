new_lines = ""
with open("przybycia.txt", "r") as file:
    for line in file:
        new_line = line
        day, month, year = line[2], 0, 0
        print(day, month, year)
        
#with open("przybycia.txt", "w") as file:
#    file.write(new_lines)