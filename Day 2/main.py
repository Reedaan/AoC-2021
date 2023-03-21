data = open("D:\Python\AoC 2021\Day 2\input.txt", "r").readlines()
data = [line.strip(" ") for line in data]
data = [line.strip("\n") for line in data]
data = [line.replace(" ", "") for line in data]

# Part one

def part_one():
    
    x = 0
    y = 0

    for line in data:
        line_number = int(line[::-1][0])
        line_string = line[:-1]
        
        if line_string == "forward":
            x = x + line_number
        elif line_string == "down":
            y = y + line_number
        elif line_string == "up":
            y = y - line_number
        
    return x*y
        
#Part two    
    
def part_two():
        
    x = 0
    y = 0
    aim = 0

    for line in data:
        line_number = int(line[::-1][0])
        line_string = line[:-1]
        
        if line_string == "forward":
            x = x + line_number
            y = y + (aim * line_number)
        elif line_string == "down":
            aim = aim + line_number
        elif line_string == "up":
            aim = aim - line_number
        
    return x*y
       
print(part_one())
print(part_two())     
        
