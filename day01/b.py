with open('input.txt', 'r') as f:
    lines = f.readlines()

totals = []
total = 0

for line in lines:
    if line != '\n':
        total += int(line)
    else:
        totals.append(total)
        total = 0

totals.sort(reverse=True)

print(sum(totals[:3]))