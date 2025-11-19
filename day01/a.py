with open('input.txt', 'r') as f:
    lines = f.readlines()

total = 0
sum = 0

for line in lines:
    if line != '\n':
        sum += int(line)
    else:
        total = max(total, sum)
        sum = 0


print(total)