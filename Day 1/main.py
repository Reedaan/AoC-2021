data = open("D:\Python\AoC 2021\Day 1\input.txt", "r").readlines()
data = [line.strip(" ") for line in data]
data = [line.strip("\n") for line in data]
data = [line.replace(" ", "") for line in data]

data = [int(line) for line in data]
part_two_data = []

def part_one():
    
    a = 1

    for line in range(len(data)):
        if data[line] >= data[line - 1]:
            a += 1
            
    return a

def part_two():
    
    b = 0
    
    for line in range(len(data)):
        try:
            a = data[line] + data[line + 1] + data[line + 2]
            part_two_data.append(a)
        except IndexError:
            break
                
    for c in range(len(part_two_data)):
        if part_two_data[c] > part_two_data[c - 1]:
            b += 1

    print(b)

print(part_one())
print(part_two())
