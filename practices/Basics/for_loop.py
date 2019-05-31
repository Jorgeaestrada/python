bag = [10, 20, 30, 40, 50, 60, 70]

print(bag)
len(bag)

for item in bag:
    print(item)

for item in bag:
    if item == 70:
        print('so coooooool')
    else:
        print('this is not cool')

i = 0
for item in bag:
    i += 1
    print(i)
