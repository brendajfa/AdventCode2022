f = open("day1_input.txt", "r")
data = f.read()
data1 = data.split("\n")
print(data)

acum = 0
total = []
for calories in data1:
    if calories == '':
        total.append(acum)
        acum = 0
    else:
        acum += int(calories)
print(total)

max_three = []

for i in range (3):
    max_three.append(max(total))
    total[total.index(max(total))] = 0

print(max_three)
print(sum(max_three))

