result = {}
keys = []
hobbes = []

with open('users.csv', 'r', encoding='utf-8') as f:
    for line in f:
        elem = [line[:line.index(',')]]
        line = line[line.index(',') + 1:]
        elem.append(line[:line.index(',')])
        elem.append(line[line.index(',') + 1:-1])
        keys.append(tuple(elem))
# print(keys)

with open('hobby.csv', 'r', encoding='utf-8') as f:
    for line in f:
        hobbes.append(line[:-1])
# print(hobbes)

if (len(keys) == len(hobbes)) or (len(keys) < len(hobbes)):
    for i in range(len(keys)):
        result.setdefault(keys[i], hobbes[i])
elif len(keys) > len(hobbes):
    for i in range(len(keys)):
        if i < len(hobbes):
            hobby = hobbes[i]
        else:
            hobby = None
        result.setdefault(keys[i], hobby)

for key in result:
    print(*key, ':', result[key])
