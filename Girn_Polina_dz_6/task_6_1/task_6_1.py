result = []

with open('nginx_logs.txt', 'r', encoding='utf-8') as f:
    for line in f:
        # print(f.readlines())
        element = [line[:line.index('-') - 1]]
        line = line[line.index('"')+1:]
        element.append(line[:line.index(' ')])
        element.append(line[line.index('/'):line.index('H')-1])
        result.append(tuple(element))
        # print(element)

print('[')
for el in result:
    print(el, end=',\n')
print(']')


